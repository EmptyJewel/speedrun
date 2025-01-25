from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3  # Для роботи з векторами
from panda3d.core import WindowProperties  # Для обробки миші
from panda3d.core import CollisionTraverser, CollisionNode, CollisionSphere, CollisionHandlerQueue
from panda3d.core import globalClock


class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # Сховати курсор миші
        props = WindowProperties()
        props.setCursorHidden(True)
        self.win.requestProperties(props)
        # Завантаження моделі гравця
        self.car = self.loader.loadModel("playes.obj")  # Завантаження вашої 3D-моделі
        self.car.reparentTo(self.render)  # Прив'язка моделі до сцени
        self.car.setScale(0.2)  # Задаємо масштаб гравця
        self.car.setPos(0, 0, 0)  # Встановлюємо початкову позицію гравця
        # Додавання камери для слідкування за гравцем
        self.camera.reparentTo(self.player)  # Камера слідкує за гравцем
        self.camera.setPos(0, -10, 2)  # Камера розташована позаду гравця
        # Встановлення швидкості руху і поворотів
        self.speed = Vec3(0, 0, 0)  # Початкова швидкість
        self.mouse_sensitivity = 0.2  # Чутливість миші
        # Прив'язка клавіш для управління
        self.accept("w", self.move_forward)    # Вперед
        self.accept("w-up", self.stop_moving)  # Зупинка після відпускання
        self.accept("s", self.move_backward)   # Назад
        self.accept("s-up", self.stop_moving)
        self.accept("a", self.strafe_left)     # Ліво
        self.accept("a-up", self.stop_strafing)
        self.accept("d", self.strafe_right)    # Право
        self.accept("d-up", self.stop_strafing)
        # Оновлення положення гравця кожен кадр
        self.taskMgr.add(self.update_position, "UpdatePosition")
        self.taskMgr.add(self.update_mouse, "UpdateMouse")
    # Функції для управління рухом
    def move_forward(self):
        self.speed.setY(5)  # Рух вперед з певною швидкістю
    def move_backward(self):
        self.speed.setY(-5)  # Рух назад
    def strafe_left(self):
        self.speed.setX(-5)  # Рух ліворуч
    def strafe_right(self):
        self.speed.setX(5)  # Рух праворуч
    def stop_moving(self):
        self.speed.setY(0)  # Зупинка вперед/назад
    def stop_strafing(self):
        self.speed.setX(0)  # Зупинка руху ліворуч/праворуч
    # Обробка руху мишкою
    def update_mouse(self, task):
        # Отримання позиції курсора
        mouse_data = self.win.getPointer(0)
        mouse_x = mouse_data.getX()
        mouse_y = mouse_data.getY()
        # Обчислення повороту персонажа
        if self.win.movePointer(0, self.win.getXSize() // 2, self.win.getYSize() // 2):
            delta_x = (mouse_x - self.win.getXSize() // 2) * self.mouse_sensitivity
            self.car.setH(self.car.getH() - delta_x)
        return task.cont
    # Оновлення позиції гравця
    def update_position(self, task):
        dt = globalClock.getDt()  # Час між кадрами
        # Переміщення вперед/назад та ліворуч/праворуч
        forward_vector = self.car.getQuat().getForward() * self.speed.getY() * dt
        right_vector = self.car.getQuat().getRight() * self.speed.getX() * dt
        movement_vector = forward_vector + right_vector
        self.car.setPos(self.car.getPos() + movement_vector)

        return task.cont  # Продовжуємо виконання задачі

# Запуск гри
game = MyGame()
game.run()
