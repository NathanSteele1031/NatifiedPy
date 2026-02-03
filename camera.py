import world

class Camera(world.WorldObject):
    def __init__(self, target: world.WorldObject):
        super().__init__("Camera", "The camera following a target object.")
        self.target = target
        self.update_position()

    def update_position(self):
        self.x = self.target.x
        self.y = self.target.y