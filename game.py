import arcade


# Главное окно игрового поля
class Game(arcade.Window):
    def on_draw(self):  # Метод отвечает за отрисовку элементов окна
        self.clear((255, 255, 255))  # Методом clear перезаливаем задний фон в белый


if __name__ == '__main__':
    window = Game()
    arcade.run()
