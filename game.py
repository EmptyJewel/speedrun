from direct.showbase.ShowBase import ShowBase


class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.map = self.load_and_display_model('tutorial.obj', 'tutprial.png', 0, 0, 0)  # Завантажуємо модель �� відображаємо на сцені
        self.map.setHpr(0,180,0)
        self.hero = self.load_and_display_model('playes.obj', 'playes.png', 0, 0, 0)  # розміщує героя в центрі карти

        # Встановлення поля зору камери на 90 градусів для ширшого огляду
        base.camLens.setFov(90)

    def load_and_display_model(self, model_path, texture_path, x, y, z):
        model = self.loader.loadModel(model_path)
        model.reparentTo(self.render)
        texture = self.loader.loadTexture(texture_path)
        model.setTexture(texture)
        model.setPos(x, y, z)
        return model
game = MyGame()
game.run()