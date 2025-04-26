from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base


class CartProduct(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator

    word = "//td[@class='multicart__item__description']/div[2]/a"
    price_cart = "//b[@class='nowrap']"
    name_product= "//td[@class='multicart__item__description']/div[2]/a"


    # Getters

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.word)))

    def get_price_cart(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.price_cart)))

    def get_name_cart(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.name_product)))

    # Actions

    def save_price_cart(self):
        price_car = self.get_price_cart().text
        return price_car

    def save_name_cart(self):
        name_cart = self.get_name_cart().text
        return name_cart

    # Methods

    def cart_pr(self):
        self.page_succses(self.get_word(), "Смартфон Huawei Pura 70 12/256GB Белый")
        print("название совпадает")
        self.save_price_cart()
        self.save_name_cart()