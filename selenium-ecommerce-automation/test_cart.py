from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com")

# Username
username = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"user-name"))
)
username.send_keys("standard_user")

# Password
password = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"password"))
)
password.send_keys("secret_sauce")

# Login Button
login = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"login-button"))
)
login.click()

# Verify Login
WebDriverWait(driver,10).until(
    EC.url_contains("inventory")
)

assert "inventory" in driver.current_url
print("Login Successful")

# Add Backpack to Cart
add_backpack = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))
)
add_backpack.click()

# Verify Cart Badge
cart_badge = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))
)

assert cart_badge.text == "1"
print("Product Added Successfully")

# Open Cart
cart = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))
)
cart.click()

# Verify Product in Cart
product = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"inventory_item_name"))
)

assert product.text == "Sauce Labs Backpack"
print("Correct Product Found")
time.sleep(10)

# Remove Product
remove = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"remove-sauce-labs-backpack"))
)
remove.click()

# Verify Cart is Empty

assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
print("Cart is Empty")
time.sleep(10)

driver.quit()