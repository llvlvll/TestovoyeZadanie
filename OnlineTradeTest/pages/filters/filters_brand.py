from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains


class Brands(Base):
    url = "https://www.onlinetrade.ru/"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    view_all = "//div[@class='spoiledLst_cover ']/a" #локатор кнопки "показать все"
    search_brand = "//div[@class='spoiledLst_cover  active']/div/input" #поле ввода имени брэнда
    huawei = "(//span[@class='displayInline'])[20]" #чекбокс ХУАВЕЯ



    # Getters

    def move_to_brand(self): #перемещаемся к фильтру брэндов/производителей
        actions = ActionChains(self.driver)
        elem = WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.view_all)))
        actions.move_to_element(elem).perform()

    def all_brands(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.view_all)))

    def get_brands(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.search_brand)))

    def get_huawei(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.huawei)))


    # Actions
    def click_all_brand(self): # нажимаем показать все
        self.all_brands().click()

    def send_keys_to_form(self, brand): # пишем в поле брэнд который нужен
        self.get_brands().send_keys(brand)

    def click_huawei(self):
        self.get_huawei().click()




    # Methods

    def open_all_brands(self):
        self.get_current_url()
        self.click_all_brand()
        print("Нажали показать все")
        self.send_keys_to_form("Huawei")
        print("Ввели в  поле поиска Хуавей")
        self.click_huawei()
        print("Нажали на на Huawei")

