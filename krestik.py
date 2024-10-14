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
        if table[condition[0] - 1] == table[condition[1] - 1] == table[condition[2] - 1]: #cсравниваем победные координаты
            return table[condition[0] - 1]  # возвращаем символ победителя
    return None  # возвращаем пустоту если нет победителя
def game():  # Функция игры
    current_player = "X" # Текущий игрок
    for i in range(9): # Максимальное количество ходов
        table_game() # Вызываем текуще состояние стола
        player_move = input(f"Ходит игрок {current_player}. Выберите номер клетки (1-9): ") # Ход игрока
        if not player_move.isdigit(): # Проверяем что он вводит цифры и если нет, сообщаем ему и продолжаем цикл
            print("Введите число от 1 до 9")
            continue
        player_move = int(player_move) # преобразуем переменную в целое число
        if 1 <= player_move <= 9 and table[player_move - 1] not in ["X", "O"]: # делаем проверку на допустимое число и занятость клетки
            table[player_move - 1] = current_player # заменяем клетку символом текущего игрока
            winner = check_winner() # Проверяем есть ли победная линия
            if winner: #если победитель есть
                table_game()
                print(f"Игрок {winner} выиграл!") #указываем победу текущего игрока
                return
            current_player = "O" if current_player == "X" else "X" # Переключаем на второго игрока
        else:
            print("Некорректный ход. Попробуйте снова.") # если вводится не допустимое число
    table_game() # показываем текущее поле
    print("Игра завершилась ничьей!") # конец цикла
game() # вызываем игру