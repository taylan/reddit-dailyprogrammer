from math import sqrt


class Particle:
    mass, x_pos, y_pos = 0, 0, 0

    def __init__(self, m, x, y):
        self.mass, self.x_pos, self.y_pos = m, x, y

    def calculate_repulsion(self, p2):
        dx = self.x_pos - p2.x_pos
        dy = self.y_pos - p2.y_pos
        dist = sqrt(dx**2 + dy**2)
        return (self.mass * p2.mass) / dist**2


def parse_particle(line):
    return Particle(*[float(val) for val in (line.split(' '))])

inp = open("input.txt").read().splitlines()

p1 = parse_particle(inp[0])
p2 = parse_particle(inp[1])

print("{0:.4f}".format(p1.calculate_repulsion(p2)))
