import pygame
import requests
import sys
import os


def load_map():
    map_request = "http://static-maps.yandex.ru/1.x/?ll=37.621094,55.753605&spn=0.05,0.05&l=map"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


def main():
    pygame.init()
    running = True
    screen = pygame.display.set_mode((600, 450))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        map_file = load_map()
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    os.remove(map_file)


main()
