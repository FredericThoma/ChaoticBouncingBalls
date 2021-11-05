#!/usr/bin/env python3
import pygame
from simple_vect import *

pygame.init()
screen = pygame.display.set_mode((900, 900))
g = 0.01


class Ball:
    def __init__(self, x, y, color):
        self.pos = Vect(x, y)
        self.vel = Vect(0, 0)
        self.acc = Vect(0, 1)
        self.color = color
        self.r = 25

    def show(self):
        pygame.draw.circle(screen, self.color, self.pos.to_tuple(), self.r)

    def update(self, container_r, center: Vect):
        self.vel += self.acc.multiply(g)
        self.pos += self.vel
        direction = self.pos - center
        dist_to_center = mag(direction)
        if dist_to_center < container_r - self.r:
            return
        else:
            self.handle_collision(direction)

    def handle_collision(self, direction: Vect):
        v = mag(self.vel)
        collision_angle = math.atan2(-direction[1], direction[0])
        old_angle = math.atan2(-self.vel[1], self.vel[0])
        new_angle = 2 * collision_angle - old_angle
        new_vel_x = -v * math.cos(new_angle)
        new_vel_y = v * math.sin(new_angle)
        self.vel = Vect(new_vel_x, new_vel_y)
        self.pos += self.vel

    def get_pos(self):
        return self.pos.to_tuple()


def main():
    width = screen.get_width()
    height = screen.get_height()
    ball_1 = Ball(width // 2 - 5, height // 8, (0, 255, 0))
    ball_2 = Ball(ball_1.pos[0] + 0.1, ball_1.pos[1], (0, 0, 255))  # Initial position very close to ball_1
    container_r = width // 2
    center = Vect(width // 2, height // 2)
    running = True
    counter = 0
    prev_ball_positions = []
    while running:
        screen.fill(0)
        pygame.draw.circle(screen, (255, 255, 255), center.to_tuple(), container_r)
        pygame.draw.circle(screen, (0, 0, 0), center.to_tuple(), container_r - 10)
        ball_1.update(container_r, center)
        ball_2.update(container_r, center)
        if counter % 5 == 0:
            prev_ball_positions = update_prev_ball_positions(prev_ball_positions, ball_1, ball_2)
        draw_prev_positions(prev_ball_positions)
        ball_1.show()
        ball_2.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        pygame.display.flip()
        counter += 1


def draw_prev_positions(prev_bp):
    for index, pos in enumerate(prev_bp):
        color = (0, 255, 0, 100) if index % 2 == 0 else (0, 0, 255, 100)
        pygame.draw.circle(screen, color, pos, 1)


def update_prev_ball_positions(prev_bp, b1, b2):
    prev_bp.append(b1.get_pos())
    prev_bp.append(b2.get_pos())
    return prev_bp if len(prev_bp) < 1000 else prev_bp[2:]


if __name__ == '__main__':
    main()
