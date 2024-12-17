from copy import deepcopy

input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    robots = []
    for line in input_data:
        # p=0,4 v=3,-3
        pos, vel = line.split()
        pos_x, pos_y = pos.strip().split("=")[-1].strip().split(",")
        vel_x, vel_y = vel.strip().split("=")[-1].strip().split(",")
        robots.append(Robot(int(pos_x), int(pos_y), int(vel_x), int(vel_y)))

    return robots


def create_grid(height, width):
    return [["." for _ in range(width)] for _ in range(height)]


class Robot:
    def __init__(self, start_x, start_y, vel_x, vel_y):
        self.start_x = start_x
        self.start_y = start_y
        self.pos_x = start_x
        self.pos_y = start_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def move(self, steps=1):
        self.pos_x += self.vel_x * steps
        self.pos_y += self.vel_y * steps

    def __repr__(self):
        return f"Robot(start={self.start_x}, {self.start_y}, cur={self.pos_x}, {self.pos_y}, vel={self.vel_x}, {self.vel_y})"


def move_robots(robots, moves):
    for robot in robots:
        robot.move(moves)


def visualise_grid(grid):
    for g in grid:
        print("".join([str(x) for x in g]))


def place_robots(grid, robots):
    new_grid = deepcopy(grid)
    # visualise_grid(new_grid)
    for robot in robots:
        # print(robot)
        x = abs(robot.pos_x % len(new_grid[0]))
        y = abs(robot.pos_y % len(new_grid))
        # print(y, x)
        cur = new_grid[y][x]
        new_num = 1 if cur == "." else cur + 1
        new_grid[y][x] = new_num
        # visualise_grid(new_grid)

    return new_grid


def calculate_safety_factor(grid):
    mid_h = int(len(grid) / 2)
    mid_w = int(len(grid[0]) / 2)
    quads = [
        [[0 if w == "." else w for w in h[:mid_w]] for h in grid[:mid_h]],
        [[0 if w == "." else w for w in h[mid_w+1:]] for h in grid[:mid_h]],
        [[0 if w == "." else w for w in h[:mid_w]] for h in grid[mid_h+1:]],
        [[0 if w == "." else w for w in h[mid_w+1:]] for h in grid[mid_h+1:]],
    ]
    total_safety = 1
    for quad in quads:
        total_safety *= sum([sum(r) for r in quad])

    return total_safety


def main():
    moves = 100
    height = 103
    width = 101
    robots = parse_input(get_input_data())
    grid = create_grid(height, width)
    visualise_grid(grid)
    move_robots(robots, moves)

    grid = place_robots(grid, robots)
    visualise_grid(grid)

    print("Total Safety Factor:", calculate_safety_factor(grid))


if __name__ == '__main__':
    main()