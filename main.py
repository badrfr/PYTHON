from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


# Specify the path to the GeckoDriver executable
gecko_driver_path = 'C:/Users/mouazen/Desktop/tmp/geckodriver.exe'

# Create a Firefox webdriver instance
driver = webdriver.Firefox()

# URL of the login page
login_url = 'https://www.neoprofs.org/login'
driver.get(login_url)

# Find the username and password input fields by their name, ID, class, or other locators
username_field = driver.find_element('username')  # Replace with the actual name of the username field
password_field = driver.find_element('password')  # Replace with the actual name of the password field

# Replace 'your_username' and 'your_password' with your actual login credentials
username = 'leroy'
password = 'Ne_pass123'

# Enter the username and password
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the form (you may need to locate the login button and click it)
password_field.send_keys(Keys.RETURN)

# Wait for a few seconds to let the login process complete (you can use WebDriverWait for better synchronization)
driver.implicitly_wait(5)

# Perform additional actions after login if needed

# Close the browser window when done
driver.quit()
