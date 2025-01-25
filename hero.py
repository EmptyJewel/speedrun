


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  
        self.hero = loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setH(180)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(-3, 3, 1.5)
        self.cameraOn = True

    
    def setup_parkour_objects(self):
        self.parkour_objects = []
        positions = [(5, 10, 0), (10, 20, 5), (15, 30, 10)]  # Позиції об'єктів
        for pos in positions:
            obj = loader.loadModel("models/block.egg")
            obj.setPos(*pos)
            obj.reparentTo(self.render)
            self.parkour_objects.append(obj)

    def check_grab(self):
        for obj in self.parkour_objects:
            if (self.character.getDistance(obj) < 2 and
                    abs(self.character.getZ() - obj.getZ()) < 2):
                self.character.setZ(obj.getZ() + 1)  # Підняти на рівень об'єкта

        
    def setup_collision(self):
        self.character_collider = CollisionNode("character")
        self.character_collider.addSolid(CollisionSphere(0, 0, 0.5, 0.5))
        self.character_collider_np = self.character.attachNewNode(self.character_collider)
        self.cTrav.addCollider(self.character_collider_np, self.collision_handler)

    
    def setup_camera(self):
        base.disableMouse()
        self.camera_distance = 10
    
    def update_camera(self, task):
        camera.lookAt(self.character)
        camera.setPos(self.character.getX(), self.character.getY() - self.camera_distance, self.character.getZ() + 5)
        return task.cont




