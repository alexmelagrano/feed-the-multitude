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
password = "Freestarbucks!1"
firstName = "Alex"
lastName = "Melons"
zipcode = "02115"
url = "https://www.starbucks.com/account/create"

# Main function; give it a birthday and it'll run its course
def create_account(birthday):
  
  # Create email address
  emailAddress = "alexalex" + birthday + "@yahoo.com"
  
  # Use Selenium/PhantomJS to retrieve the form
  print("Starting up PhantomJS")
  driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
  driver.set_window_size(1120, 550)
    
  print("Storing the page location")
  driver.get(url)
  print(account_page.url + "\n")    
    
  firstName = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "firstName"))
      )
    
  account_form = driver.find_element_by_xpath("//form[1]")

  print("Selecting the form element for the domain page")
  account_form = driver.find_element_by_id("form")[0]
    
  # Filling out the form    
  print("Setting the first name value to " + firstName)
  account_form.find_element_by_id("#firstName")[0]['value'] = firstName
    
  print("Setting the last name value to " + lastName)
  account_form.find_element_by_id("#lastName")[0]['value'] = lastName
    
  print("Setting the zipcode value to " + zipcode)
  account_form.find_element_by_id("#postalCode")[0]['value'] = zipcode
    
  print("Setting the email address value to " + emailAddress)
  account_form.find_element_by_id("#emailAddress")[0]['value'] = emailAddress
    
  print("Setting the password value to " + password)
  account_form.find_element_by_id("#password")[0]['value'] = password
    
  print("Selecting the digital rewards card")
  account_form.find_element_by_xpath("//*[@id='cardRewards']/label[1]/input").click()
    
  print("Setting the birthday value to " + birthday)
  account_form.find_element_by_css_selector('#birthMonth .select__selected_text')[0]['value'] = 'May'
  account_form.find_element_by_css_selector('#birthDay .select__selected_text')[0]['value'] = '19'
    
  print("Selecting the Terms and Conditions")
  account_form.find_element_by_id('termsAndConditions').click()

  # Submitting the form
  print("Submitting the form")
  try:
    account_form.find_element_by_class_name('sb-button')[0].click()
  except Exception:
    print('Errored out somewhere:')
    print Exception
    
        
# UX Print Statements (prompts user for API key, initiates the file_delete function)
print("<-------------------------------------------------------->")
print("Ready for some free food? \n Enter the desired birthday here: \n")
birthday = raw_input("Date: ")
create_account(birthday)