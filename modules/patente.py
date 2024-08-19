from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from pyvirtualdisplay import Display
import base64
import easyocr

from flask import jsonify

def get_placa(placa):

    #SILENT BROWSER
    display = Display(visible=0, size=(800, 600))
    display.start()

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get("https://portal.mtc.gob.pe/reportedgtt/form/frmconsultaplacaitv.aspx")

    captchaImage = driver.find_element(By.XPATH, '//*[@id="imgCaptcha"]')

    captchaImageSave = driver.execute_async_script("""
        var ele = arguments[0], callback = arguments[1];
        ele.addEventListener('load', function fn(){
            ele.removeEventListener('load', fn, false);
            var cnv = document.createElement('canvas');
            cnv.width = this.width; cnv.height = this.height;
            cnv.getContext('2d').drawImage(this, 0, 0);
            callback(cnv.toDataURL('image/jpeg').substring(22));
        }, false);
        ele.dispatchEvent(new Event('load'));
        """, captchaImage)

    with open(r"./images/captcha.jpg", 'wb') as f:
        f.write(base64.b64decode(captchaImageSave))

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext('./images/captcha.jpg')

    captchaResult = None
    if result:
        captchaResult = result[0][1]
        print(f"CAPTCHA Result: {captchaResult}")
    else:
        return jsonify({"error": "Failed to read CAPTCHA"}), 400

    driver.find_element(By.XPATH, '//*[@id="txtPlaca"]').send_keys(placa)
    driver.find_element(By.XPATH, '//*[@id="txtCaptcha"]').send_keys(captchaResult)
    driver.find_element(By.XPATH, '//*[@id="BtnBuscar"]').click()

    # Close the driver or keep it open if needed
    # driver.quit()

    #Extract data

    WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/form/div[4]/div/div/div[2]/div[2]/div/div/div[6]/div[2]/div/div/div/table')))
    tabla_1 = driver.find_element(By.XPATH, '//*[@id="divDetalle"]/div[2]/div/div/div/table')
    tabla_1 = tabla_1.text

    WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/form/div[4]/div/div/div[2]/div[2]/div/div/div[6]/div[3]/div/div/div/table')))
    tabla_2 = driver.find_element(By.XPATH, '//*[@id="divDetalle"]/div[3]/div/div/div/table')
    tabla_2 = tabla_2.text

    WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/form/div[4]/div/div/div[2]/div[2]/div/div/div[6]/div[4]/div/div/div/table')))
    tabla_3 = driver.find_element(By.XPATH, '//*[@id="gvBonificacion"]')
    tabla_3 = tabla_3.text
    
    data = {
        'tabla1': tabla_1,
        'tabla2': tabla_2,
        'tabla3': tabla_3
    }

    # Stop silent browser
    display.stop()

    return jsonify({"data": data})