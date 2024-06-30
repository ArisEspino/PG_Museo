import matplotlib.pyplot as plt
class Collisions:
    def __init__(self, app):
        self.app = app
        self.positions_models = ((0.10, -5.01), (-8.4, -10.4))
        self.limits = 1.4
    def check_limits(self):
        print(self.app.position)
        collisionFound = True
        length_positions = len(self.positions_models)
        for i in range(length_positions):
            bool_x = self.positions_models[i][0] - self.limits < self.app.x < self.positions_models[i][0] + self.limits
            bool_z = self.positions_models[i][1] - self.limits < self.app.z < self.positions_models[i][1] + self.limits
            if bool_x and bool_z:
                collisionFound = False
                break
        if collisionFound:
            return True
        else:
            return False

class Collisions_two:
    def __init__(self, app):
        self.app = app
        self.positions_models = ((-2.32, -2.43), (-2.47, -4.46),
                                 (-2.40, -7.52), (-0.05, -7.54), (2.44, -7.54), (2.46, -4.51), (2.52, -2.55))
        self.limits = 0.2
    def check_limits(self):
        print(self.app.position)
        collisionFound = True
        length_positions = len(self.positions_models)
        for i in range(length_positions):
            bool_x = self.positions_models[i][0] - self.limits < self.app.x < self.positions_models[i][0] + self.limits
            bool_z = self.positions_models[i][1] - self.limits < self.app.z < self.positions_models[i][1] + self.limits
            if bool_x and bool_z:
                collisionFound = False
                break
        if collisionFound:
            return True
        else:
            return False