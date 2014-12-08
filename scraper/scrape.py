from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from pymongo import MongoClient
import json
__author__ = 'William'

def main():
    global b
    b = webdriver.PhantomJS()
    b.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
    accept = b.find_element_by_name("disclaimerFM")
    accept.submit()
    b.get("http://www.dcor.state.ga.us/GDC/OffenderQuery/jsp/OffQryForm.jsp")
    listPrison("ALBANY TC")
    
    
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
    print(b.page_source)


b = 0
client = MongoClient()
main()
