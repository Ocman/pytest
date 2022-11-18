from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        #  self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()

    def buy_product(self, basket):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys(basket.first_name)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys(basket.last_name)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys(basket.postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()

    def put_product_in_basket(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".header_secondary_container").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"product_sort_container\"]").click()
        self.driver.find_element(By.LINK_TEXT, "2").click()

    def login(self, username, password):
        self.open_page()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_window_size(1616, 868)

    def destroy(self):
        self.driver.quit()