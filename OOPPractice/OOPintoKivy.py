import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random


class Player:

    STATS_MAP = {
        "hp": random.randint(1, 255),
        "mp": random.randint(1, 255),
        "attack": random.randint(1, 50),
        "defense": random.randint(1, 50),
        "intell": random.randint(1, 50)
    }

    def __init__(self):
        self.hp = self.STATS_MAP["hp"]
        self.mp = self.STATS_MAP["mp"]
        self.attack = self.STATS_MAP["attack"]
        self.defense = self.STATS_MAP["defense"]
        self.intell = self.STATS_MAP["intell"]


char = Player


class MyGrid(GridLayout, char):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        # Name
        self.inside.add_widget(Label(text="Enter your name:"))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        # Age
        self.inside.add_widget(Label(text="How old are you?"))
        self.age = TextInput(multiline=False)
        self.inside.add_widget(self.age)

        self.add_widget(self.inside)

        # Button
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.inside.add_widget(self.submit)

        # Output
        self.output = TextInput(multiline=True)
        self.output.bind(on_press=self.pressed)
        self.inside.add_widget(self.output)

    def pressed(self, instance):

        # Combines what I was trying to do with lists, dicts, and dict.keys
        labels = [
            f"Name: {self.name.text}\n"
            f"Age: {self.age.text}\n"
            f"Health: {self.hp}\n"
            f"Mana: {self.mp}\n"
            f"Strength: {self.attack}\n"
            f"Toughness: {self.defense}\n"
            f"Intelligence: {self.intell}\n"
        ]

        self.output.text = ''.join(labels)  # Combines everything in the list


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()