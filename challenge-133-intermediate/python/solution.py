def enum(**enums): # Stolen from http://stackoverflow.com/a/1695250/36938
    return type('Enum', (), enums)

PropagationDirection = enum(UP=1, DOWN=2, RIGHT=3, LEFT=4)

class Particle:
    x, y, rng = 0, 0, 0
    name = ''
    prop_dirs = None
    is_active = False

    def __init__(self, x_pos=None, y_pos=None, range=None, name=None, *prop_dirs):
        self.x, self.y, self.rng, self.name, self.prop_dirs = x_pos, y_pos, range, name, list(prop_dirs)

    def __str__(self):
        return 'X' if self.is_active else self.name


def get_prop_directions(s):
    dirs = [('u', PropagationDirection.UP), ('d', PropagationDirection.DOWN), ('r', PropagationDirection.RIGHT), ('l', PropagationDirection.LEFT)]
    return [dir[1] for dir in dirs if dir[0] in s.lower()]


def get_particles(lines):
    i = 0
    names = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for line in lines:
        tokens = line.split(' ')
        i += 1
        yield Particle(int(tokens[0]), int(tokens[1]), int(tokens[2]), names[i], *get_prop_directions(tokens[3]))


def print_grid(grid, caption=''):
    if caption:
        print(caption)

    for row in grid:
        print("".join([str(cell) if cell is not None else '•' for cell in row]))
    print()


def initialize_grid(size, particles):
    grid = []
    for y in list(range(size)):
        grid.append([None for x in list(range(size))])

    for p in particles:
        grid[p.y][p.x] = p

    return grid


def get_target_coordinates(p, grid):
    grid_size = len(grid)
    target_coords = []
    if PropagationDirection.UP in p.prop_dirs:
        target_coords.extend([(p.x, y) for y in [y_coord for y_coord in range(p.y, p.y - p.rng, -1) if y_coord > 0]])
    if PropagationDirection.DOWN in p.prop_dirs:
        target_coords.extend([(p.x, y) for y in [y_coord for y_coord in range(p.y, p.y + p.rng) if y_coord < grid_size]])
    if PropagationDirection.LEFT in p.prop_dirs:
        target_coords.extend([(x, p.y) for x in [x_coord for x_coord in range(p.x, p.x - p.rng, -1) if x_coord > 0]])
    if PropagationDirection.RIGHT in p.prop_dirs:
        target_coords.extend([(x, p.y) for x in [x_coord for x_coord in range(p.x, p.x + p.rng) if x_coord < grid_size]])
    return target_coords


def react(p, grid):
    for coord in get_target_coordinates(p, grid):
        particle = grid[coord[1]][coord[0]]
        if particle is not None:
            particle.is_active = True


def do_step(particles, grid):
    if len([p for p in particles if p.is_active]) == 0:
        particles[0].is_active = 1
        return

    [react(active_particle, grid) for active_particle in [p for p in particles if p.is_active]]


def main():
    inp = open('input.txt').read().splitlines()
    grid_size = int(inp[0].split(' ')[1])
    particles = list(get_particles([line for line in inp[1:]]))
    grid = initialize_grid(grid_size, particles)
    print_grid(grid, caption='Step 0')

    step_count = 0
    pending_particle_count = len(particles) - 1
    while True:
        step_count += 1
        do_step(particles, grid)
        inactive_particle_count = len([p for p in particles if not p.is_active])
        print_grid(grid, caption="Step {0}".format(step_count))

        if inactive_particle_count == 0 or step_count == pending_particle_count:
            break


if __name__ == "__main__":
    main()