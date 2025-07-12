import time
import random
from PIL import Image
import pygame
import threading
import os

def slow_print(text, delay=0.1):
    for char_in_text in text:
        print(char_in_text, end="", flush=True)
        time.sleep(delay)

def tocka():
    for i in range(3):
        slow_print(". ", delay=0.5)
    return ""

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("saund.mp3")
    pygame.mixer.music.play()

def show_image_with_timer(image_path, duration=10):
    pygame.init()
    img = pygame.image.load(image_path)
    width, height = img.get_size()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Image Display")

    screen.blit(img, (0, 0))
    pygame.display.flip()

    start_time = time.time()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if time.time() - start_time > duration:
            running = False

        pygame.time.Clock().tick(30)

    pygame.quit()

x = 1000
while x > 0:
    y = x
    x -= 7

    slow_print(f"{y} - 7 = {x} ", delay=0.3)
    tocka()

    if random.randint(1, 5) == 1:
        play_sound()
        show_image_with_timer("Screenshot_12.png", 10)

    print()
    time.sleep(0.05)
