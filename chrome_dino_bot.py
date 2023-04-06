import pyautogui as gui
import keyboard as key
import time
import math

top, left, width, height = 293, 0, 1920, 437                # Define the game area
previous_second, current_second = 0, 0                      # Define timing variables
search_x, search_dist = 435, 520                            # Define the search distance (from search_x to search_dist)
cacti_y, birds_y = 350, 275                                 # Define the heights at which to search for obstacles

# Function that takes in an image and searches it for obstacles
def search(image):                                          
    for x in reversed(range(search_x, search_dist)):        # Loop through each pixel of the search distance in reverse order (furthest pixel from the Dino to the closest)
        if image.load()[x, cacti_y] != sky_colour:          # If there is a pixel that does not match the colour of the sky in the height range of cacti
            key.release('down')                             # Stop crouching
            key.press('up')                                 # Jump to avoid the obstacle
            break                                           # Stop searching
        elif image.load()[x, birds_y] != sky_colour:        # Otherwise, if there is an obstacle in the height range of birds
            key.press('down')                               # Crouch to avoid the obstacle
            break                                           # Stop searching
    return

# Wait a second to allow the user to start the game
time.sleep(1)
while key.is_pressed('esc') == False:                       # Loop indefinitely until the escape key is pressed
    current_time = time.time()                              # Note the current time
    if math.floor(current_second) != previous_second:       # If the current second, rounded down, does not match the previous second, a second has passed
        if search_dist < 1200:                              # If the search distance is less than 1200 pixels
            search_dist += 4                                # Increase the current search distance by 4 pixels
        previous_second = math.floor(current_second)        # Set previous_second to the current_second, rounded down
    image = gui.screenshot(region=(left,top,width,height))  # Take a screenshot of the previously defined game area
    sky_colour = image.load()[30, 435]                      # Note the sky colour
    search(image)                                           # Search the game area for upcoming obstacles
    current_second += time.time() - current_time            # Set the current second by comparing the current time to the previous 'current' time