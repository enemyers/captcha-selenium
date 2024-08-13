from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
import easyocr

from flask import jsonify

def get_placa(placa):
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

    return jsonify({"message": "Placa processed successfully!"})