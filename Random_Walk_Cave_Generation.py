#ref：http://www.roguebasin.com/index.php?title=Random_Walk_Cave_Generation
import random

class Random_Walk_Cave:
    def generate(self, width, height, max_count):
        map_data = [['#' for w in range(width)] for h in range(height)]
        count = 1
        init_x = width//2
        init_y = height//2
        map_data[init_y][init_x]
        curr_x = init_x
        curr_y = init_y
        next_x = None
        next_y = None

        while count < max_count:
            next_x, next_y = self.take_one_step(curr_x, curr_y, width, height)
            if map_data[next_y][next_x] == '#':
                map_data[next_y][next_x] = '.'
                count = count + 1
            curr_x, curr_y = next_x, next_y

        return map_data
            

    def take_one_step(self, x, y, width, height):
        if random.choice(['x','y']) == 'x':
            x = x + random.choice([-1, 1])
            if x < 1:
                x = 1
            if x > width - 2:
                x = width - 2
            y = y
        else:
            x = x
            y = y + random.choice([-1, 1])
            if y < 1:
                y = 1
            if y > height - 2:
                y = height - 2
        return x, y

if __name__ == '__main__':
    width = 50
    height = 25
    count = 400
    cave = Random_Walk_Cave()
    map_data = cave.generate(width, height, count)
    for y in range(height):
        for x in range(width):
            print(map_data[y][x], end='')
        print()

'''
##################################################
######################.........####......#########
######################.........####.....##########
####################...........#........##########
#####################.........##........##########
######################........###..##...##########
########################.#....#....#...###########
########################......#....#..############
#########################.....#.......############
##########.#############........#....#############
########....############.##.......#.##############
######....#.####...#####.....#.....###############
######...#.......#..###......#......##############
######...#####...##...#..#.....##..#....##########
#####...######...##.....#................#########
####.....#####.#.##....##.....#....#.......#######
####.....##########.#..##...####..###.........####
###....##################.#.#####..##..#......####
###..####################.....#........##...######
###..##################....##...............######
##...##################....###.......#.....#######
#....###....#############.####.......#.....#######
#....##....#####################..#####...########
#.......#########################.#####...########
##################################################
'''
