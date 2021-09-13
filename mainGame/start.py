from function import clear, save
from battle import teste_fight
from random import randint
from time import sleep
from sys import stdout
from custom import logo
from enemyClasses import LadrãoIG, BandidoIG, VampireIG
##### Map #####
#mapa = {'World':{'CasaDoCrowley':{XP: 8000,DESCRIPTION: 'Lugar mais sujo e podre do mundo.',SUB_LOCAL: ['Esgoto', 'Lixao'],BOSS: ['Crowley', 'Mae do Crowley']}}}
##### Inventory #####
def inventory(PlayerIG):
  if PlayerIG.hp_pot >0: print("     [ ! ] Poção de HP: %s"%PlayerIG.hp_pot)
  elif PlayerIG.mp_pot >0: print("     [ ! ] Poção de MP: %s"%PlayerIG.mp_pot)
  elif PlayerIG.maxhp_pot >0: print("     [ ! ] Poção de MAX HP: %s"%PlayerIG.maxhp_pot)
  elif PlayerIG.maxmp_pot >0: print("     [ ! ] Poção de MAX MP: %s"%PlayerIG.maxmp_pot)
  else: print('     [ X ] Você não tem nenhum item.')
  choice = input('     [  ! ]Para beber uma poção, digite /beber (nome da poção)\n     [ Ex ]: /beber maxmp_pot\n     >')
  if choice == "/beber hp_pot": 
    if PlayerIG.hp_pot > 0:
      if PlayerIG.health >= PlayerIG.maxhealth:
        print("     [ ! ] Você está com o máximo de HP permitido.")
      else:
        PlayerIG.hp_pot=-1;print("     [ ! ] Você bebeu a poção e recuperou 15 de HP");PlayerIG.health+=15
        if PlayerIG.health > PlayerIG.maxhealth: PlayerIG.health = PlayerIG.maxhealth
    else: print("     [ X ] Item inválido.")
    sleep(2)
  elif choice =="/beber mp_pot":
    if PlayerIG.mp_pot > 0:
      if PlayerIG.mp >= PlayerIG.maxmp:
        print("     [ ! ] Você está com o máximo de HP permitido.")
      else: PlayerIG.mp_pot=-1;print("     [ ! ] Você bebeu a poção e recuperou 10 de MP");PlayerIG.mp+=10
    else: print("     [ X ] Item inválido.")
    sleep(2)
  elif choice =="/beber maxhp_pot":
    if PlayerIG.maxhp_pot > 0:
      if PlayerIG.health >= PlayerIG.maxhealth:
        print("     [ ! ] Você está com o máximo de HP permitido.")
      else: PlayerIG.maxhp_pot=-1;print("     [ ! ] Você bebeu a poção e recuperou 45 de HP");PlayerIG.mp+=45
    else: print("     [ X ] Item inválido.")
    sleep(2)
  elif choice =="/beber maxmp_pot":
    if PlayerIG.maxmp_pot > 0:
      if PlayerIG.mp >= PlayerIG.maxmp:
        print("     [ ! ] Você está com o máximo de MP permitido.")
        PlayerIG.maxmp_pot=-1;print("     [ ! ] Você bebeu a poção e recuperou 40 de MP");PlayerIG.mp+=40
    else: print("    [ X ] Item inválido.")
    sleep(2)
  else: print("     [ X ] Comando Inválido");sleep(2)
##### Shop #####
def store(PlayerIG):
  clear.clear();text=('%s     [ Vendedor Viajante ] : Olá %s, o que vai querer comprar?\n     [ ! ] Para comprar um item, digite /comprar (nome do item)\n     [ EX ] /comprar hp_pot'%(logo,PlayerIG.name))
  for fala_vendedor in text:
    stdout.write(fala_vendedor)
    stdout.flush()
    sleep(0.007)
  choice= input('''
     「 ¥ens 」: %s
     
     [ 20 ¥ens ] Poção MP
     [ 25 ¥ens ] Poção HP
     [ 50 ¥ens ] Poção MAX MP
     [ 65 ¥ens ] Poção MAX HP
     
     [ Para Sair, digite /sair]
     > '''%PlayerIG.gold)
  if choice == '/comprar mp_pot':
    if PlayerIG.gold <20: print("     [ X ] Você não tem ¥ens o suficiente para comprar este item.")
    else: PlayerIG.gold-=20;PlayerIG.mp_pot+=1;print("     [ $ ] Compra feita com sucesso.")
    sleep(2)
  elif choice == '/comprar hp_pot':
    if PlayerIG.gold<25: print("     [ X ] Você não tem ¥ens o suficiente para comprar este item")
    else: PlayerIG.gold-=25;PlayerIG.hp_pot+=1;print("     [ $ ] Compra feita com sucesso.")
    sleep(2)
  elif choice == '/comprar maxhp_pot':
    if PlayerIG.gold<50: print("     [ X ] Você não tem ¥ens o suficiente para comprar este item.")
    else: PlayerIG.gold-=50;PlayerIG.maxmp_pot+=1;print("     [ $ ] Compra feita com sucesso.")
    sleep(2)
  elif choice == '/comprar maxmp_bot':
    if PlayerIG.gold<65: print("     [ X ] Você não tem ¥ens o suficiente para comprar este item.")
    else: PlayerIG.gold-=65;PlayerIG.maxmp_pot+=1;print("     [ $ ] Compra feita com sucesso.")
  elif choice == '/sair': start(PlayerIG)
  store(PlayerIG)
  
##### Battle System #####
def battleSystem(PlayerIG, enemy, Turno):
  if Turno == 'Player': teste_fight.fight(Turno, PlayerIG, enemy)
  elif Turno == 'Enemy':
    if enemy.standuser==True:
      randomChoice=randint(1,2)
      if randomChoice==1: teste_fight.enemy_stand(Turno, PlayerIG, enemy)
      elif randomChoice==2: teste_fight.enemy_move(Turno, PlayerIG, enemy)
    else:teste_fight.enemy_move(Turno, PlayerIG, enemy)

def standUser_fight(PlayerIG, enemy):
  if PlayerIG.stand_velocidade > enemy.stand_velocidade: Turno= 'Player'
  elif PlayerIG.stand_velocidade < enemy.stand_velocidade: Turno='Enemy'
  else:
    enemyD100=randint(1,100)
    playerD100=randint(1,100)
    if playerD100 > enemyD100: Turno='Player'
    elif playerD100 < enemyD100: Turno='Enemy'
    else: standUser_fight(PlayerIG)
  battleSystem(PlayerIG, enemy, Turno)
def normalFight(PlayerIG, enemy):
  if PlayerIG.velocidade > enemy.velocidade: Turno = 'Player'
  elif PlayerIG.velocidade < enemy.velocidade: Turno = 'Enemy'
  else:
    enemyD100=randint(1,100)
    playerD100=randint(1,100)
    if playerD100 > enemyD100: Turno = 'Player'
    elif playerD100 < enemyD100: Turno = 'Enemy'
    else: normalFight(PlayerIG,enemy,enemy)
  battleSystem(PlayerIG, enemy, Turno)
def random_fight(PlayerIG):
  global enemy
  enemynum=randint(1,3)
  if enemynum == 1:
    enemy = BandidoIG
  elif enemynum == 2:
    enemy = LadrãoIG
  else:
    enemy=VampireIG
  normalFight(PlayerIG, enemy)

def fightMenu(Turno, PlayerIG,enemy):
  if PlayerIG.health > PlayerIG.maxhealth: PlayerIG.health=PlayerIG.maxhealth
  elif PlayerIG.mp > PlayerIG.maxmp: PlayerIG.mp=PlayerIG.maxhealth
  clear.clear();choice=input('''%s
     「 HP 」: [%s/%s]   「 MP 」: [%s/%s]
   [ 1 ] Attack     [ 2 ] Stand     [ 3 ] Inventory
         
         [ 4 ] Tecnicas     [ 5 ] Fugir
  '''%(logo, PlayerIG.health, PlayerIG.maxhealth, PlayerIG.mp, PlayerIG.maxmp))
  if choice =='1': print("     [ ! ] Attack")
  elif choice =='2': print("     [ ! ] Stand")
  elif choice =='3': print("     [ ! ] Inventory")
  elif choice =='4': print("     [ ! ] Exit")
  elif choice == '5': teste_fight.run(Turno,PlayerIG, enemy)
  fightMenu(PlayerIG, enemy)
##### Main Menu #####
def start(PlayerIG):
  clear.clear()
  tecnicas='Nenhuma'
  if PlayerIG.hamon == True: tecnicas="Hamon"
  elif PlayerIG.spin == True: tecnicas="Spin"
  if PlayerIG.hamon == True and PlayerIG.spin == True: tecnicas='Hamon e Spin'
  op = input('''%s
    Posição:
    Local:
    Sub-Local:
    Descrição: 
    
          「 HP 」: [%s/%s] 「 MP 」: [%s/%s]
              「 Tecnica(s) 」: %s
    ☆/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\☆
         「 /andar 」「 /inspecionar 」「 /viajar 」
    ☆/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\☆
    「 1 」Salvar 「 2  」Sair 「 3 」Inventário
     > '''%(logo, PlayerIG.health, PlayerIG.maxhealth, PlayerIG.mp, PlayerIG.maxmp, tecnicas)).lower()
  if op == '/andar': store(PlayerIG)
  elif op  == '/inspecionar': pass
  elif op == '/viajar': pass
  elif op == '1': save.save(PlayerIG)
  elif op == '2': exit()
  elif op == '3': inventory(PlayerIG);start(PlayerIG)
  start(PlayerIG)

#def start(PlayerIG):
  #clear.clear();print('''\n     「 Stand Name 」: %s     「 Stand User 」: %s'''%(PlayerIG.standname, PlayerIG.name)) 
  #menu(PlayerIG)
