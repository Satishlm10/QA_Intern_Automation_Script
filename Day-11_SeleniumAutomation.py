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

def complete_course():
  driver=setup()
  start=driver.find_element(By.XPATH, "(//a/span[text()='Start'])[1]")
  start.click()
  time.sleep(3)
  try:
    lesson_list=driver.find_element(By.XPATH, '//a[@data-modal-target="lessonListModal" or data-modal-toggle="lessonListModal"]')
    lesson_list.click()
    time.sleep(1)
    close=driver.find_element(By.XPATH, "//span[text()='Close']")
    close.click()
    time.sleep(2)
    page=1
    while (page<29):
      if (page==28):
        break
      else:
        try:
          nextLesson=driver.find_element(By.XPATH, "//button[@type='submit']")
          if nextLesson:
           nextLesson.click()
        except Exception:
          # nextLesson=driver.find_element(By.XPATH, "//button[@type='submit']")
          goquiz=driver.find_element(By.XPATH,"//span[text()='Go to Quiz']")
          if goquiz:
            goquiz.click()
            time.sleep(2)
            checkboxs=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            for checkbox in checkboxs:
              checkbox.click()
        time.sleep(2)
      page +=1
  except Exception as e:
    print(e)
  finally:
    time.sleep(3)
    teardown(driver) 
complete_course()

def edit_profile():
    driver = setup()
    wait = WebDriverWait(driver,5)
    
    loginLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//span[contains(text(),"Sign in")])[1]')))
    loginLink.click()

    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    emailField.send_keys("joyboythevoidcentury100@gmail.com")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_password"]')))
    passwordField.send_keys("S.mhrjn@lm10")

    loginBtn = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()

    profileLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//span[contains(text(),"Profile")])[1]'))).click()
    
    editProfileLink = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Edit Profile")]'))).click()

    firstNameField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_first_name"]')))
    firstNameField.clear()
    firstNameField.send_keys('John')

    lastNameField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_last_name"]')))
    lastNameField.clear()
    lastNameField.send_keys('Doe')

    phoneField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_phone"]')))
    phoneField.clear()
    phoneField.send_keys('9812345678')

    addressField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_street_address"]')))
    addressField.clear()
    addressField.send_keys('kumaripati')

    postalField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_postalcode"]')))
    postalField.clear()
    postalField.send_keys("44600")

    cityField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_city"]')))
    cityField.clear()
    cityField.send_keys('Lalitpur')

    countrySelect = wait.until(EC.presence_of_element_located((By.XPATH,'//select[@id="user_country"]')))
    dropdown = Select(countrySelect)
    dropdown.select_by_index(2)

    uploadAvatar = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_avatar"]')))
    uploadAvatar.send_keys("C:\\Users\\nerus\\Downloads\\avatar.png")

    updateLink = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()
    time.sleep(5)
    
    teardown(driver)    
edit_profile()

def course_popUp():
    driver = setup()
    wait = WebDriverWait(driver,5)
    listsLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//a//span[contains(text(),"Lists")])[1]'))).click()
    numberOfLessons = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'//h3//a'))))
    firstLesson = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Goals of the Intro Course")]'))).click()

    for i in range(numberOfLessons):
        try:
            lessonPopUp = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-modal-toggle="lessonListModal"]')))
            lessonPopUp.click()
        except:
            lessonPopUp = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-modal-toggle="lessonListModal"]')))
            lessonPopUp.click()
            
        lessonsList = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//h3//a')))
        lessonsList[i].click()
    time.sleep(5)  
    teardown(driver)    
course_popUp()

def signUp_Automation():
    driver = setup()
    wait = WebDriverWait(driver,5)
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

    driver.get("https://app.endtest.io/mailbox?email=techbraintest4@endtest-mail.io")
    time.sleep(5)
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="email_list"]'))).click()
    mail = wait.until(EC.presence_of_element_located((By.XPATH, "(//a)[1]"))).click()
    
    driver.get("https://techbrain.ai/")
    signInLink = driver.find_element(By.XPATH,'(//span[contains(text(),"Sign in")])[1]')
    signInLink.click()
    
    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_password"]')))
    passwordField.send_keys('K@thmandu123')

    loginBtn = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()

    time.sleep(5)
    
    
    
    teardown(driver)    
signUp_Automation()    

def signIn_SignOut():
    driver = setup()
    wait = WebDriverWait(driver,5)
    
    signInLink = driver.find_element(By.XPATH,'(//span[contains(text(),"Sign in")])[1]')
    signInLink.click()
    
    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_email"]')))
    emailField.send_keys("techbraintest4@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('K@thmandu123')

    loginBtn = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()

    time.sleep(2)

    signOut = wait.until(EC.presence_of_element_located((By.XPATH,'(//span[contains(text(),"Sign out")])[1]'))).click()
    alert = driver.switch_to.alert 
    alert.accept()
    time.sleep(2)
    
    teardown(driver)    
signIn_SignOut()

def continue_already_started_course(): #checking continue link works or not for a registered user 
    driver = setup()
    wait = WebDriverWait(driver,5)
    
    signInLink = driver.find_element(By.XPATH,'(//span[contains(text(),"Sign in")])[1]')
    signInLink.click()
    
    emailField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_email"]')))
    emailField.send_keys("techbraintest5@endtest-mail.io")

    passwordField = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="form-inputs"]//input[@id="user_password"]')))
    passwordField.send_keys('K@thmandu123')

    loginBtn = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@type="submit"]'))).click()

    #Starting a course which is not started by a user
    startCourse = wait.until(EC.presence_of_element_located((By.XPATH,'(//a//span[contains(text(),"Start")])[1]'))).click()
    nextLesson = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@type="submit"]'))).click()
    homeLink = wait.until(EC.presence_of_element_located((By.XPATH,'//a//img[@alt="Techbrain"]'))).click()
    continueCourse = wait.until(EC.presence_of_element_located((By.XPATH,'(//a/span[contains(text(),"Continue")])[1]'))).click()

    time.sleep(3)
    
    teardown(driver)
continue_already_started_course()