import cv2

def resize_image(input_image_path, output_image_path, scale_percent):
    # Read the input image
    image = cv2.imread(input_image_path)

    if image is None:
        print(f"Error: Unable to load image from {input_image_path}")
        return

    # Calculate the new dimensions
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    new_dimensions = (width, height)

    # Resize the image
    resized_image = cv2.resize(image, new_dimensions)

    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)
    print(f"Image resized and saved as {output_image_path}")

# Example usage
input_path = "hacker-binary.jpg"  # Replace with your image path
output_path = "resized_image.png"  # Replace with your desired output file name
scale_percent = 50  # Resize image to 50% of original size

resize_image(input_path, output_path, scale_percent)
