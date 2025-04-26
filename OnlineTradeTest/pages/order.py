from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base


class OrderProduct(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    order_product = "//a[@id='js__popup_addedToCart__cartLinkID']"
    word = "//div[@id='js__addedToCart_itemsID']/div/div[2]/p/text()[1]"
    no_auth = "//a[@title='Продолжить без регистрации']"

    # Getters
    def get_order(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.order_product)))

    def get_no_auth(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.no_auth)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.word)))

    # Actions
    def click_order_pr(self):  #оформляем заказ
        self.get_order().click()

    def click_no_auth(self):  # продолжит без регестрации
        self.get_no_auth().click()


    # Methods

    def order(self):
        self.click_order_pr()
        print("Нажали офрмить заказ")
        self.click_no_auth()
        print("Нажали без регестрации")

