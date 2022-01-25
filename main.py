from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime


def find_by_text(driver, text, several=False):
    if several:
        return driver.find_elements("xpath","//*[contains(text(), '" + text + "')]")
    return driver.find_element("xpath","//*[contains(text(), '" + text + "')]")


def wait_for_element_to_be_clickable(driver, element):
    while True:
        try:
            element.click()
            break
        except:
            sleep(1)

class Bot:
    def __init__(self) -> None:
        self.main_url = "https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng?sprachauswahl=en"
        print('Bot started\nPress Ctrl+C to stop\n')
    

    def start_browser(self):
        o = ChromeOptions()
        #o.add_argument("--headless")
        s = Service(ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service = s, options = o)

    def process(self):
        self.driver.get(self.main_url)
        sleep(2)

        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="xi-txt-11"]/p/a/strong')))
        element.click()

        sleep(5)
        while len(self.driver.find_elements("name","gelesen"))==0:
            sleep(2)
        self.driver.find_element('name','gelesen').click()
        sleep(3)
        while len(self.driver.find_elements("class name","ui-button-text"))==0:
            sleep(2)
        self.driver.find_element('class name','ui-button-text').click()
        while len(self.driver.find_elements('name','sel_staat'))==0:
            sleep(1)
        sleep(3)
        Select(self.driver.find_element('name','sel_staat')).select_by_visible_text('Peru')
        sleep(3)
        Select(self.driver.find_element('name','personenAnzahl_normal')).select_by_visible_text('one person')
        sleep(3)
        Select(self.driver.find_element('name',"lebnBrMitFmly")).select_by_visible_text("no")
        sleep(3)
        self.driver.find_element('name','applicationForm:managedForm:proceed').click()
        sleep(3)
        find_by_text(self.driver,"Apply for a residence title").click()
        sleep(3)
        find_by_text(self.driver,"Economic activity").click()
        sleep(3)
        find_by_text(self.driver,"EU Blue Card / Blaue Karte EU (sect. 18b para. 2)").click()
        sleep(10)
        self.driver.find_element('name','applicationForm:managedForm:proceed').click()
        sleep(30)
        if len(find_by_text(self.driver,'There are currently no dates available',several=True))==1:
            print('No dates available : {}'.format(datetime.now()))
        else:
            print('Good')
            ## 
            # Notify here
            ##
            while 1:
                continue
        self.driver.quit()


if __name__ == "__main__":
    bot = Bot()
    while 1 : 
        bot.start_browser() 
        bot.process()