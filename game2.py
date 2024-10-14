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
        if table[condition[0] - 1] == table[condition[1] - 1] == table[condition[2] - 1]:  # сравниваем победные координаты
            return table[condition[0] - 1]  # возвращаем символ победителя
    return None  # возвращаем None, если нет победителя

def game():  # Функция игры
    current_player = "X"  # Текущий игрок
    moves_made = 0  # Счетчик сделанных ходов

    while True:  # Бесконечный цикл, пока не будет победителя или ничья
        table_game()  # Вызываем текущее состояние стола
        player_move = input(f"Ходит игрок {current_player}. Выберите номер клетки (1-9): ")  # Ход игрока

        if not player_move.isdigit():  # Проверяем, что вводится число
            print("Введите число от 1 до 9")
            continue  # Пропускаем итерацию, если ввод некорректен

        player_move = int(player_move)  # Преобразуем переменную в целое число

        if 1 <= player_move <= 9 and table[player_move - 1] not in ["X", "O"]:  # Проверяем допустимость и занятость клетки
            table[player_move - 1] = current_player  # Заменяем клетку символом текущего игрока
            moves_made += 1  # Увеличиваем счетчик сделанных ходов
            winner = check_winner()  # Проверяем, есть ли победная линия

            if winner:  # Если победитель есть
                table_game()
                print(f"Игрок {winner} выиграл!")  # Указываем победу текущего игрока
                return

            # Переключаем на второго игрока
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Некорректный ход. Попробуйте снова.")  # Если вводится недопустимое число

        if moves_made == 9:  # Если все клетки заполнены
            table_game()  # Показываем текущее поле
            print("Игра завершилась ничьей!")  # Конец игры
            return

game()  # Вызываем игру