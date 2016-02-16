# -*- coding:utf-8 -*-
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self,paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""Lucky for you they made you learn Gothon insults in the academy.""")

the_bridge = Room("The Bridge",
"""The container clicks open and the seal breaks, letting gas out.""")

escape_pod = Room("Escape Pod",
""" There's 5 pods, which one do you take?""")

the_end_winner = Room("The End",""" You won!""")

the_end_loser = Room("The End","""You jump into a random pod and hit the eject button.""")

escape_pod.add_paths({'2': the_end_winner,'*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({'throw the bomb': generic_death,'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({'0132': the_bridge,'*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor
