from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup():
    driver = webdriver.Chrome()
    driver.get("https://techbrain.ai/")
    return driver

def teardown(driver):
    driver.quit()


def forget_password():
    driver = setup()
    wait = WebDriverWait(driver,5)
    
    signInLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//span[contains(text(),"Sign in")])[1]')))
    signInLink.click()
    
    forgotPwdLink = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Forgot")]')))
    forgotPwdLink.click()
    
    # required because emailfield is same for both signup and forget password and the emailfield for signup gets filled 
    # instead of getting filled in the forgot password's email field
    time.sleep(5)
    
    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")
    
    submitBtn = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
    submitBtn.click()

    driver.get("https://app.endtest.io/mailbox?email=techbraintest4@endtest-mail.io")
    # waiting 5 seconds so that the reset mail is received then the page is refreshed to see the received mail
    time.sleep(5)
    driver.refresh()
    
    wait.until(EC.element_to_be_clickable((By.XPATH,'(//div[contains(text(),"Password reset")])[1]'))).click()
    mail = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a)[1]"))).click()

    newPwdField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_password"]')))
    newPwdField.send_keys("Nepal@123")

    newConfirmPwdField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_password_confirmation"]')))
    newConfirmPwdField.send_keys("Nepal@123")

    updatePwdBtn = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]'))).click()

    time.sleep(5)
    
    teardown(driver)
    
forget_password()

def login_with_invalid_password():
    driver = setup()
    wait = WebDriverWait(driver,5)
    expectedResult = "Invalid Email or password."
    
    signInLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//span[contains(text(),"Sign in")])[1]')))
    signInLink.click()

    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('K@thmandu123')

    submitBtn = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
    submitBtn.click()

    result = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@role="alert"]//div[contains(text(),"Invalid")]')))
    actualResult = result.text

    try:
        assert actualResult == expectedResult ,"Test Failed"
        print("Test Passed: Expected Result with the invalid password in login")

    except AssertionError as e:
        print(e)
    
    teardown(driver)

login_with_invalid_password()

def succesful_signIn_with_valid_email_password():
    driver = setup()
    wait = WebDriverWait(driver,5)
    expectedResult = "Signed in successfully."
    
    signInLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//span[contains(text(),"Sign in")])[1]')))
    signInLink.click()

    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('Nepal@123')

    submitBtn = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
    submitBtn.click()

    result = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@role="alert"]//div[contains(text(),"Signed in successfully.")]')))
    actualResult = result.text
    try:
        assert actualResult == expectedResult ,"Test Failed"
        print("Test Passed: Expected Result with valid email and password")

    except AssertionError as e:
        print(e)
    
    teardown(driver)
    
succesful_signIn_with_valid_email_password()

def signUp_with_registered_email():
    driver = setup()
    wait = WebDriverWait(driver,5)
    expectedResult = "Email has already been taken"
    signInLink = driver.find_element(By.XPATH,'(//span[contains(text(),"Sign in")])[1]')
    signInLink.click()
    
    singUpLink = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Sign up")]'))).click()

    time.sleep(5)
    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('K@thmandu123')

    confirmPasswordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password_confirmation"]')))
    confirmPasswordField.send_keys('K@thmandu123')

    submitBtn = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()
    
    result = wait.until(EC.presence_of_element_located((By.XPATH,'//p[contains(text(),"Email has already been taken")]')))
    actualResult = result.text
    try:
        assert actualResult == expectedResult ,"Test Failed"
        print("Test Passed: Expected Result - Email has already been taken")

    except AssertionError as e:
        print(e)
    
    teardown(driver)
    
signUp_with_registered_email()

def password_validation_in_signUp():
    driver = setup()
    wait = WebDriverWait(driver,5)
    expectedResult = "Password must be atleast 8 alphanumeric characters with mixed case"
    signInLink = driver.find_element(By.XPATH,'(//span[contains(text(),"Sign in")])[1]')
    signInLink.click()
    
    singUpLink = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Sign up")]'))).click()

    time.sleep(5)
    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('abcd1234')

    confirmPasswordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password_confirmation"]')))
    confirmPasswordField.send_keys('abcd1234')

    submitBtn = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()
    
    result = wait.until(EC.presence_of_element_located((By.XPATH,'//p[contains(text(),"Password must be atleast 8 alphanumeric characters with mixed case")]')))
    actualResult = result.text
    try:
        assert actualResult == expectedResult ,"Test Failed"
        print("Test Passed: Expected Result - Password with atleast 8 alphanumric characters with mixed case")
        time.sleep(5)
    except AssertionError as e:
        print(e)
    
    teardown(driver)

password_validation_in_signUp()

def password_confimation_match_test_in_signUp():
    driver = setup()
    wait = WebDriverWait(driver,5)
    expectedResult = "Password confirmation doesn't match Password"
    signInLink = driver.find_element(By.XPATH,'(//span[contains(text(),"Sign in")])[1]')
    signInLink.click()
    
    singUpLink = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Sign up")]'))).click()

    time.sleep(5)
    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('Abcd1234')

    confirmPasswordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password_confirmation"]')))
    confirmPasswordField.send_keys('Abcd12345')

    submitBtn = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()
    
    result = wait.until(EC.presence_of_element_located((By.XPATH,'//p[contains(text(),"Password confirmation")]')))
    actualResult = result.text
    try:
        assert actualResult == expectedResult ,"Test Failed"
        print("Test Passed: Expected Result - Password confirmation doesn't match Password")
        time.sleep(5)
    except AssertionError as e:
        print(e)
    
    teardown(driver)
    
password_confimation_match_test_in_signUp()

def progress_bar_for_loggedIn_user():
    driver = setup()
    wait = WebDriverWait(driver,5)
    
    signInLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//span[contains(text(),"Sign in")])[1]')))
    signInLink.click()

    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('Nepal@123')

    submitBtn = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
    submitBtn.click()

    progressBar = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="block"]')))
    for progress in progressBar:
        print(progress.text)

    print("Progress Bar is being displayed for the logged in user.")
    
    teardown(driver)
    
progress_bar_for_loggedIn_user()