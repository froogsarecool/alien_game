# src/animation_controller.py

class AnimationController:
    def __init__(self, frames, speed=0.15):
        self.frames = frames
        self.speed = speed
        self.index = 0
        self.timer = 0

    def update(self):
        if not self.frames:
            return
        self.timer += self.speed
        if self.timer >= 1:
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)

    def get_image(self):
        if not self.frames:
            return None
        return self.frames[self.index]