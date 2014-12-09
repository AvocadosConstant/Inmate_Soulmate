from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from pymongo import MongoClient
import json
from pprint import pprint
from multiprocessing import Pool
__author__ = 'William'

def main():
    global b
    json_data = json.load(open('prisonlist.json'))
    pprint(json_data)
    for prison in json_data:
        print("Starting pull of " + prison + "!")
        listPrison(prison)

    
def listPrison(location):
    global b
    global pool
    b.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
    radioBtn = b.find_element_by_id("byOther")
    locField = Select(b.find_element_by_id("vCurrentInstitution"))
    #maxField = Select(b.find_element_by_id("RecordsPerPage"))
    form = b.find_element_by_id("OffenderQueryForm")
    ActionChains(b).click(radioBtn).perform()
    locField.select_by_value(location)
    #maxField.select_by_value("150")
    #b.execute_script("document.getElementById('RecordsPerPage').value = '150'")
    form.submit()
    ids = b.find_elements_by_name("vRecNo")
    for gcdid in ids:
        pullPrisoner(gcdid.get_attribute('value'))
    #print(b.page_source)

def pullPrisoner(prisonerID):
    global b2
    print(prisonerID)
    b2.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
    form = b2.find_element_by_id("OffenderQueryForm")
    identifier = Select(b2.find_element_by_id("vUnoCaseNoRadioButton"))
    identifier.select_by_value("UNO_NO")
    textBox = b2.find_element_by_id("vOffenderId")
    textBox.send_keys(prisonerID)
    form = b2.find_element_by_id("OffenderQueryForm")
    form.submit()

def initializeBrowsers():
    global b
    global b2
    bs = []
    bs.append(b)
    bs.append(b2)
    for br in bs:
        br.delete_all_cookies()
        br.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
        accept = br.find_element_by_name("disclaimerFM")
        accept.submit()
        br.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
        print("Fired up a browser!")
    b = bs[0]
    b2 = bs[1]

pool = Pool(processes=1)
b = webdriver.PhantomJS()
b2 = webdriver.PhantomJS()
initializeBrowsers()
client = MongoClient()
main()
