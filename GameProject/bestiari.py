class Monster:
    def __init__(self, name):
        self.name = name
        # Зависиимости от характеристик
        self.attack = 10
        self.hp = 100  # очки здоровья
        self.mana = 50  # очки маны
        # характеристик
        self.sila = 5  # cила влияет на на хп и урон
        self.agila = 5  # ловкость влияете на урон + крит удар
        self.intelect = 5  # Интелект влияет на ману и урон

        # Контейнеры
        self.abillity = []  # Текущие способности
        # Зона флагов и состояний

    def show_stat(self):
        stat = (
                f'Имя :{self.name}\n'
                f'Здоровье: {self.hp}\n'
                f'Мана: {self.mana}\n'
                f'Сила: {self.sila}\n'
                f'Ловкость: {self.agila}\n'
                f'Интеллект: {self.intelect}\n'
                f"Способности: {', '.join(self.abillity) if self.abillity else 'Нет'}"
                )
        return stat

class Goblin(Monster):
    def __init__(self, name='Гоблин'):
        super().__init__(name)  # Вызов конструктора родительского класса
        # Переопределяем только те атрибуты, которые специфичны для гоблина
        self.attack = 5  # Переопределение атаки
        self.hp = 50  # Переопределение здоровья
        self.mana = 1  # Переопределение маны
        self.abillity = ['Коварный удар']  # Способности, которые есть у гоблина

    def attack_p(self,target):
        damage = self.attack
        target.hp -= damage

