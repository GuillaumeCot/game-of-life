import random


def glider_gun(grid, x, y):
    grid[x + 1][y + 5] = 1
    grid[x + 1][y + 6] = 1
    grid[x + 2][y + 5] = 1
    grid[x + 2][y + 6] = 1
    grid[x + 11][y + 5] = 1
    grid[x + 11][y + 6] = 1
    grid[x + 11][y + 7] = 1
    grid[x + 12][y + 4] = 1
    grid[x + 12][y + 8] = 1
    grid[x + 13][y + 3] = 1
    grid[x + 13][y + 9] = 1
    grid[x + 14][y + 3] = 1
    grid[x + 14][y + 9] = 1
    grid[x + 15][y + 6] = 1
    grid[x + 16][y + 4] = 1
    grid[x + 16][y + 8] = 1
    grid[x + 17][y + 5] = 1
    grid[x + 17][y + 6] = 1
    grid[x + 17][y + 7] = 1
    grid[x + 18][y + 6] = 1
    grid[x + 21][y + 3] = 1
    grid[x + 21][y + 4] = 1
    grid[x + 21][y + 5] = 1
    grid[x + 22][y + 3] = 1
    grid[x + 22][y + 4] = 1
    grid[x + 22][y + 5] = 1
    grid[x + 23][y + 2] = 1
    grid[x + 23][y + 6] = 1
    grid[x + 25][y + 1] = 1
    grid[x + 25][y + 2] = 1
    grid[x + 25][y + 6] = 1
    grid[x + 25][y + 7] = 1
    grid[x + 35][y + 3] = 1
    grid[x + 35][y + 4] = 1
    grid[x + 36][y + 3] = 1
    grid[x + 36][y + 4] = 1


def glider(grid, x, y):
    grid[x + 0][y + 1] = 1
    grid[x + 1][y + 2] = 1
    grid[x + 2][y + 0] = 1
    grid[x + 2][y + 1] = 1
    grid[x + 2][y + 2] = 1


def blinker(grid, x, y):
    grid[x + 0][y + 1] = 1
    grid[x + 1][y + 1] = 1
    grid[x + 2][y + 1] = 1


def beacon(grid, x, y):
    grid[x + 0][y + 0] = 1
    grid[x + 0][y + 1] = 1
    grid[x + 1][y + 0] = 1
    grid[x + 1][y + 1] = 1
    grid[x + 2][y + 2] = 1
    grid[x + 3][y + 3] = 1
    grid[x + 3][y + 4] = 1
    grid[x + 4][y + 3] = 1
    grid[x + 4][y + 4] = 1


def pulsar(grid, x, y):
    grid[x + 2][y + 0] = 1
    grid[x + 3][y + 0] = 1
    grid[x + 4][y + 0] = 1
    grid[x + 8][y + 0] = 1
    grid[x + 9][y + 0] = 1
    grid[x + 10][y + 0] = 1
    grid[x + 0][y + 2] = 1
    grid[x + 5][y + 2] = 1
    grid[x + 7][y + 2] = 1
    grid[x + 12][y + 2] = 1
    grid[x + 0][y + 3] = 1
    grid[x + 5][y + 3] = 1
    grid[x + 7][y + 3] = 1
    grid[x + 12][y + 3] = 1
    grid[x + 0][y + 4] = 1
    grid[x + 5][y + 4] = 1
    grid[x + 7][y + 4] = 1
    grid[x + 12][y + 4] = 1
    grid[x + 2][y + 5] = 1
    grid[x + 3][y + 5] = 1
    grid[x + 4][y + 5] = 1
    grid[x + 8][y + 5] = 1
    grid[x + 9][y + 5] = 1
    grid[x + 10][y + 5] = 1
    grid[x + 2][y + 7] = 1
    grid[x + 3][y + 7] = 1
    grid[x + 4][y + 7] = 1
    grid[x + 8][y + 7] = 1
    grid[x + 9][y + 7] = 1
    grid[x + 10][y + 7] = 1
    grid[x + 0][y + 8] = 1
    grid[x + 5][y + 8] = 1
    grid[x + 7][y + 8] = 1
    grid[x + 12][y + 8] = 1
    grid[x + 0][y + 9] = 1
    grid[x + 5][y + 9] = 1
    grid[x + 7][y + 9] = 1
    grid[x + 12][y + 9] = 1
    grid[x + 0][y + 10] = 1
    grid[x + 5][y + 10] = 1
    grid[x + 7][y + 10] = 1
    grid[x + 12][y + 10] = 1
    grid[x + 2][y + 12] = 1
    grid[x + 3][y + 12] = 1
    grid[x + 4][y + 12] = 1
    grid[x + 8][y + 12] = 1
    grid[x + 9][y + 12] = 1
    grid[x + 10][y + 12] = 1
    grid[x + 2][y + 13] = 1
    grid[x + 3][y + 13] = 1
    grid[x + 4][y + 13] = 1
    grid[x + 8][y + 13] = 1
    grid[x + 9][y + 13] = 1
    grid[x + 10][y + 13] = 1
    grid[x + 2][y + 14] = 1
    grid[x + 3][y + 14] = 1
    grid[x + 4][y + 14] = 1
    grid[x + 8][y + 14] = 1
    grid[x + 9][y + 14] = 1
    grid[x + 10][y + 14] = 1


def pentadecathlon(grid, x, y):
    grid[x + 0][y + 1] = 1
    grid[x + 1][y + 1] = 1
    grid[x + 2][y + 0] = 1
    grid[x + 2][y + 1] = 1
    grid[x + 2][y + 2] = 1
    grid[x + 2][y + 3] = 1
    grid[x + 2][y + 4] = 1
    grid[x + 2][y + 5] = 1
    grid[x + 2][y + 6] = 1
    grid[x + 1][y + 7] = 1
    grid[x + 0][y + 7] = 1


def randomize_grid(grid: list[list[int]]):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = random.choice([0, 1])
