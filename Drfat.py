from direct.showbase.ShowBase import ShowBase


class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

    # Завантаження моделі, застосування текстури, встановлення позиції та обертання
    def load_and_display_model(self, model_path, texture_path, x, y, z, h, p, r):
        """Завантажує модель, застосовує текстуру, встановлює позицію та обертання"""

        # Завантаження моделі
        model = self.loader.loadModel(model_path)
        model.reparentTo(self.render)  # Додаємо модель до сцени

        # Завантаження текстури та застосування її до моделі
        texture = self.loader.loadTexture(texture_path)
        model.setTexture(texture)

        # Встановлення позиції (x, y, z)
        model.setPos(x, y, z)

        # Встановлення обертання (h, p, r)
        # h - обертання по осі Y (горизонтальне)
        # p - обертання по осі X (вертикальне)
        # r - обертання по осі Z (плоске)
        model.setHpr(h, p, r)

        # Повертаємо модель для подальшого використання
        return model


# Запуск гри
game = MyGame()

# Викликаємо метод для завантаження і відображення моделі
# Вказуємо шлях до моделі, текстури, координати та обертання
model = game.load_and_display_model("tutorial.obj","tutorial.png",-3, 3, 1.5, 180, 90, -90)  # Позиція (0, 10, 0), обертання (90, 0, 0)
model2 = game.load_and_display_model("playes.obj","playes.png",0, 0, -2.2, 180, 90, 0)  # Позиція (0, 10, 0), обертання (90, 0, 0)

game.run()
