# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, field, state, x_coord, y_coord):
        self.field = field
        self.speed = 1
        self.state = state
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, direction):
        speed_move = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y_coord + speed_move, x=self.x_coord, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y_coord - speed_move, x=self.x_coord, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord - speed_move, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y_coord, x=self.x_coord + speed_move, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Что-то не то')


#     ...
