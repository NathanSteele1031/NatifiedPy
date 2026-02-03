import pygame

class WorldObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.x = 0
        self.y = 0

    def describe(self):
        return f"{self.name}: {self.description}"

class World:
    def __init__(self):
        self.objects = []
    
    def add_object(self, world_object: WorldObject, x: int, y: int):
        world_object.x = x
        world_object.y = y
        self.objects.append(world_object)
    
    def remove_object(self, world_object):
        self.objects.remove(world_object)