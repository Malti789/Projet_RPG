
def attack(self):
        room = world.tile_at(self.x, self.y)  
        enemy = room.enemy
        print ("Tu as attaqué {}!".format(enemy.name))    
        enemy.hp-=self.power+self.powerup 
        if not enemy.is_alive():
            print ("Tu as tué {}!".format(enemy.name))
            self.gold=self.gold+enemy.gold
            self.exp=self.exp+enemy.exp
            print ("Tu as gagné {} experience ".format(enemy.exp))

class map:
    def __init__(self,dx,dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self) :
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

