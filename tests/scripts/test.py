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

def test_selenium_cleancity_app():
    # Step one : launch the browser
    driver = webdriver.Chrome()
    
    # Step Two: visit the web page
    try:
        
        driver.get("http://localhost:3000/")
        
        # Step Three: Find the elements by ID, Class, Name, etc.
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cta-btn:nth-child(1)"))
        )
        
        # Step Four: Perform the action.
        sign_up_button.click()
        time.sleep(2)  # Wait for 2 seconds to observe the action
        
        # Step Five: Verify expected outcomes.
        assert "localhost:3000/register" in driver.current_url, "Url does not contain'localhost:3000/register'"
        input("Press Enter to close the browser...")
        
    finally:
        # Step Six: Close the browser.
        driver.quit()
        
    
test_selenium_cleancity_app()
