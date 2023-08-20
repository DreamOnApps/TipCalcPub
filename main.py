import sys
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from math import acos


# Screens for Apps______________________________________________________________________________________________________
class WindowManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class TipCalcScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


# Home__________________________________________________________________________________________________________________


class HomeGridLayout(GridLayout):
    pass

# Help__________________________________________________________________________________________________________________

class HelpGridLayout(GridLayout):
    pass

# Tip Calculator________________________________________________________________________________________________________


class TipCalcGridLayout(GridLayout):
    def tip_calc(self, tipcalc):
        if tipcalc:
            try:
                answer = str(tipcalc)
                if "%" in tipcalc:
                    global num1, num2, rounded_answer, my_answer
                    num1, num2 = answer.split("%")
                    num2 = str(num2) + "/100"
                    my_num2 = str(eval(num2))
                    my_answer = str(num1) + "*" + str(my_num2)
                    my_answer = eval(my_answer)
                    rounded_answer = round(my_answer, 2)
                    self.display.text = str(rounded_answer)
            except Exception:
                self.display.text = "Error"

    def plus_bill(self, bill_tip):
        if bill_tip:
            try:
                bill_plus_tip = str(num1) + "+" + str(my_answer)
                bill_plus_tip_answered = (eval(bill_plus_tip))
                bill_plus_tip_answered_rounded = round(bill_plus_tip_answered, 2)
                self.display.text = str(bill_plus_tip_answered_rounded)
            except Exception:
                self.display.text = "Error"

    def tip(self, tip_equals):
        if tip_equals:
            try:
                self.display.text = str(rounded_answer)
            except Exception:
                self.display.text = "Error"

    def bill(self, original_bill):
        if original_bill:
            try:
                self.display.text = str(num1)
            except Exception:
                self.display.text = "Error"


# App Class and Run App_________________________________________________________________________________________________


class CalculatorApp(App):

    def build(self): Builder.load_file


if __name__ == "__main__":
    CalculatorApp().run()