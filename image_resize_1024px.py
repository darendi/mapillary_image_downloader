import os
import cv2

# Define the path to the folder containing the images
image_folder = r'C:\Users\65923\Desktop\MUSPP\Term 3\Thesis\Mapiliary\lat long image downloader\images\commerce expat area\1_commerceexpatarea_0_15_N'

# Define the output folder to store the resized images
output_folder = r'C:\Users\65923\Desktop\MUSPP\Term 3\Thesis\Mapiliary\lat long image downloader\images\commerce expat area\1_commerceexpatarea_0_15_N\resized_1024px'
os.makedirs(output_folder, exist_ok=True)

# Define the target width for resizing
target_width = 1024
target_height = 576

# Iterate over the images in the image folder
for image_name in os.listdir(image_folder):
    # Get the image file path
    image_path = os.path.join(image_folder, image_name)
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Failed to load {image_name}.")
        continue
    
    # Calculate the aspect ratio and determine the new dimensions
    aspect_ratio = image.shape[1] / image.shape[0]
    target_height = int(target_width / aspect_ratio)
    
    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (target_width, target_height))
    
    # Save the resized image to the output folder
    output_path = os.path.join(output_folder, image_name)
    cv2.imwrite(output_path, resized_image)

    print(f"Processed image: {image_name}, Saved as: {output_path}")

print("Image resizing completed.")