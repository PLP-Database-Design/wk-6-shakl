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


def test_selenium_cleancity_User_Registration():
    # Step one : launch the browser
    driver = webdriver.Chrome()
    messages = []
    def log(msg):
        ts = datetime.now(timezone.utc).isoformat()
        messages.append(f"[{ts}] {msg}")
        print(msg)
        
     # simple result tracking
    test_name = "test_selenium_cleancity_User_Registration"
    start_ts = datetime.now(timezone.utc).isoformat()
    start_time = time.time()
    status = "passed"
    error_msg = ""
    
    # Step Two: visit the web page
    try:
        
        driver.get("http://localhost:3000/")
        
        # driver.script.add_console_message_handler(log_entries.append)
        
        # Step Three: Find the elements by ID, Class, Name, etc.
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cta-btn:nth-child(1)"))
        )
        
        # Step Four: Perform the action.
        # Click on the "Sign Up" button
        sign_up_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Verify the URl redirects to the profile page upon successful log in.
        assert "localhost:3000/register" in driver.current_url, "Url does not contain'localhost:3000/register'"
        log("Navigated to Registration Page, proceed to Register")
        
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
        log("Registration Successful, proceed to Login")
        
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
        log("Login Successful, navigated to Profile Page")
        
        # Logout after Login
        logout_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".nav-logout"))
        )
        logout_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Step Five: Verify expected outcomes.
        # Verify the URl redirects to the profile page upon successful log in.
        assert "localhost:3000/" in driver.current_url, "Url does not contain'localhost:3000/'"
        log("Logout Successful, navigated to Home Page")
        input("Press Enter to close the browser...")
        
    finally:
        # Step Six: Close the browser.
        try:
            driver.quit()
        except Exception:
            pass
        
        # determine duration and write result
        duration = time.time() - start_time
        # write a small CSV line (create if missing)
        try:
            output_path = "tests/selenium_test_results.csv"
            with open("tests/selenium_test_results.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                # header if file empty or missing
                writer.writerow(["test","timestamp","status","duration","error", "messages"])
                writer.writerow([test_name, start_ts, status, f"{duration:.2f}", error_msg, " | ".join(messages)])
                # blank line to separate runs
                writer.writerow([])
                # message section
                writer.writerow(["messages"])
                for m in messages:
                    writer.writerow([m])
        except Exception:
            # fallback: log to console
            log("Failed to write test_results.csv:", traceback.format_exc())
        
    
test_selenium_cleancity_User_Registration()
