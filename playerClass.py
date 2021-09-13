class Player:
  def __init__(self, playerName, standName,poderDestrutivo, velocidade, alcance, precisao, durabilidade, desenPotencial):
    ##### Player #####
    self.name=playerName
    self.maxhealth=100
    self.health=100
    self.hamon=False
    self.spin=False
    self.hamon_tec=[]
    self.spin_tec=[]
    self.mp=20
#    self.maxhm=20
#    self.hm=20
    self.maxmp=20
    self.maxlevel=250
    self.attack=10
    self.durabilidade=10
    self.velocidade=10
    self.gold=0
    self.pot_hp=0
    self.pot_mp=0
    self.xp=0
    self.level=1
    self.nextlvl=self.level+1
    #### Potion Bag #####
    self.bag=[]
    #### Potion #####
    self.maxhp_pot=0
    self.maxmp_pot=0
    self.hp_pot=0
    self.mp_pot=0
    ##### Stand #####
    self.standname=standName
    self.skill=[]
    self.stand_poderDestrutivo=poderDestrutivo
    self.stand_velocidade=velocidade
    self.stand_alcance=alcance
    self.stand_precisao=precisao
    self.stand_durabilidade=durabilidade
    self.stand_desenPotencial=desenPotencial
