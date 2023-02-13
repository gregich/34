from kivy.app import App
from kivy.config import Config
Config.set("graphics", "resizeble", 0)
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file('calc.kv')
Window.size = (360, 800)



class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = "0"

# кнопка delete
    def remove_last(self):
        
        character_field = self.ids.input_box.text
        if len(character_field) > 1:
            character_field = character_field[:-1] #стереть последнюю запись в строке
            self.ids.input_box.text = character_field

        else:
            self.ids.input_box.text = "0"

    def button_value(self, number):
        character_field = self.ids.input_box.text
        if "wrong equation" in character_field:
            character_field = ''
        if character_field == '0':
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{character_field}{number}"

    def sings(self, sing):
        character_field: str = self.ids.input_box.text
        proverka = character_field[len(character_field)-1:]
        if proverka == '+' or proverka == '-' or proverka == '*' or proverka == '/':
            pass
        else:
            if sing != '%':
                self.ids.input_box.text = f"{character_field}{sing}"
            else:
                if ("+" in character_field or "-" in character_field or "*" in character_field or "/" in character_field or "%" in character_field):
                    num_list = re.split("\+|\*|-|/|%", character_field)
                    if len(num_list) == 2:
                        res_old = character_field[:-len(num_list[1])]
                        simvol = res_old[len(res_old)-1:]
                        if simvol == '+' or simvol == '-':
                            try:
                                result = float(num_list[0]) * (float(num_list[1])/100)
                            except:
                                result = str(float(num_list[1])/100)
                        else:
                            result = float(num_list[1])/100
                        self.ids.input_box.text = f"{res_old}{result}"
                    elif len(num_list)>2:
                        string = character_field[:-len(num_list[-1])]
                        simvol = string[len(string)-1:]
                        if simvol == '+' or simvol == '-':
                            result_number = eval(string[:-1])
                            result = float(result_number) * (float(num_list[-1])/100)
                        else:
                            result = float(num_list[-1])/100
                        self.ids.input_box.text = f"{string}{result}"
                else:
                    result = float(character_field)/100
                    self.ids.input_box.text = str(result)
                     

    def dot(self):
        character_field = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", character_field)


        if ("+" in character_field or "-" in character_field or "*" in character_field or "/" in character_field or "%" in character_field) and "." not in num_list[-1]:
            character_field = f"{character_field}."
            self.ids.input_box.text = character_field

        elif '.' in character_field:
            pass

        else:
            character_field = f'{character_field}.'
            self.ids.input_box.text = character_field

    def results(self):
        character_field = self.ids.input_box.text
        try:
            result = eval(character_field)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    def positive_negative(self):
        character_field = self.ids.input_box.text
        if "-" in character_field:
            self.ids.input_box.text = f"{character_field.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{character_field}"


class CalculatorSuperApp(App):
    def build(self):

        self.icon = 'myicon.png'
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorSuperApp().run()