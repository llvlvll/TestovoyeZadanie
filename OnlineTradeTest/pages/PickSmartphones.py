from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base


class GetSmart(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    smartphones = "//div[@class='drawCats__items fullWidth']/div/a"
    word = "//div[@id='main_area']/div[4]/div/h1"
    # Getters

    def get_smartphones(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.smartphones)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.word)))

    # Actions
    def click_smartphones(self):   # кликаем на раздел смартфоны

        self.get_smartphones().click()


    # Methods

    def open_smartphones(self):
        self.get_current_url()
        self.click_smartphones()
        print("Открываем раздел смартфоны")
        self.page_succses(self.get_word(), "Смартфоны")
