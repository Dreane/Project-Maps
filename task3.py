import pygame
import requests
import sys
import os


def load_map(scale, pos_x, pos_y):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={pos_x},{pos_y}&spn={scale},{scale}&l=map"
    response = requests.get(map_request)
    print(scale)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file, scale, pos_x, pos_y


def main():
    pygame.init()
    running = True
    screen = pygame.display.set_mode((600, 450))

    scale = 1
    d_scale = 8
    pos_x = 38.621094
    pos_y = 55.753605
    d_pos = 2

    while running:
        map_file, scale, pos_x, pos_y = load_map(scale, pos_x, pos_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEDOWN:
                    if 0.01 <= (scale + d_scale) <= 50:
                        map_file, scale, pos_x, pos_y = load_map(scale + d_scale, pos_x, pos_y)
                if event.key == pygame.K_PAGEUP:
                    if 0.01 <= (scale - d_scale) <= 50:
                        map_file, scale, pos_x, pos_y = load_map(scale - d_scale, pos_x, pos_y)
                if event.key == pygame.K_UP:
                    if 30 <= pos_y + d_pos <= 80:
                        map_file, scale, pos_x, pos_y = load_map(scale, pos_x, pos_y + d_pos)
                if event.key == pygame.K_RIGHT:
                    if 20 <= pos_x + d_pos <= 50:
                        map_file, scale, pos_x, pos_y = load_map(scale, pos_x + d_pos, pos_y)
                if event.key == pygame.K_DOWN:
                    if 30 <= pos_y - d_pos <= 80:
                        map_file, scale, pos_x, pos_y = load_map(scale, pos_x, pos_y - d_pos)
                if event.key == pygame.K_LEFT:
                    if 20 <= pos_x - d_pos <= 50:
                        map_file, scale, pos_x, pos_y = load_map(scale, pos_x - d_pos, pos_y)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    os.remove(map_file)


main()
