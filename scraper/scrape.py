from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from pymongo import MongoClient
import json
from pprint import pprint
__author__ = 'William'

def main():
    global b
    b = webdriver.PhantomJS()
    b.delete_all_cookies()
    b.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
    print("phase 1")
    accept = b.find_element_by_name("disclaimerFM")
    accept.submit()
    b.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
    json_data = json.load(open('prisonlist.json'))
    pprint(json_data)
    for prison in json_data:
        listPrison(prison)
    
    
def listPrison(location):
    global b
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
        print(gcdid.get_attribute('value'))
    #print(b.page_source)


b = 0
client = MongoClient()
main()
