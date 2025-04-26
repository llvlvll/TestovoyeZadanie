from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base

"""Страница с продуктами по выбранным условиям"""
class Product(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locator

    product = "(//div[@class='indexGoods__item__manage'])[2]/a"  # локатор продукта который выбираем, точнее его кнопка купить
    price_in_catalogue = "//span[@class='price js__actualPrice']"
    name_in_cotalogue = "(//div[@class='indexGoods__item__descriptionCover'])[2]/a"
    def buy_product(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.product)))
    def get_price(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.price_in_catalogue)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.name_in_cotalogue)))


    ## Actions

    def click_buy(self):  #нажатие кнопки купить
        self.buy_product().click()

    def price_cotalogue(self):
        price_cat = self.get_price().text
        return price_cat

    def name_cotalogue(self):
        name_cat = self.get_name().text
        return name_cat

    def move_to_buy(self):  #перемещаемся к кнопке купить
        actions = ActionChains(self.driver)
        elem = WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.product)))
        actions.move_to_element(elem).perform()



    # Methods


    def choose(self):  #ну и метод
        self.price_cotalogue()
        self.name_cotalogue()
        self.move_to_buy()
        self.click_buy()
        print("нажали купить")

