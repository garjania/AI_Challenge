import Model
from random import randint

from Game import Search


class AI:

    counter = 0

    def preprocess(self, world):
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
        for r in world.map.cells:
            for cell in r:
                if cell.is_in_objective_zone and not cell.is_wall:
                    row = cell.row
                    col = cell.column
                    break
        for hero in world.my_heroes:
            world.move_hero(hero=hero, direction=Search().search(hero, world.map, row, col))
    def action(self, world):
        print("action")
        for hero in world.my_heroes:
            row_num = randint(0, world.map.row_num)
            col_num = randint(0, world.map.column_num)
            abilities = hero.abilities
            world.cast_ability(hero=hero, ability=abilities[randint(0, len(abilities) - 1)],
                               cell=world.map.get_cell(row_num, col_num))



