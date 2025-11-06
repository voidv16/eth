from PIL import Image
import binascii

# py -m pip install pillow
# Function to encode text into an image
def encode_image(image_path, secret_message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(c), '08b') for c in secret_message)
    img_data = list(img.getdata())

    # Modify the LSB of each pixel to store the secret message
    new_img_data = []
    data_index = 0

    for pixel in img_data:
        new_pixel = list(pixel)
        for i in range(len(new_pixel)):
            if data_index < len(binary_message):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_message[data_index])
                data_index += 1
        new_img_data.append(tuple(new_pixel))

    img.putdata(new_img_data)
    img.save(output_path)


# Function to decode the secret message from an image
def decode_image(image_path):
    img = Image.open(image_path)
    img_data = list(img.getdata())
    binary_message = ''
 
    for pixel in img_data:
        for value in pixel:
            binary_message += str(value & 1)

    # Convert binary message to string
    secret_message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) == 8:
            secret_message += chr(int(byte, 2))
        else:
            break

    return secret_message


# Example usage
image_path = 'input_image.jpg'
encoded_image_path = 'encoded_image.jpg'
message = "This is a secret message"

encode_image(image_path, message, encoded_image_path)

# To retrieve the hidden message
retrieved_message = decode_image(encoded_image_path)
print("Decoded Message:", retrieved_message)
