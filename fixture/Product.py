class Product:
    def __init__(self, app):
        self.app = app
        
    def buy(self, basket):
        driver = self.app.driver
        By = self.app.By
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys(basket.first_name)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys(basket.last_name)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys(basket.postal_code)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()

    def put_in_basket(self):
        driver = self.app.driver
        By = self.app.By
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
        driver.find_element(By.CSS_SELECTOR, ".header_secondary_container").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"product_sort_container\"]").click()
        driver.find_element(By.LINK_TEXT, "2").click()