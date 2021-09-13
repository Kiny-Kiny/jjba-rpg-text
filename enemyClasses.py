from random import randint
class DIO:
  def __init__(self, name):
    self.name=name
    self.maxhealth=500
    self.health=self.maxhealth
    self.standuser=True
    self.attack=75
    self.goldgain=200000
    self.stand_user=True
    self.standname='The World'
    self.attack=90
    self.velocidade=85
    self.durabilidade=90
DIOIG= DIO("DIO")

class Vampiro:
  def __init__(self, name):
    self.name=name
    self.maxhealth= 120
    self.health=self.maxhealth
    self.standuser=False
    self.attack=12
    self.durabilidade=12
    self.velocidade=12
    self.goldgain=randint(5, 15)
    self.xpgain=randint(7, 20)
VampireIG= Vampiro("Vampiro")

class Bandido:
  def __init__(self, name):
    self.name=name
    self.maxhealth=50
    self.health=self.maxhealth
    self.standuser=False
    self.attack=5
    self.durabilidade=7
    self.velocidade=7
    self.goldgain=10
    self.xpgain=7
BandidoIG= Bandido("Bandido")
class Ladrão:
  def __init__(self, name):
    self.name=name
    self.maxhealth=70
    self.health=self.maxhealth
    self.standuser=False
    self.attack=7
    self.durabilidade=9
    self.velocidade=9
    self.goldgain=15
    self.xpgain=10
LadrãoIG= Ladrão("Ladrão")
