# pylint: disable=C0103
# Importing the pygame module
import pygame
from pygame.locals import *
import math
from PIL import Image


def calculate_images(window, image, size, left, top, num_rec):
    if num_rec == 1:
        window.blit(image, (left, top))
        return
    cropped1 = pygame.Surface((size, size))
    cropped1.blit(image, (0, 0), (0, 0, size, size))
    cropped2 = pygame.Surface((size, size))
    cropped2.blit(image, (0, 0), (0, size, size, size * 2))
    cropped3 = pygame.Surface((size, size))
    cropped3.blit(image, (0, 0), (size, 0, size * 2, size))
    cropped4 = pygame.Surface((size, size))
    cropped4.blit(image, (0, 0), (size, size, size * 2, size * 2))

    if num_rec == 2:
        calculate_images(
            window, cropped1, int(size / 2), left + counter, top, num_rec - 1
        )
        calculate_images(
            window, cropped2, int(size / 2), left, top + size - counter, num_rec - 1
        )
        calculate_images(
            window, cropped3, int(size / 2), left + size, top + counter, num_rec - 1
        )
        calculate_images(
            window,
            cropped4,
            int(size / 2),
            left + size - counter,
            top + size,
            num_rec - 1,
        )
        return
    calculate_images(window, cropped1, int(size / 2), left + size, top, num_rec - 1)
    calculate_images(window, cropped2, int(size / 2), left, top, num_rec - 1)
    calculate_images(
        window, cropped3, int(size / 2), left + size, top + size, num_rec - 1
    )
    calculate_images(window, cropped4, int(size / 2), left, top + size, num_rec - 1)


# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

image_pil = Image.open("fox.png")
width, height = image_pil.size
image_size = width
end = int(math.log2(image_size)) + 1
image = pygame.image.load("fox.png")

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((image_size, image_size))

# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Creating a boolean variable that
# we will use to run the while loop
run = True
counter = 0
split = 1
loop_counter = 0
time_to_split = False

# Creating an infinite loop
# to run our game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This would be a quit event.
            run = False  # So the user can close the program

    # Setting the framerate to 30fps
    clock.tick(30)

    # print(loop_counter, time_to_split, split, counter)
    # delays spinning for a few cycles
    if loop_counter == 50:
        time_to_split = True

    if time_to_split:
        split += 1
        counter += 1
        time_to_split = False
    elif not time_to_split and counter != 0:
        counter += 1

    calculate_images(window, image, int(image_size / 2), 0, 0, split)

    loop_counter += 1
    # Updating the display surface
    pygame.display.update()

    if counter == 2 ** (end - split):
        time_to_split = True
        counter = 0
        if split == end:
            split = 1
            # rotating 90 degrees clockwise
            image = pygame.transform.rotate(image, -90)

    # Filling the window with black color
    window.fill((0, 0, 0))

pygame.quit()
