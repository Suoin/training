import pickle

# Путь к файлу
PLAYER_FILE = 'players_status.pkl'

# Рекурсивная функция для вывода всех данных
def recursive_print(obj, indent=0):
    """ Рекурсивно выводит содержимое объекта. """
    spacing = "  " * indent
    if isinstance(obj, dict):
        # Если объект - словарь, выводим его ключи и значения
        for key, value in obj.items():
            print(f"{spacing}Key: {key} ->")
            recursive_print(value, indent + 1)
    elif isinstance(obj, list):
        # Если объект - список, выводим элементы
        for i, item in enumerate(obj):
            print(f"{spacing}Index {i}:")
            recursive_print(item, indent + 1)
    elif isinstance(obj, object):
        # Если объект - экземпляр класса, выводим его атрибуты
        print(f"{spacing}Object of type {type(obj)}:")
        for attr in dir(obj):
            # Выводим только публичные атрибуты (без магических методов)
            if not attr.startswith("__"):
                try:
                    value = getattr(obj, attr)
                    print(f"{spacing}  {attr}: {value}")
                except Exception as e:
                    print(f"{spacing}  {attr}: Error reading attribute ({e})")
    else:
        # Просто выводим другие объекты (строки, числа и т.д.)
        print(f"{spacing}{repr(obj)}")

# Чтение и вывод данных из файла
try:
    with open(PLAYER_FILE, 'rb') as file:
        players_data = pickle.load(file)
        print("Содержимое файла:")
        recursive_print(players_data)  # Рекурсивно выводим все содержимое
except FileNotFoundError:
    print(f"Файл {PLAYER_FILE} не найден.")
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
