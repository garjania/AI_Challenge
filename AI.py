import Model
from random import randint

from Game import Search


class AI:

    counter = 0
    zone = []
    go = []

    def preprocess(self, world,):
        for r in world.map.cells:
            for cell in r:
                if cell.is_in_objective_zone and not cell.is_wall:
                    row = cell.row
                    col = cell.column
                    self.zone.append([row, col])
        for i in range(4):
            row = self.zone[randint(0, len(self.zone) - 1)][0]
            col = self.zone[randint(0, len(self.zone) - 1)][1]
            self.go.append([row,col])
        print("preprocess")

    def pick(self, world):
        self.counter += 1
        print("pick", self.counter)
        if self.counter < 3:
            world.pick_hero(Model.HeroName.SENTRY)
        if self.counter == 3:
            world.pick_hero(Model.HeroName.GUARDIAN)
        if self.counter > 3:
            world.pick_hero(Model.HeroName.BLASTER)

    def move(self, world):
        print("move")
        i=0
        for hero in world.my_heroes:
            row=self.go[i][0]
            col=self.go[i][1]
            world.move_hero(hero=hero, direction=Search().search(hero, world.map, row, col))
            i+=1
    def action(self, world):
        print("action")
        for hero in world.my_heroes:
            row_num = randint(0, world.map.row_num)
            col_num = randint(0, world.map.column_num)
            abilities = hero.abilities
            world.cast_ability(hero=hero, ability=abilities[randint(0, len(abilities) - 1)],
            cell=world.map.get_cell(row_num, col_num))



