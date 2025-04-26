

class Base():
    def __init__(self, driver):

        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current Url: " + get_url)

    def page_succses(self, word, result):
        page_succsess = word.text
        assert page_succsess == result
        print("Pass")



