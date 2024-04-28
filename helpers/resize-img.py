from PIL import Image

def resize_image(image_path, output_path, new_size=(300, 300)):
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Resize the image to cover the specified dimensions
        image.thumbnail(new_size)
        
        # Create a new blank image with the specified dimensions
        new_image = Image.new("RGB", new_size)
        
        # Paste the resized image onto the new image with center alignment
        position = ((new_size[0] - image.size[0]) // 2, (new_size[1] - image.size[1]) // 2)
        new_image.paste(image, position)
        
        # Save the new image
        new_image.save(output_path)
        
        print("Image resized successfully wooo!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    input_image_path = "pillow.jpg"
    output_image_path = "pillow.jpg"
    resize_image(input_image_path, output_image_path)
