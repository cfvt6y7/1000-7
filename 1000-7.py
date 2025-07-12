import time
import random
from PIL import Image
import pygame
import threading
import os

pygame.mixer.init()

def slow_print(text, delay=0.1):
    for char_in_text in text:
        print(char_in_text, end="", flush=True)
        time.sleep(delay)

def tocka():
    for i in range(3):
        slow_print(". ", delay=0.5)
    return ""

def show_image_pygame_and_close(image_path, display_time_seconds=3):
    try:
        pygame.display.init()
        image = pygame.image.load(image_path)
        image_width, image_height = image.get_size()
        screen = pygame.display.set_mode((image_width, image_height))
        pygame.display.set_caption("1000-7") # Название окна
        screen.blit(image, (0, 0))
        pygame.display.flip()
        time.sleep(display_time_seconds)
        pygame.display.quit()

    except pygame.error as e:
        print(f"Ошибка Pygame при загрузке или отображении картинки: {e}")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{image_path}' не найден.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def play_sound():
    pygame.mixer.music.load("saund.mp3")
    pygame.mixer.music.play()

x = 1000
while x > 0:
    y = x
    x -= 7

    slow_print(f"{y} - 7 = {x} ", delay=0.3)
    tocka()

    if random.randint(1, 5) == 1:

        threading.Thread(target=show_image_pygame_and_close, args=("Screenshot_12.png", 17)).start()

        threading.Thread(target=play_sound).start()

    print()
    time.sleep(0.05)