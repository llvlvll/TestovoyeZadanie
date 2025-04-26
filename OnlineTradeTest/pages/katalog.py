from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base

class OpenCatalogue(Base):

    url = "https://www.onlinetrade.ru/"

    def __init__(self, driver):
        
        super().__init__(driver)
        self.driver = driver


    #locator

    catalogue = "//div[@class='header__catalogActionsButtons']/a"
    electronics = "//li[@class='mCM__item']/a"
    word = "//div[@id='main_area']/div[4]/div/h1"
    cookie = "//a[@title='Принять']"


    #Getters

    def get_catalogue(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.catalogue)))

    def get_electronics(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.electronics)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.word)))

    def get_cookie(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.cookie)))


    #Actions
    def click_catalogue(self):  # открываем меню коталога
        self.get_catalogue().click()

    def click_electronics(self):  # тыкаем раздел электроника
        self.get_electronics().click()

    def click_cookies(self):  # ну и принять куки, надо, а то элементы, которые перекрывает плашка куки не кликабельны
        self.get_cookie().click()



    #Methods

    def open_catalogue(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_cookies()
        print("приняли куки")
        self.click_catalogue()
        print("открыли меню каталога")
        self.click_electronics()
        print("выбрали раздел электроника")
        self.page_succses(self.get_word(), "Электроника")
