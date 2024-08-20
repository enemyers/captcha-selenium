from selenium import webdriver
from selenium.webdriver.common.by import By

from pypasser import reCaptchaV2

#from pyvirtualdisplay import Display

from flask import jsonify

def get_papeleta(placa):

    #SILENT BROWSER
    #display = Display(visible=0, size=(800, 600))
    #display.start()

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.sat.gob.pe/VirtualSAT/modulos/papeletas.aspx?mysession=xUQo%2bVlFtAGfa0%2fNIUx%2bmrUXt6JElgEMs%2bO6MxyVbEc%3d")

    driver.find_element(By.XPATH, '//*[@id="tipoBusquedaPapeletas"]/option[2]').click()

    driver.find_element(By.XPATH, '//*[@id="ctl00_cplPrincipal_txtPlaca"]').send_keys(placa)

    recaptcha_response = reCaptchaV2(driver)

    print('recaptcha:', recaptcha_response)

    driver.find_element(By.XPATH, '//*[@id="ctl00_cplPrincipal_CaptchaContinue"]').click()

    data = driver.find_element(By.XPATH, '//*[@id="ctl00_cplPrincipal_divMsg"]')

    result = data.text

    data = {
        'result': result
    }

    # Stop silent browser
    #display.stop()

    # Close the driver or keep it open if needed
    driver.quit()

    return jsonify({"data": data})