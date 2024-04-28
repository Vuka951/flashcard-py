import base64

def img_to_base64(png_file):
    with open(png_file, "rb") as f:
        image_bytes = f.read()
        base64_str = base64.b64encode(image_bytes).decode("utf-8")
        return base64_str

if __name__ == "__main__":
    img_file = "./speed.jpg"
    base64_str = img_to_base64(img_file)
    print("Base64 encoded string:")
    print(base64_str)
