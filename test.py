from PIL import Image
import pygame

def show_image():
    img = Image.open("Screenshot_12.png")
    img.show()

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("saund.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

show_image()
play_sound()
