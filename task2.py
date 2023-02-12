import pygame
import requests
import sys
import os


def load_map(scale):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll=37.621094,55.753605&spn={scale},{scale}&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file, scale


def main():
    pygame.init()
    running = True
    screen = pygame.display.set_mode((600, 450))
    scale = 1
    while running:
        map_file, scale = load_map(scale)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if 0.01 <= (scale + 8) <= 50:
                        map_file, scale = load_map(scale + 8)

                elif event.key == pygame.K_UP:
                    if 0.01 <= (scale - 8) <= 50:
                        map_file, scale = load_map(scale - 8)

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    os.remove(map_file)


main()
