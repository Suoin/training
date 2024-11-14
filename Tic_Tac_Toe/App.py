import tkinter as tk
from tkinter import messagebox

# Создаем доску
table = [""] * 9

def table_game():
    for i in range(9):
        button = tk.Button(frame, text=table[i], font=('Arial', 20), width=5, height=2,
                           command=lambda i=i: player_move(i))
        button.grid(row=i // 3, column=i % 3)

def check_winner():
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for condition in win_conditions:
        if table[condition[0] - 1] == table[condition[1] - 1] == table[condition[2] - 1] and table[condition[0] - 1] != "":
            return table[condition[0] - 1]
    return None

def player_move(pos):
    global current_player
    if table[pos] == "":  # Проверяем, что клетка свободна
        table[pos] = current_player
        table_game()
        winner = check_winner()
        if winner:
            messagebox.showinfo("Победа!", f"Игрок {winner} выиграл!")
            reset_game()
        elif all(x != "" for x in table):
            messagebox.showinfo("Ничья!", "Игра завершилась ничьей!")
            reset_game()
        current_player = "O" if current_player == "X" else "X"
        update_current_player_display()

def reset_game():
    global table, current_player
    table = [""] * 9
    current_player = "X"
    table_game()
    update_current_player_display()

def update_current_player_display():
    current_player_label.config(text=f"Текущий игрок: {current_player}")

def exit_game():
    root.quit()

# Основное окно
root = tk.Tk()
root.title("Крестики Нолики")
current_player = "X"

# Создаем кнопки сверху
button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")  # Сдвигаем к левому краю

# Кнопка "Выйти из игры"
btn_exit = tk.Button(button_frame, text="Выйти из игры", command=exit_game)
btn_exit.pack(side=tk.LEFT)

# Создаем фрейм для игрового поля и центруем его
frame = tk.Frame(root)
frame.grid(row=1, column=0, padx=50, pady=50)  # Используем отступы для центровки

# Метка для отображения текущего игрока
current_player_label = tk.Label(root, text=f"Текущий игрок: {current_player}", font=('Arial', 16))
current_player_label.grid(row=2, column=0, padx=20)

table_game()

# Запуск приложения
root.mainloop()