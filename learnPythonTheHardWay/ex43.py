# -*- coding:utf-8 -*-
from sys import exit
from random import randint

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Scene(object):
    def enter(self):
        exit(1)

class Death(Scene):
    def enter(self):
        print "You died."
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "Central Corridor Scene"
        action = raw_input("> ")

        if action == "shoot!":
            return 'death'

        elif action == "dodge!":
            return 'death'

        elif action == "tell a joke":
            return 'laser_weapon_armory'

        else:
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print "Laser Weapon Armory"

        guesses = 0
        while True:
            code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
            print "code: ",code
            guess = raw_input("[keypad]> ")
            if  guess == code or guesses>8:
                break
            print "BZZZZEDDD"
            guesses += 1

        if guess == code:
            return 'the_bridge'
        else:
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print "The Bridge Scene"

        action = raw_input("> ")

        if action == "throw the bomb":
            return 'death'

        elif action == "slowly place the bomb":
            return 'escape_pod'
        else:
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print "Escape Pod Scene"
        good_pod = randint(1,5)
        print "good_pod: ",good_pod

        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            return 'death'
        else:
            return 'finished'

class Finished(Scene):
    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
