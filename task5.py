import random
import pygame
import time
import itertools

class Molecule:
    """
    This class represents a molecule in a simulation.

    Attributes
    -----------
    - radius: int, The radius of the molecule.
    - color: tuple, The color of the molecule represented as an RGB tuple.
    - speed: int, The speed of the molecule.
    - x: int, The x-coordinate of the molecule's position.
    - y: int, The y-coordinate of the molecule's position.
    - Kx: float, The horizontal movement direction coefficient.
    - Ky: float, The vertical movement direction coefficient.

    Methods
    --------
    - change(): Changes the position of the molecule based on its speed and direction coefficients.
    - move(): Moves the molecule according to its speed and direction coefficients.
    - show(win): Draws the molecule on the given Pygame window.
    - get(): Returns the x, y coordinates, and radius of the molecule.
    - connect(cor): Checks if the molecule collides with another molecule represented by the given coordinates and radius.
                    If a collision occurs, the molecule expands and moves.
    - expand(): Reverses the direction of the molecule's movement by negating its x and y coordinates.


    """
    colors = [(220, 20, 60), (255, 200, 255), (255, 215, 0), (255, 0, 255), (30, 144, 255)]
    def __init__(self):
        self.radius = random.randint(5, 20)
        self.color = random.choice(self.colors)
        self.speed = 1
        self.x = random.randint(0, 750)
        self.y = random.randint(0, 750)
        self.Kx = random.choice([3 / 5, -3 / 5, 1, -1])
        self.Ky = random.choice([3 / 5, -3 / 5, 1, -1])

    def change(self):
        """
        Changes the position of the molecule based on its speed and direction coefficients.
        """
        if self.x <= 0:
            self.Kx = self.Kx * (-1)
        if self.y <= 0:
            self.Ky = self.Ky * (-1)
        if self.x >= 800 - self.radius * 2:
            self.Kx = self.Kx * (-1)
        if self.y >= 900 - self.radius * 2:
            self.Ky = self.Ky * (-1)
        self.move()

    def move(self):
        """
        Moves the molecule according to its speed and direction coefficients.
        """
        self.x += self.speed * self.Kx
        self.y += self.speed * self.Ky

    def show(self, win):
        """
        Draws the molecule on the given Pygame window.
        """
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def get(self):
        """
        Returns the x, y coordinates, and radius of the molecule.
        """
        return self.x, self.y, self.radius

    def connect(self, cor):
        """
        Checks if the molecule collides with another molecule represented by the given coordinates and radius.
        If a collision occurs, the molecule expands and moves.
        """
        dx = self.x - cor[0]
        dy = self.y - cor[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance <= self.radius + cor[2]:  # Проверяем столкновение по расстоянию между центрами и радиусам
            self.expand()
            self.move()
            return True
        else:
            return False

    def expand(self):
        """
        Reverses the direction of the molecule's movement by negating its x and y coordinates.
        """
        self.x *= -1
        self.y *= -1


main_win = pygame.display.set_mode((800, 800))
main_win.fill((100, 100, 100))
flag = True

COUNT = 20
mas_mol = [Molecule() for i in range(COUNT)] # Создание списка молекул
while flag:
    pygame.time.delay(10) # Задержка для управления частотой обновления экрана
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    pygame.display.update()
    main_win.fill((100, 100, 100))

    for mol in mas_mol:  # Отображение и изменение положения каждой молекулы
        mol.show(main_win)
        mol.change()

    for par in itertools.combinations(mas_mol, 2): # Проверка наличия столкновений между молекулами
        if par[0].connect(par[1].get()):
            par[1].expand()
            par[1].move()