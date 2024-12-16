from config import bot
class Player:
    def __init__(self,name):
        self.name = name
        #Зависиимости от характеристик
        self.attack = 10
        self.hp = 100 # очки здоровья
        self.mana = 50 # очки маны
        #характеристик
        self.sila = 5 #cила влияет на на хп и урон
        self.agila = 5 #ловкость влияете на урон + крит удар
        self.intelect = 5 #Интелект влияет на ману и урон
        self.luck = 5 #Удача влияете на хз что пока
        #Контейнеры
        self.invetary =[] #инвентарь
        self.abillity = [] #Текущие способности
        self.player_class =[] # Воин, Маг, Стрелок, Везунчик
        self.use_hand = [] # Помещаем сюда основное оружие
        self.quest_invetary =[ ] # да я допустил ошибку, но мне уже лень переписывать. Здесь храним предметы которые не использщуются но важны для сюжета
        # Зона флагов и состояний
        self.goblin_flag = False #скрытый квест на логово гоблинов

        #Флаги скрытых боссов
        self.black_dragon = False
        self.green_dragon = False
        self.red_dragon = False
        self.gold_dragon = False
        self.system ={
            'action':{
            'Меч-палка':self.stock_sword
        }}
        #self.system =[] # Контейнер костыль, ввиду того что я быдлокодер и лошара и не могу это реализовать иначе, я просто сменил концепцию


    def show_stat(self):
        stat= (f'Имя :{self.name}\n'
               f'Класс {', '.join(self.player_class) if self.player_class else 'Нет'}\n'
               f'Основное оружие: {', '.join(self.use_hand) if self.use_hand else 'Нет'}\n'
               f'Здоровье: {self.hp}\n'
               f'Мана: {self.mana}\n'
               f"Способности: {', '.join(self.abillity) if self.abillity else 'Нет'}\n"
               '\n'
               f'Сила: {self.sila}\n'
               f'Ловкость: {self.agila}\n'
               f'Интеллект: {self.intelect}\n'
               f'Удача: {self.luck}\n'
               '\n'
               f'Рюкзак: {', '.join(self.quest_invetary) if self.quest_invetary else 'Пусто'}\n'
               f"Карманы и сумки: {', '.join(self.invetary) if self.invetary else 'Пусто'}\n"


               )
        return stat
#КОСТЫЛЬ для реализации динамического боя
    def stock_sword(self, target):
        damage = 30  # Урон мечом
        target.hp -= damage
        return f'Вы ударили деревяным мечом и нанесли {damage} урона.'