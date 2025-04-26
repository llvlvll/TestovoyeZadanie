import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains


class choose_price(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    scrollTo = "//div[@title='Операционная система в категории «Смартфоны»']" # тут та же самая беда что и со вторым лакатором
    price = "//div[@title='Подобрать по цене в категории «Смартфоны»']" #кроме как заголовка он никак не хочет работать //div[@class='columnBlock__spoiledContent ']/div
    # но в отличии от локатора на тайтол этот лакатор никак нериагирует
    price1 = "//input[@id='price1']"
    price2 = "//input[@id='price2']"


    # Getters

    def move_to_price(self): # перемещаемся к фильтру цена
        actions = ActionChains(self.driver)
        elem = WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.scrollTo)))
        actions.move_to_element(elem).perform()

    def get_price1(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.price1)))

    def get_price2(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.price2)))
    def get_price(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.price)))


    # Actions

    def click_price(self): # раскрываем фильтр цена,###### так вот тут самое интерсное, сначала я сделал с ползунками, но ползунки очень фигово работали
        # из-за чего, я тильтанул, и просто применил фильтр через ввод в поля, не знаю, что творится с ползунками, но они работают через раз
        self.get_price().click()

    def click_price1(self, price1): # кликаем на поле левое, очищаем и вводим свое значение
        self.get_price1().click()
        self.get_price1().clear()
        self.get_price1().send_keys(price1)

    def click_price2(self, price2):  #кликаем на поле правое, очищаем и вводим свое значение
        self.get_price2().click()
        self.get_price2().clear()
        self.get_price2().send_keys(price2)



    # Methods

    def move(self):
        self.move_to_price()
        print("")

    def set_price(self):
        self.click_price()
        print("раскрыли фильтр цена")
        self.click_price1(15000)
        print("ввели цену ОТ")
        time.sleep(1)
        self.click_price2(100000)
        print("ввели цену ДО")

