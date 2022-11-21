class Sessionhelp:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        By = self.app.By
        self.app.open_page()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()

    def logout(self):
        driver = self.app.driver
        By = self.app.By
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        #  self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()