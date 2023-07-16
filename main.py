import time
import pyautogui
from pynput import mouse
import logging
import threading

# Configure logging
logging.basicConfig(filename='capture_coordinates.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create an empty list to store the coordinates
coordinates = []

# Function to get the coordinates on mouse click
def on_click(x, y, button, pressed):
    if pressed:
        coordinates.append((x, y))
        if len(coordinates) == 2:
            logging.info(f"Point 1: {coordinates[0]}")
            logging.info(f"Point 2: {coordinates[1]}")
            listener.stop()
            proceed()

# Function to proceed after capturing the second point
def proceed():
    # Get the x and y coordinates of the two points
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    # Define the delay between each iteration
    delay = 3.5

    # Iterate the process 39 times
    for _ in range(39):
        # Move to the first point
        pyautogui.moveTo(x1, y1, duration=0.5)

        # Double-click at the first point
        pyautogui.doubleClick()

        # Move to the second point
        pyautogui.moveTo(x2, y2, duration=0.5)

        # Double-click at the second point
        pyautogui.doubleClick()

        # Wait for the specified delay
        time.sleep(delay)

# Prompt the user to click the first point
input("Click the first point on the screen and press Enter...")

# Start the mouse listener
listener = mouse.Listener(on_click=on_click)
listener.start()

# Wait for the coordinates to be captured
listener.join()
