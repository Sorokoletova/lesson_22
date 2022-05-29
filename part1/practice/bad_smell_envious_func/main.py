# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume_cube(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_volume_cube(cube):
        return cube.get_volume_cube()
