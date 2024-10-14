
import tkinter as tk  #
import random

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кубик")

        self.sides = []
        #self.label#
        self.label = tk.Label(root, text="Введите название для грани кубика:")
        self.label.pack()

        self.entry = tk.Entry(root) #dsdss
        self.entry.pack()

        self.add_button = tk.Button(root, text="Добавить грань", command=self.add_side)
        self.add_button.pack()

        self.sides_label = tk.Label(root, text="Грани кубика: ")
        self.sides_label.pack()

        self.roll_button = tk.Button(root, text="Бросить кубик", command=self.roll_dice)
        self.roll_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def add_side(self):
        side_name = self.entry.get()
        if side_name:
            self.sides.append(side_name)
            self.update_sides_label()
            self.entry.delete(0, tk.END)

    def update_sides_label(self):
        self.sides_label.config(text="Грани кубика: " + ", ".join(self.sides))

    def roll_dice(self):
        if self.sides:
            result = random.choice(self.sides)
            self.result_label.config(text="Выпало: " + result)
        else:
            self.result_label.config(text="Сначала добавьте грани кубика!")

# Создаем главное окно
root = tk.Tk()
app = DiceApp(root)

# Запускаем главный цикл
root.mainloop()
