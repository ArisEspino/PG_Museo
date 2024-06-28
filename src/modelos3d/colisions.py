import matplotlib.pyplot as plt
class Collisions:
    def __init__(self, app):
        self.app = app
        self.positions_models = ((-6.5, -6.4), (-8.4, -10.4), (-11.4, -10.4), (-9.9, -5.9), (-13.4, -6.4), (8.5, -6.3), (6.5, -10.3), (10.5, -10.3), (13.5, -11.3),
                                 (12.5, -6.3), (-1.95, -6.08), (-4.55, -8.52), (-4.45, -10.55), (-0.95, -9.46),
                                 (2.04, -10.00), (1.79, -13.90), (-2.03, -14.01), (4.03, -10.02))
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

class Collisions_two:
    def __init__(self, app):
        self.app = app
        self.positions_models = ((-1.95, -6.08), (0, 0))
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