# Proof of Concept Version

# Run the script and it'll print out an email for you to log in with in the Starbucks app


# Imports
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json


# Variables
PASSWORD = "Freestarbucks!1"
FIRST_NAME = "Alex"
LAST_NAME = "Melons"
ZIPCODE = "02115"
url = "https://www.starbucks.com/account/create"

# Main function; give it a birthday and it'll run its course
def create_account(birthday):
  
  # Create email address
  emailAddress = "alexalex" + birthday + "@yahoo.com"
  
  # Use Selenium/PhantomJS to retrieve the form
  print("Starting up PhantomJS")
  driver = webdriver.PhantomJS()
  driver.set_window_size(1120, 550)
    
  print("Storing the page location")
  driver.get(url)
  #print(account_page.url + "\n")    
    
  firstName = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "firstName"))
      )
    
  #account_form = driver.find_element_by_xpath("//form[1]")

#  print("Selecting the form element for the domain page")
#  account_form = driver.find_element_by_id("form")[0]
    
  
  # Filling out the form    
  print("Setting the first name value to " + FIRST_NAME)
  driver.find_element_by_xpath("//*[@id='firstName']").send_keys(FIRST_NAME)
  
  print("Setting the last name value to " + LAST_NAME)
  driver.find_element_by_xpath("//*[@id='lastName']").send_keys(LAST_NAME)
    
  print("Setting the zipcode value to " + ZIPCODE)
  driver.find_element_by_xpath("//*[@id='postalCode']").send_keys(ZIPCODE)
    
  print("Setting the email address value to " + emailAddress)
  driver.find_element_by_xpath("//*[@id='emailAddress']").send_keys(emailAddress)
    
  print("Setting the password value to " + PASSWORD)
  driver.find_element_by_xpath("//*[@id='password']").send_keys(PASSWORD)
  driver.save_screenshot('out.png')

  print("Selecting the digital rewards card")
  driver.find_element_by_xpath("//*[@id='cardRewards']/label[1]/input").click()
    
  print("Setting the birthday value to " + birthday)
  driver.find_element_by_css_selector('#birthMonth .select__selected_text')[0]['value'] = 'May'
  driver.find_element_by_css_selector('#birthDay .select__selected_text')[0]['value'] = '19'
    
  print("Selecting the Terms and Conditions")
  tocRadio = driver.find_element_by_id('termsAndConditions')
  tocRadio.click()

  # Submitting the form
  print("Submitting the form")
  try:
    submitButton = driver.find_element_by_class_name('sb-button')
    submitButton.click()
  except Exception:
    print('Errored out somewhere:')
    print Exception
    
        
# UX Print Statements (prompts user for API key, initiates the file_delete function)
print("<-------------------------------------------------------->")
print("Ready for some free food? \n Enter the desired birthday here: \n")
birthday = raw_input("Date: ")
create_account(birthday)