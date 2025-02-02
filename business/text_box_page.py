from selenium.webdriver.common.by import By


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_full_name(self, full_name):
        self.driver.find_element(By.ID, "userName").send_keys(full_name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

    def enter_current_address(self, current_address):
        self.driver.find_element(By.ID, "currentAddress").send_keys(current_address)

    def enter_permanent_address(self, permanent_address):
        self.driver.find_element(By.ID, "permanentAddress").send_keys(permanent_address)

    def click_submit(self):
        self.driver.find_element(By.ID, "submit").click()

    def get_output(self):
        name_output = self.driver.find_element(By.ID, "name").text
        email_output = self.driver.find_element(By.ID, "email").text
        current_address_output = self.driver.find_element(By.XPATH, "//p[@id='output']/div[@id='currentAddress']").text
        permanent_address_output = self.driver.find_element(By.XPATH, "//p[@id='output']/div[@id='permanentAddress']").text
        return name_output, email_output, current_address_output, permanent_address_output