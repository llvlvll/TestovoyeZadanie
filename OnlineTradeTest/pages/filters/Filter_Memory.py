
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains


class Memory(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    op_memory = "//label[@id='l0d036641b14805407c159fb503525ef8']"
    ram = "//label[@id='l6f3d9b10f765520c50377823b8c4282f']"
    move_to = "//div[@id='columnBlock__82filter__ID']"


    # Getters

    def move_to_memory(self): # переходим к фильтам по памяти
        actions = ActionChains(self.driver)
        elem = WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.move_to)))
        actions.move_to_element(elem).perform()

    def get_ram(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.ram)))

    def get_op_memory(self):
        return WebDriverWait(self.driver, 30).until(exp.element_to_be_clickable((By.XPATH, self.op_memory)))




    # Actions


    def click_op_memory(self): # выбираем объем оперативную
        self.get_op_memory().click()

    def click_ram(self): # выбираем объем встроенную
        self.get_ram().click()


    # Methods

    def move_to_filt_memory(self):
        self.move_to_memory()

    """Можно выбрать какой фильтр применить или можно сразу оба"""

    def choose_op(self):
        self.click_op_memory()
        print("Выбрали размер оперативную память")


    def choose_ram(self):
        self.click_ram()
        print("Выбрали размер встроенной памяти")


