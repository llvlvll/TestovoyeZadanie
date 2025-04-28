import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart import CartProduct
from pages.filters.FilterResults import Filter_Results
from pages.filters.Filter_Memory import Memory
from pages.PickSmartphones import GetSmart
from pages.SmartphonesGadgets import OpenSmartGadget
from pages.filters.filters_brand import Brands
from pages.katalog import OpenCatalogue
from pages.filters.priceChoose import choose_price
from pages.order import OrderProduct
from pages.filters.result_page_choose_product import Product



def test_smoke_buy_product():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)


    print("Start Test")

    ctl = OpenCatalogue(driver) # открываем меню, и выбираем раздел электроника
    ctl.open_catalogue()
    time.sleep(1)

    sm_gd = OpenSmartGadget(driver) # на странице электроники выбираем смартфоны и гаджеты
    sm_gd.open_smart_gadgets()

    kt_sm = GetSmart(driver) #открывем раздел смартоны
    kt_sm.open_smartphones()

    br = Brands(driver) # фильтр #1 брэнд
    br.open_all_brands()

    p = choose_price(driver) #фильтр #2 цена от и до
    p.move()
    p.set_price()

    memory = Memory(driver) # фильтр #3 выбираем обьем оператвки и встроенной памяти
    memory.move_to_memory() # переход к фильтру памяти
    time.sleep(1)
    memory.click_ram() # выбираем размер встроенной
    time.sleep(1)
    memory.click_op_memory() # выбираем размер оперативной
    time.sleep(1)

    result = Filter_Results(driver) # класс с методом, чтобы показывать результат после выбора фильтров
    result.show_results() # после выбора всех фильтров показываем результат

    pr = Product(driver)
    r = pr.price_cotalogue()
    Name_catol = f'Смартфон {pr.name_cotalogue()}' #сохраняем в переменную - цену из каталога
    print(Name_catol)
    print(r)
    pr.choose() # выбираем продукт

    order_p = OrderProduct(driver)
    order_p.order() # офрмляем, а так же выбираем, что заказ оформим без регестрации

    cr_pr = CartProduct(driver) #сверяем имя продукта
    s = cr_pr.save_price_cart()
    Name_cart = cr_pr.save_name_cart() # сохраняем цену из корзины в перменную
    cr_pr.cart_pr()
    print(Name_cart)
    print(s)

    assert r == s # сравниваем цену из каталога и корзины
    print(f'{r} = {s} Отлично!')
    assert Name_cart == Name_catol # сверяем название из катлога и корзины
    print(f'{Name_cart} = {Name_catol} Отлично!!')





# //b[@class='nowrap'] 57 999
# //span[@class='price js__actualPrice'] 57 999






