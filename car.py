class Car:
    def sound(self):
        print("beep")

    def long_sound(self):
        print('beep-beep')














class Button:
    _click_count = 0

    def click(self):
        self._click_count += 1

    def click_count(self):
        return self._click_count

    def reset(self):
        self._click_count = 0


b1 = Button()
b2 = Button()

b1.click()
b1.click()
b1.click()
b2.click()
b2.click()
b2.click()
print(b1.click_count(), b2.click_count())











