typing_speed=650
from custom import logo
from sys import stdout
from random import random, randint, choice
from time import sleep
from function import clear, loader
from os import system, path
from pickle import dump, load
##### Intro #####
for char in logo:
    stdout.write(char);stdout.flush();sleep(random()*10.0/typing_speed)
##### New game #####
def newGame():
  from mainGame import start
  clear.clear();system('rm -rf PlayerBackup && rm -rf StandBackup')
  from playerClass import Player
  playerName=input("%s\n     [ ! ] Digite seu nome > "%logo)
  standName=input("     [ ! ] Digite um nome para seu Stand > ")
#  type=choice(['Não-Remoto', 'Remoto','Automático','Guardião','Objeto','União', 'Habilidade', 'Colônia', 'Sem-Usuário', 'Compartilhamento'])
  global My_Stand, PlayerIG
  stand_poderDestrutivo=choice(['A','B','C','D','E'])
  stand_Velocidade=choice(['A','B','C','D','E'])
  stand_Durabilidade=choice(['A','B','C','D','E'])
  stand_Precisao=choice(['A','B','C','D','E'])
  stand_Desenvolvimento=choice(['A','B','C','D','E'])
  ##########
  status ={'A':[21, 25],'B':[16, 20],'C':[11, 15],'D':[6, 10],'E':[1, 5]}
  ##########
  poderDestrutivo= randint(status['%s'%stand_poderDestrutivo][0], status['%s'%stand_poderDestrutivo][1])
  velocidade = randint(status['%s'%stand_Velocidade][0], status['%s'%stand_Velocidade][1])
  durabilidade = randint(status['%s'%stand_Durabilidade][0], status['%s'%stand_Durabilidade][1])
  precisao = randint(status['%s'%stand_Precisao][0], status['%s'%stand_Precisao][1])
  desenPotencial = randint(status['%s'%stand_Desenvolvimento][0], status['%s'%stand_Desenvolvimento][1])
  ##########
  if stand_poderDestrutivo == 'A': stand_Alcance="E"
  elif stand_poderDestrutivo == 'B': stand_Alcance=choice(["E","D"])
  elif stand_poderDestrutivo == 'C': stand_Alcance=choice(["E","D","C"])
  elif stand_poderDestrutivo == 'D': stand_Alcance=choice(["E","D","C","B"])
  elif stand_poderDestrutivo =='E': stand_Alcance=choice(["E","D","C","B","A"])
  alcance = randint(status['%s'%stand_Alcance][0], status['%s'%stand_Alcance][1])
  print('''
     「 Stand Name 」: %s
     「 Stand User 」: %s
     
     「 Poder Destrutivo 」: %s
     「 Velocidade 」: %s
     「 Alcance 」: %s
     「 Durabilidade 」: %s
     「 Precisão 」: %s
     「 Desenvolvimento Potencial 」: %s
  '''%(standName, playerName, stand_poderDestrutivo,stand_Velocidade, stand_Alcance, stand_Durabilidade, stand_Precisao, stand_Desenvolvimento))
  input('     [ < Aperte Enter para começar > ]')
  PlayerIG=Player(playerName,standName, poderDestrutivo, velocidade, alcance, precisao, durabilidade, desenPotencial)
  with open('PlayerBackup', "wb") as f: dump(PlayerIG, f)
  start.start(PlayerIG)
#### Initial Menu #####
def init():
  choice=input('''\n     [ 1 ] > Novo Jogo\n     [ 2 ] > Continuar\n     [ 3 ] > Sair\n     >>> ''');clear.clear()
  if choice == '1': newGame()
  elif choice == '2': loader.loadGame()
  elif choice == "3": exit()
  else: init()
#### Dialog ####
def text(text_1):
  typing_speed=100
  text=text_1
  for char in text:
    stdout.write(char);stdout.flush();sleep(random()*10.0/typing_speed)
#;text(text_1='''     Pode parecer um espirito maligno, mas não é. Aquilo que você acreditava ser um espirito maligno é uma poderosa visão, criada de sua própria energia vital. Por aparecer ao seu lado, a visão é chamada de... Stand! ''')
