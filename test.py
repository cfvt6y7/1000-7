import pygame
import time

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

play_sound()
show_image_with_timer("Screenshot_12.png", 10)

