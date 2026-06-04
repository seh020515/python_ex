import random

player = {
    'name': input('캐릭터 이름을 입력하세요: '),
    'hp': 100,
    'attack': 10,
    'items': [],
    'potion': 2
}

class Player:
    def __init__(self):
        self.name = input('캐릭터 이름을 입력하세요: ')
        self.hp = 100
        self.attack = 10
        self.items = []
        self.potion = 2
    def use_potion(self):
        if self.potion > 0:
            self.hp += 30
            self.potion -= 1
            print(f'HP가 회복됐다! 현재 HP: {self.hp} 포션: {self.potion}개')
        else:
            print('포션이 없다!')

    def take_damage(self, damage):
        self.hp -= damage
        print(f'플레이어 HP: {self.hp}')



class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    def take_damage(self, damage):
        self.hp -= damage
        print(f'{self.name}의 HP: {self.hp}')

slime  = Monster('슬라임', 15, 5)
goblin = Monster('고블린', 50, 10)
orc    = Monster('오크', 75, 15)

monsters = [ Monster('슬라임', 15, 5),
            Monster('고블린', 50, 10),
            Monster('오크', 75, 15)]

class Game:
    def __init__(self):
        self.player = Player()
        self.monsters = [
            Monster('슬라임', 15, 5),
            Monster('고블린', 50, 10),
            Monster('오크', 75, 15)
        ]
        self.boss = Monster('투명 드래곤', 200, 50)
        self.defeated = []
        self.items = []
    def battle(self, moster):
        pass

    def drop_item(self):
        pass

    def run(self):
        pass

monsters = [
    {'name': '슬라임', 'hp': 15, 'attack': 5},
    {'name': '고블린', 'hp': 50, 'attack': 10},
    {'name': '오크', 'hp': 75, 'attack': 15}
]
boss = {'name': '헥슘 투명 드래곤', 'hp': 200, 'attack': 30}
defeated = []
items = [
    {'name': 'HP 강화', 'hp': 30, 'attack': 0,'potion': 0},
    {'name': '공격력 강화', 'hp': 0, 'attack': 15, 'potion': 0},
    {'name': 'HP 포션', 'hp': 0, 'attack': 0, 'potion': 1}
]


while True:
    original = random.choice(monsters)

    monster = {
        'name' : original['name'],
        'hp' : original['hp'],
        'attack' : original['attack']
    }

    print(f'{monster['name']}이(가) 나타났다!')
    print('''.　ヽ　|　|　 /　 ／
            ＼ ヽ |　|　/　／
            　＼　　　　 ／　 ＿
            ― /i⌒i⌒i⌒i－￣ 
            三｜|　|　|　|∧_∧ 
            _〈_{＿|＿}_ノ)`o´) <ぐ
            　／`ー―(＿ノ　_ﾉっㅠㅠ
            ／　/ ｜ | ヽし(_) ''')
    while monster['hp'] > 0 and player['hp'] > 0:
        print(f'[{player["name"]}] HP: {player["hp"]} | 포션: {player["potion"]}개')
        print('-' * 40)
        choice = int(input('1.공격 2.도망 3.포션 사용 : '))

        if choice == 1:
            monster['hp'] -= player['attack']
            print(f'{monster['name']}의 HP: {monster["hp"]}')
            if monster['hp'] > 0:
                player['hp'] -= monster['attack']
                print(f'플레이어 HP: {player["hp"]}')
                print('-' * 40)

        elif choice == 2:
            print('도망치고 말았다!')
            break
        
        elif choice == 3:
            if player['potion'] > 0:
                player['hp'] += 30
                player['potion'] -= 1
                print(f'HP가 회복됐다! 현재 HP: {player["hp"]} 포션: {player["potion"]}개')
            else:
                print('포션이 없다!')

    if monster['hp'] <= 0:
        print(f'{monster["name"]}을(를) 처치했다!')
        print('''
                  .∧＿∧      ∧_∧.
                (  `・ω・)つ)゜Д゜)・゜
                (つ    r  ⊂   ⊂)
                |    _つ ⊂_⊂ノ
                `し´  ''')
        defeated.append(monster['name'])
        drop = random.choice(items)
        print(f'{drop["name"]} 을(를) 획득했다!')
        player['hp'] += drop['hp']
        player['attack'] += drop['attack']
        player['potion'] += drop['potion']
        print(f'포션이 {player["potion"]}개가 되었다!')

    elif player['hp'] <= 0:
        print('게임 오버...')
        break

    if len(defeated) >= len(monsters):
        print('보스[헥슘 투명 드래곤]이(가) 나타났다!')
        print('''                            ______________
                        ,===:'.,            `-._
                            `:.`---.__         `-._
                                `:.     `--.         `.
                                \.        `.         `.
                        (,,(,    \.         `.   ____,-`.,
                        (,'     `/   \.   ,--.___`.'
                    ,  ,'  ,--.  `,   \.;'         `
                    `{D, {    \  :    \;
                    V,,'    /  /    //
                    j;;    /  ,' ,-//.    ,---.      ,
                    \;'   /  ,' /  _  \  /  _  \   ,'/
                            \   `'  / \  `'  / \  `.' /
                            `.___,'   `.__,'   `.__,'   ''')

              
        while boss['hp'] > 0 and player['hp'] > 0:
            print(f'[{player["name"]}] HP: {player["hp"]} | 포션: {player["potion"]}개')
            choice = int(input('1.공격 2.도망 3.포션 사용 : '))

            if choice == 1:
                boss['hp'] -= player['attack']
                print(f'{boss['name']}의 HP: {boss["hp"]}')
                if boss['hp'] > 0:
                    player['hp'] -= boss['attack']
                    print(f'플레이어 HP: {player["hp"]}')

            elif choice == 2:
                print('도망치고 말았다!')
                break
                
            elif choice == 3:
                if player['potion'] > 0:
                        player['hp'] += 30
                        player['potion'] -= 1
                        print(f'HP가 회복됐다! 현재 HP: {player["hp"]} 포션: {player["potion"]}개')
                else:
                        print('포션이 없다!')

        if boss['hp'] <= 0:
                print(f'{boss["name"]}을(를) 처치했다!')
                print('축하합니다!')
                break

        elif player['hp'] <= 0:
                print('게임 오버...')
                break

    break