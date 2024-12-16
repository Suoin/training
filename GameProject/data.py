import pickle
import os
from player import Player

PLAYER_FILE = 'players_status.pkl'


# Объект бота


#Модуль сохранения состояния игрока

def load_players():
    if os.path.exists(PLAYER_FILE):
        with open(PLAYER_FILE, 'rb') as f:
            return pickle.load(f)
    return {}
def save_players():
    with open(PLAYER_FILE, 'wb') as f:
        pickle.dump(player, f)

player = load_players()  # Загружаем состояние игроков при запуске