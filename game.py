import arcade

# Константы (определяются заглавными)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.08)
        self.change_x = 1
        # self.change_y = -1

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 1.0)  # передаём в родительский init картинку и её масштаб


# Главное окно игрового поля
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)  # передаём в родительский init высоту, ширину и название окна
        self.bar = Bar()  # создаём ракетку
        self.ball = Ball()  # создаём мячик
        self.setup()

    # создаём метод отвечающий за положение элементов в игре
    def setup(self):  # setup не является методом родителя (arcade), поэтому мы должны его вызвать дополнительно
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):  # Метод отвечает за отрисовку элементов окна
        self.clear((255, 255, 255))  # Методом clear перезаливаем задний фон (в данном случае в белый)
        self.bar.draw()  # отрисовываем ракетку в игровом окне
        self.ball.draw()  # отрисовываем мячик в игровом окне

    def update(self, delta):
        self.ball.update()


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
