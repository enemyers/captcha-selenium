from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
import easyocr # este es el OCR


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

with open(r"captcha.jpg", 'wb') as f:
    f.write(base64.b64decode(captchaImageSave))

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext('captcha.jpg')

    for x in result:
        captchaResult = x[1]

        print(captchaResult)

        driver.find_element(By.XPATH, '//*[@id="txtPlaca"]').send_keys('AUH628')

        driver.find_element(By.XPATH, '//*[@id="txtCaptcha"]').send_keys(captchaResult)

        driver.find_element(By.XPATH, '//*[@id="BtnBuscar"]').click()
