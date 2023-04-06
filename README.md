# Chrome_Dino_Bot

The genesis of this project was a programming challenge I participated in during my Undergraduate work placement. We were asked to automate the Chrome Dino game, and the solution with the highest average score after 10 runs would win. The rules were straightforward; anything goes so long as the game is not tampered with.

There were ten teams of two, my teammate [@LukeCanny](https://github.com/lukecanny) and I ended up coming second with a 10-run average of over 30,000 points. Our solution was based on the same principles as this project, with a bit of a jankier and less refined approach. We had a day to work on it and another day to test it. The highest score this program has been able to achieve thus far is just over 90,000.

![high score](https://user-images.githubusercontent.com/74914758/230424167-f5b935c8-e226-4983-9fe7-3cce3ec3d5a7.png)

# How it works

The program works using image processing. Each cycle, a screenshot of the game area is taken and checked for obstacles ahead of the Dino. It does this by searching a line of pixels starting just in front of the Dino and out to a predefined search distance. The program loops through this line of pixels, starting from the furthest pixel from the Dino to the closest. If a pixel is determined to be a different colour from the background, it's considered an obstacle, and the Dino will react accordingly. The search distance is increased over time so that the Dino reacts quicker and quicker as the game difficulty increases.

# Setup

First, the following packages are required:
* PyAutoGUI
* Keyboard

When these are installed, PyAutoGUI can also be used to gather screen coordinates using Command Prompt, like so:

![mouse coord](https://user-images.githubusercontent.com/74914758/230338759-ed858016-5e44-406a-83cf-3a8711fd6e4e.png)

#

Next, it's important to understand the variables used by the program so that they can be altered to suit your setup. The following are the variables used to determine the game area:
* top - how far down from the top of the screen the top of the game area will begin
* left - how far to the left the game area should start (almost always 0 when fullscreened)
* width - the total width of the game area (almost always the monitor width when fullscreened)
* height - the height of the game area (top + height = total distance from the top of the screen)
* sky_colour - a pixel that only changes when the sky colour changes

The screenshot below represents the game area as described using the above variables. These variables are entirely dependent on monitor resolution and must be changed on a case-by-case basis. The program was written on my work laptop with a screen resolution of 1920x1080. However, factors such as: resolution scaling or a bookmark bar can throw the program off. It's best to use PyAutoGUI to determine the game area for your own setup prior to running.

![boundaries](https://user-images.githubusercontent.com/74914758/230321719-cec97d9b-89b1-4d88-9da5-8ef4f199746f.png)

#

When the game area has been defined, it can now be searched for obstacles. The program does this using the following variables:
* search_x - where to stop searching
* search_dist - where to start searching
* cacti_y - the height at which to search for cacti (and low birds) as defined from the top of the game area
* birds_y - the height at which to search for birds as defined from the top of the game area

The screenshot below gives an approximation as to how the program interprets these variables. Obviously, the actual line being searched is only a single pixel wide.

![search_dist](https://user-images.githubusercontent.com/74914758/230338771-98d1a4f8-f8a3-4835-a470-80fa1fd09fb8.png)

It's important that search_x is placed relativly close to the Dino; I've found that a 15-20 pixel gap works well. When search_x has been defined, search_dist should be defined as the point furthest from the Dino where the Dino can jump and still avoid each kind of cacti. Setting search_dist too low will result in the Dino reacting too late and jumping into cacti, setting it too high too early will result in the Dino jumping too early and landing on top of cacti.

Every machine is different, so it will take some time to dial in these variables to get the best results. The best approach I've found is to just run the prorgram and see where it trips up. If the Dino jumps from too far back, too early, then the search_dist is too far. If later in the game the Dino is only just barely jumping in time, then the search_dist is too short (or is taking too long to increase).

# Run

Running the program is very straight forward. Ensure the official version of the Chrome Dino game is open and ready to go in your browser (navigate to chrome://dino/). Then run chrome_dino_bot.py, switch to the browser and click on the browser window to so that it is active. You'll know after the first cactus if it's working or not. When you want the program to stop, just press the escape key.

Bear in mind that the program uses a timer to determine the game speed, so simply restarting the game after a game over will result in the program continuing to assume the game is running at a higher speed. Every time the game restarts, the program must also be restarted.
