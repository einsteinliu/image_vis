import cv2
import os
from glob import glob


# Get all the images to display
all_images = glob("images/*")
# The index of the current image
index = 0

# Create opencv window
cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
# Visualize in full screen
cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

image = all_images[index]
while True:
    # Visualize the current image in full screen
    cv2.imshow("test", cv2.imread(image))
    # Wait for 0.25 seconds and get the key
    key = cv2.waitKey(250)

    # If the key is Esc, break the loop
    if key == 27:
        break

    # If an empty file "message" is found, goto the next image
    if os.path.exists("message"):
        index += 1
        # Loop through all images
        index = index % len(all_images)
        # Remove the empty file "message"
        os.remove("message")
        # Set the image
        image = all_images[index]
