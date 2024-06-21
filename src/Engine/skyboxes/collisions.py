class Collisions:
    def _init_(self, app):
        self.app = app
        self.positions_models = ((-9.27, -0.04), (0.38, -11.14), (9.45, 0.02), (0.41, 9.68),
                                 (0.41, 20.68), (0.37, -24.04), (-18.71, 9.63),(-19.34, -8.94),
                                 (19.15, -8.17), (19.16, 9.80))
        self.limits = (0.5, 0.5)
    def check_limits(self):
        print(self.app.position)
        collisionFound = True
        length_positions = len(self.positions_models)
        for i in range(length_positions):
            bool_x = self.positions_models[i][0] - self.limits[0] < self.app.x < self.positions_models[i][0] + self.limits[0]
            bool_z = self.positions_models[i][1] - self.limits[0] < self.app.z < self.positions_models[i][1] + self.limits[0]
            if bool_x and bool_z:
                collisionFound = False
                break
        if collisionFound:
            return True
        else:
            return False


# finished