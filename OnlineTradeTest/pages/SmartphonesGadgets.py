from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base


class OpenSmartGadget(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    smartphones_gadgets = "//div[@class='drawCats__item ']/a"
    word = "//div[@id='main_area']/div[4]/div/h1"
    # Getters

    def get_smart_gadgets(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.smartphones_gadgets)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.word)))
    # Actions
    def click_smart_gadgets(self):
        self.get_smart_gadgets().click()


    # Methods

    def open_smart_gadgets(self):
        self.get_current_url()
        self.click_smart_gadgets()
        self.page_succses(self.get_word(), "Телефоны и гаджеты")



