import matplotlib.pyplot as plt
class Collisions:
    def __init__(self, app):
        self.app = app
        self.positions_models = ((50.20, 80.39), (90.92, -55.004))
        self.limits = 0.5
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