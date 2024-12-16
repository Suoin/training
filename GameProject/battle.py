import random

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def show_stat(self):
        return f"{self.name} - Здоровье: {self.hp}, Атака: {self.attack}"

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def attack_player(self, player):
        # Урон врага по игроку
        player.hp -= self.attack
        if player.hp < 0:
            player.hp = 0

class Goblin(Enemy):
    def __init__(self, name="Гоблин"):
        super().__init__(name, hp=50, attack=5)

class Orc(Enemy):
    def __init__(self, name="Орк"):
        super().__init__(name, hp=80, attack=10)

def generate_enemy():
    # Генерация случайного врага
    enemy_types = [Goblin(), Orc()]
    return random.choice(enemy_types)

def start_battle(chat_id, message_id, enemy, bot, player_attack):
    bot.deleteMessage((chat_id, message_id))  # Удаляем старое сообщение
    bot.sendMessage(chat_id, f"Вы начали бой с {enemy.name}!\n{enemy.show_stat()}")
    keyboard = player_attack(chat_id)
    bot.sendMessage(chat_id, "Ваш ход!", reply_markup=keyboard)

def battle_turn(chat_id, message_id, player_action, enemy, bot, player):
    # Удаляем старое сообщение
    bot.deleteMessage((chat_id, message_id))

    # Выполнение действия игрока (например, атака)
    damage = calculate_damage(player[chat_id], enemy)  # Расчет урона
    enemy.take_damage(damage)

    # Ответ врага
    enemy.attack_player(player[chat_id])

    # Отправка сообщений о результатах
    bot.sendMessage(chat_id, f"Вы нанесли {damage} урона {enemy.name}!\n"
                             f"{enemy.name} нанес вам {enemy.attack} урона.\n"
                             f"Ваше здоровье: {player[chat_id].hp}\n"
                             f"Здоровье {enemy.name}: {enemy.hp}")

    # Проверка на победу или поражение
    if not enemy.is_alive():
        bot.sendMessage(chat_id, f"Вы победили {enemy.name}!")
        player[chat_id].battle_data = None  # Завершаем бой
    elif player[chat_id].hp <= 0:
        bot.sendMessage(chat_id, "Вы проиграли бой.")
        player[chat_id].battle_data = None  # Завершаем бой
