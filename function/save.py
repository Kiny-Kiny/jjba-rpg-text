from time import sleep
from pickle import dump
def save():
  with open('PlayerBackup', 'wb') as f: dump(PlayerIG, f)
  print('     [ ! ] Jogo salvo com sucesso.');sleep(2)
