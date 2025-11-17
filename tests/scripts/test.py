# Step one : launch the browser
# Step two : visit the web page
# Step Three : Find the elements by ID, Class, Name, etc. 
# Step Four : Perform the action. 
# Step Five : Verify expected outcomes.
# Step Six : Close the browser.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timezone
import csv
import traceback
import os


# simple logging mechanism

def log(msg, messages):
    ts = datetime.now(timezone.utc).isoformat()
    messages.append(f"[{ts}] {msg}")
    print(msg)

    
# write a small CSV line (create if missing)
def write_result(test_name, messages, status,error_msg, start_ts, duration):
    try:
        
        with open("tests/selenium_test_results.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Heading
            writer.writerow(["Selenium Test Results"])
            # blank line to separate runs
            writer.writerow([])
            # message section
            writer.writerow(["messages"])
            for m in messages:
                writer.writerow([m])
                
            # blank line to separate runs
            writer.writerow([])
            
            # header if file empty or missing
            writer.writerow(["test","timestamp","status","duration","error"])
            writer.writerow([test_name, start_ts, status, f"{duration:.2f}", error_msg])
            
            # blank line to separate runs
            writer.writerow([])
            
    except Exception:
        # fallback: log to console
        log("Failed to write test_results.csv:", traceback.format_exc())

def test_selenium_cleancity_User_Registration():
    # simple result tracking
    test_name = "test_selenium_cleancity_User_Registration"
    start_ts = datetime.now(timezone.utc).isoformat()
    start_time = time.time()
    status = "passed"
    error_msg = ""
    messages = []
    # Step one : launch the browser
    driver = webdriver.Chrome()
    
    # Step Two: visit the web page
    try:
        
        driver.get("http://localhost:3000/")
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Step Three: Find the elements by ID, Class, Name, etc.
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cta-btn:nth-child(1)"))
        )
        
        # Step Four: Perform the action.
        # Click on the "Sign Up" button
        sign_up_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Verify the URl redirects to the register page upon successful registration.
        assert "localhost:3000/register" in driver.current_url, "Url does not contain'localhost:3000/register'"
        log("Navigated to Registration Page, proceed to Register", messages)
        
        # Fill in the registration form
        # Fill in the name with generic name "Admin Tester"
        input_name = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "register-name"))
        )
        input_name.send_keys("Admin Tester")
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Fill in the email with generic email "
        input_email = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"register-email"))
        )
        input_email.send_keys("Admintester@email.com")
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Fill in the password with generic password "Admin1234"
        input_password = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"register-password"))
        )
        input_password.send_keys("Admin1234")
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Click on the "Register" button
        register_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".register-btn"))
        )
        register_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Verify the URl redirects to the profile page upon successful log in.
        assert "localhost:3000/login" in driver.current_url, "Url does not contain'localhost:3000/login'"
        log("Registration Successful, proceed to Login", messages)
        
        # Test Login after Registration
        # Fill in the email with generic email "
        input_login_email = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"login-email"))
        )
        input_login_email.send_keys("Admintester@email.com")
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Fill in the password with generic password "Admin1234"
        input_login_password = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"login-password"))
        )
        input_login_password.send_keys("Admin1234")
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Click on the "Login" button
        login_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".login-btn"))
        )
        login_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Verify the URl redirects to the profile page upon successful log in.
        assert "localhost:3000/profile" in driver.current_url, "Url does not contain'localhost:3000/profile'"
        log("Login Successful, navigated to Profile Page", messages)
        
        # Logout after Login
        logout_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".nav-logout"))
        )
        logout_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Step Five: Verify expected outcomes.
        # Verify the URl redirects to the profile page upon successful log in.
        assert "localhost:3000/" in driver.current_url, "Url does not contain'localhost:3000/'"
        log("Logout Successful, navigated to Home Page", messages)
        # input("Press Enter to close the browser...")
        
    finally:
        # Step Six: Close the browser.
        try:
            driver.quit()
        except Exception:
            pass
        # finalize with the log function to save result of this test. (disabled after test execution)
        # determine duration and write result
        duration = time.time() - start_time
        write_result(test_name, messages, status, error_msg, start_ts, duration)
        messages.clear()
        
        
# Run the test(disable after test execution)
# test_selenium_cleancity_User_Registration()

# AUTH-TC-003	2025-11-05	Password Validation	Weak 2-character password accepted.	
# 1. Go to Register page.
# 2. Fill in all fields.
# 3. Use password "a1".	Name:"Test"
# Email:test@test.com
# Password:"a1"	System accepts weak password (Expected Failure).	
# Account registered successfully with weak password "a1".	
# Fail

# Steps to Reproduce:
# 1. Open browser and navigate to http://localhost:3000/
def test_weak_password_registration():
    # simple result tracking
    test_name = "test_weak_password_registration"
    start_ts = datetime.now(timezone.utc).isoformat()
    start_time = time.time()
    status = "passed"
    error_msg = ""
    messages = []
    
    log("Starting Test Case AUTH-TC-003: Password Validation", messages)
    
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:3000/")
        time.sleep(4)  # Wait for 4 seconds to observe the action
        
        # 2. Click on "Sign Up" button to go to the registration page.
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cta-btn:nth-child(1)"))
        )
        sign_up_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Verify the URl redirects to the register page upon successful registration.
        assert "localhost:3000/register" in driver.current_url, "Url does not contain'localhost:3000/register'"
        log("Navigated to Registration Page, proceed to Register", messages)
        
        # 3. Fill in the registration form with the following details:
            #    - Name: "Test"
            #    - Email: " test@test.com "
            #    - Password: "a1"
        input_name = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "register-name"))
        )
        input_name.send_keys("Test")
        time.sleep(1)  # Wait for 1 second to observe the action
        input_email = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"register-email"))
        )
        input_email.send_keys("test@test.com")
        time.sleep(1)  # Wait for 1 second to observe the action
        input_password = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"register-password"))
        )
        input_password.send_keys("a1")
        time.sleep(1)  # Wait for 1 second to observe the action   
        
        # 4. Click on the "Register" button.
        register_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".register-btn"))
        )
        register_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        log("Attempted Registration with weak password 'a1'", messages)
        
        # 5. Observe the system's response to the weak password. 
        # Verify the URl redirects to the profile page upon successful log in.
        assert "localhost:3000/login" in driver.current_url, "Url does not contain'localhost:3000/login'"
        log("Registration Successful with weak password, proceed to Login", messages)
        
        
        # # Check for error message indicating weak password
        # error_message = WebDriverWait(driver, 2).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message"))
        # )
        # assert "Password is too weak" in error_message.text, "Weak password error message not displayed"
        # log("Weak password correctly rejected by the system.")
    finally:
        # Step Six: Close the browser.
        try:
            driver.quit()
        except Exception:
            pass
        # finalize with the log function to save result of this test. (disabled after test execution)
        # determine duration and write result
        duration = time.time() - start_time
        write_result(test_name, messages, status, error_msg, start_ts, duration)
        messages.clear()

# test_weak_password_registration()

# Expected Result:
# The system should reject the weak password and display an error message indicating that the password does not
# meet the minimum security requirements.
# Actual Result:
# The system accepted the weak password "a1" and registered the account successfully.
# Status: Failed
# Notes:
# This is a security concern as it allows users to create accounts with easily guessable passwords,
# potentially compromising account security. The password policy should be enforced to require stronger passwords.


# AUTH-TC-001	2025-11-05	User Login/Registration	
# (Security) Verify passwords are stored in plain text.	
# 1. Log in with user@cleancity.com.
# 2. Open DevTools → Application → Local Storage.
# 3. Inspect cleancity_users.	Login: user@cleancity.com
# Pass: password123	Password should appear in plain text (Expected Failure).	
# Password was visible in plain text inside cleancity_users.	
# Fail

# Steps to Reproduce:
# 1. Open browser and navigate to http://localhost:3000/
def test_password_storage_plain_text():
    # simple result tracking
    test_name = "test_password_storage_plain_text"
    start_ts = datetime.now(timezone.utc).isoformat()
    start_time = time.time()
    status = "passed"
    error_msg = ""
    messages = []
    
    log("Starting Test Case AUTH-TC-001: User Login/Registration - Password Storage", messages)
    
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:3000/")
        time.sleep(4)  # Wait for 4 seconds to observe the action
        
        # 1. Click on "Login" button on navbar to go to the login page.
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar-links > a:nth-child(8)"))
        )
        login_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Verify the URl redirects to the login page.
        assert "localhost:3000/login" in driver.current_url, "Url does not contain'localhost:3000/login'"
        log("Navigated to Login Page, proceed to Login", messages)
        
        # 2. Fill in the login form with the following details:
            #    - Email: "user@cleancity.com"
            #    - Password: "password123"
        input_email = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"login-email"))
        )
        input_email.send_keys("user@cleancity.com")
        time.sleep(1)  # Wait for 1 second to observe the action
        input_password = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID,"login-password"))
        )
        input_password.send_keys("password123")
        time.sleep(1)  # Wait for 1 second to observe the action
        log("Filled in login credentials for standard user", messages)
        # 3. Click on the "Login" button.
        submit_login_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".login-btn"))
        )
        submit_login_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        log("Attempted Login with standard user credentials", messages)
        
        # 4. Open DevTools → Application → Local Storage.
        time.sleep(20)  # Wait for 20 seconds to allow manual inspection
        log("Manual Step Required: Open DevTools -> Right click on the browser page and click inspect.", messages)
        
        # 5. Inspect cleancity_users.
        log("Note: Selenium does not support interacting with browser DevTools directly.")
        time.sleep(10)  # Wait for 10 seconds to allow manual inspection
        log("Manual Step Required: Click on the additional items icon → Application → Local Storage dropdown and inspect cleancity_users.", messages)
        input("Press Enter to close the browser...")
        
    finally:
        # Close the browser.
        try:
            driver.quit()
        except Exception:
            pass
        # finalize with the log function to save result of this test. (disabled after test execution)
        # determine duration and write result
        duration = time.time() - start_time
        write_result(test_name, messages, status, error_msg, start_ts, duration)
        messages.clear()
        
test_password_storage_plain_text()
        

# AUTH-TC-005	2025-11-06	User Registration	User enumeration via error messages.	
# 1. Register with known email.
# 2. Note error.
# 3. Register with non-existent email.
# 4. Compare errors.	Known: admin@cleancity.com
# Unknown: random@never.com	Known email returns different error (Expected Failure).	Error shown for admin email; none shown for random email.	Fail
