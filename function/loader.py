global My_Stand, PlayerIG
from os import path
from pickle import load
def loadGame():
  from main import newGame
  from mainGame import start
  if path.exists('PlayerBackup') == True:
    with open('PlayerBackup', 'rb') as f: PlayerIG=load(f)
    start.start(PlayerIG)
  else:
    newGame()
