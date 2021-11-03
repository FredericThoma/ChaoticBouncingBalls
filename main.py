#!/usr/bin/env python3
import pygame
import math


screen = pygame.display.set_mode((900, 900))
width = screen.get_width()
height = screen.get_height()
white = (255, 255, 255)
ball_r = 15
container_r = width / 2
g = 0.01


class Ball:
    def __init__(self, x, y, color):
        self.pos_x = x
        self.pos_y = y
        self.vel_x = 0
        self.vel_y = 0
        self.acc_x = 0
        self.acc_y = 1
        self.falling = True
        self.pos_arr = []
        self.count = 0
        self.color = color

    def show(self):
        pygame.draw.circle(screen, white, (self.pos_x, self.pos_y), ball_r)

    def update(self):
        self.count += 1
        if self.count % 5 == 0:
            self.pos_arr.append((self.pos_x, self.pos_y))
        self.vel_x += self.acc_x * g
        self.vel_y += self.acc_y * g
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        if len(self.pos_arr) > 1000:
            self.pos_arr = self.pos_arr[1:]
        for point in self.pos_arr:
            pygame.draw.circle(screen, self.color, point, 1)
        m_x = width / 2
        m_y = height / 2
        d_x = self.pos_x - m_x
        d_y = self.pos_y - m_y
        d_to_cont = math.sqrt(d_x ** 2 + d_y ** 2)
        if d_to_cont >= container_r - ball_r:
            v = math.sqrt(self.vel_x ** 2 + self.vel_y ** 2)
            angle_to_coll = math.atan2(-d_y, d_x)
            old_angle = math.atan2(-self.vel_y, self.vel_x)
            new_angle = 2 * angle_to_coll - old_angle
            self.vel_x = -v * math.cos(new_angle)
            self.vel_y = v * math.sin(new_angle)


def main():
    pygame.init()
    running = True
    ball = Ball(width // 2 + 1, height // 8, (0, 255, 0))
    ball_2 = Ball(width // 2 + 0.5, height // 8, (0, 0, 255))

    while running:

        screen.fill(0)
        pygame.draw.circle(screen, white, (height / 2, height / 2), height / 2)
        pygame.draw.circle(screen, (0, 0, 0), (height / 2, height / 2), height / 2 - 10)
        ball.show()
        ball_2.show()
        ball.update()
        ball_2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
