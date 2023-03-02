import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Define the filter matrix
filter_matrix = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Apply the filter on the image
filtered_image = cv2.filter2D(image, -1, filter_matrix)

# Display the filtered image
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()