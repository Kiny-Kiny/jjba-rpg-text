from random import randint
from time import sleep
from function import clear
import enemyClasses
##### Your Attack #####
def fight(Turno, PlayerIG, enemy):
  result=randint(1,20)
  PlayerDamage=randint(1, int(PlayerIG.attack*2 / 2))
  if result < 10: print('     「 %s 」 ERROU O ATAQUE!'%PlayerIG.name)
  else: print('     「 %s 」 ACERTOU O GOLPE E INFLINGIU %s DE DANO!'%(PlayerIG.name, PlayerDamage));enemy.health-=PlayerDamage
  sleep(2)
  if enemy.health <= 0:
    print('     Parabéns 「 %s 」! Você venceu!'%PlayerIG.name);levelUp_system(PlayerIG, enemy);exit()
  else:
    enemy_move(Turno,PlayerIG, enemy)
##### Enemy's Attack #####
def enemy_move(Turno,PlayerIG, enemy):
  result=randint(1,20)
  EnemyDamage=randint(1, int(enemy.attack *2 / 2))
  if result < 10: print('     「 %s 」 ERROU O ATAQUE!'%enemy.name)
  else: print('     「 %s 」 ACERTOU O GOLPE E INFLINGIU %s DE DANO!'%(enemy.name, EnemyDamage));PlayerIG.health-=EnemyDamage
  sleep(2)
  if PlayerIG.health <= 0:
    print('     Que pena 「 %s 」! Você perdeu!'%PlayerIG.name);exit()
  else:
    fight(Turno, PlayerIG, enemy)
##### Level Up System #####
def levelUp_system(PlayerIG, enemy):
  XP=int(enemy.xpgain+int(PlayerIG.level * 3))
  PlayerIG.xp+=XP;PlayerIG.gold+=enemy.goldgain
  random_levelUp=randint(1,10)
  if PlayerIG.level == PlayerIG.maxlevel:
    text=("     [ ! ] Você já está no nível maximo!")
  else:
    if random_levelUp >= 7: PlayerIG.maxhealth=+5;PlayerIG.maxmp=+5;PlayerIG.maxhealthPlayerIG.level+=1;text=('''     「 Parabéns! Você subiu de nível! Seu nível atual é %s 」\n     「 Você ganhou %s de XP e %s ¥ens 」'''%(PlayerIG.level, XP, enemy.goldgain))
    else: text=('''     「 Você ganhou %s de XP e %s ¥ens 」'''%(XP, enemy.goldgain))
  print(text);sleep(2)
################################
def standMenu(PlayerIG, enemy):
  from start import fightMenu
  if PlayerIG.mp <= 0:
    print("     [ X ] Você não tem MP para usar seu Stand.");sleep(2);fightMenu(PlayerIG, menu)
  clear.clear()
  print("%s"%logo)
  for i in PlayerIG.skill:
    print('     [ - ] %s')
  op=input("\n     [ ! ] Para usar uma habilidade, digite /stand (habilidade)\n     [ EX ] /stand time_stop\n     [ Para sair, digite /sair ]\n     >")
  if op=="/time_stop": pass
  elif op=="/time_erase": pass
  elif op=="/bitesTheDust": pass
  elif op == '/sair': fightMenu(PlayerIG, enemy)
def standAttack(PlayerIG, enemy):
  pass
##### Run ######
def run(Turno, PlayerIG, enemy):
  from start import start
  numrun = randint(1, int(PlayerIG.velocidade))
  if numrun > enemy.velocidade: print("     [ ! ] Você consegiu fugir!");sleep(2);start.start(PlayerIG)
  else: print("     [ X ] Você não conseguiu fugir.");sleep(2);enemy_move(Turno,PlayerIG, enemy)
##### Enemy's Stand #####
def standEnemy(PlayerIG, enemy):
  pass
