from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base


class Filter_Results(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    results = "//span[@class='filterResult__sticker__message']/a"

    # Getters

    def get_filter_results(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.results)))

    # Actions
    def click_filter_results(self):
        self.get_filter_results().click()

    # Methods

    def show_results(self): # нажимаем кнопку "показать" после всех примененных фильтров
        self.click_filter_results()
        print("нажали показать")
        self.get_current_url()
