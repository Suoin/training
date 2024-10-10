table = list(range(1, 10))  # создаем доску
def table_game():  # функция вывода текущего состояния стола
    print("-" * 14)
    for pos in range(3):
        print("|", table[0 + pos * 3], "|", table[1 + pos * 3], "|", table[2 + pos * 3], "|")  # разделяем доску
        print("-" * 14)
def check_winner():  # функция проверки победителя
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # строки
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # столбцы
        [1, 5, 9], [3, 5, 7]  # диагонали
    ]
    for condition in win_conditions:
        if table[condition[0] - 1] == table[condition[1] - 1] == table[condition[2] - 1]:
            return table[condition[0] - 1]
    return None
def game():  # Функция игры
    current_player = "X"
    for i in range(9):
        table_game()
        player_move = input(f"Ходит игрок {current_player}. Выберите номер клетки (1-9): ")
        if not player_move.isdigit():
            print("Введите число от 1 до 9")
            continue
        player_move = int(player_move)
        if 1 <= player_move <= 9 and table[player_move - 1] not in ["X", "O"]:
            table[player_move - 1] = current_player
            winner = check_winner()
            if winner:
                table_game()
                print(f"Игрок {winner} выиграл!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Некорректный ход. Попробуйте снова.")

    table_game()
    print("Игра завершилась ничьей!")


game()