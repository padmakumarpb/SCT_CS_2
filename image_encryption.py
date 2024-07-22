from PIL import Image
import numpy as np
import os

def ensure_rgb(image_path):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image

def encrypt_image(image_path,key_value):
    image_to_be_protected = ensure_rgb(image_path)
    pixels = np.array(image_to_be_protected, dtype=np.uint8)

    # Swapping pixel values
    modified_pixels = np.copy(pixels)
    modified_pixels[:, :, [0,2]] = modified_pixels[:, :, [2,0]]

    key_value = key_value % 256

    # Applying a basic mathematical operation (XOR) to each pixel
    encrypted_pixels = np.bitwise_xor(modified_pixels, key_value)
    encrypted_pixels = np.clip(encrypted_pixels, 0, 255).astype(np.uint8)

    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image_path = input("Please enter the path to save the encrypted image: ")
    encrypted_image.save(encrypted_image_path)

def decrypt_image(encrypted_image_path,key_value):
    encrypted_image = ensure_rgb(encrypted_image_path)
    encrypted_pixels = np.array(encrypted_image, dtype=np.uint8)

    # Swapping pixel values
    modified_pixels = np.copy(encrypted_pixels)
    modified_pixels[:, :, [0, 2]] = modified_pixels[:, :, [2, 0]]

    key_value = key_value % 256

    # Applying a basic mathematical operation (XOR) to each pixel
    decrypted_pixels = np.bitwise_xor(modified_pixels, key_value)
    decrypted_pixels = np.clip(decrypted_pixels, 0, 255).astype(np.uint8)

    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image_path = input("Please enter the path to save the decrypted image: ")
    decrypted_image.save(decrypted_image_path)

def get_valid_image_path():
    while True:
        image_path = input("Please enter the path to the image file (Example of a valid file path: /home/user/Pictures/enc.JPG): ")
        if os.path.isfile(image_path):
            return image_path
        else:
            print("Invalid input! Please enter a valid file path.")

def get_valid_key_value():
    while True:
        try:
            key_value = int(input("Enter the key value (0-255): "))
            if 0 <= key_value <= 255:
                return key_value
            else:
                print("Invalid input! Please enter a number between 0 and 255.")
        except ValueError:
            print("Invalid input! Please enter a valid integer between 0 and 255.")


end_session = True
while end_session:

    ask_the_user = input("Type 'encrypt' for Encryption and 'decrypt' for Decryption\n").lower()

    if ask_the_user not in ["encrypt" , "decrypt"]:
        print("Invalid input!\n")
        continue

    image_path = get_valid_image_path()

    key = get_valid_key_value()

    if ask_the_user == "encrypt":
        encrypt_image(image_path,key)
        print("The image has been successfully encrypted and is stored at the path you provided.")
    elif ask_the_user == "decrypt":
        decrypt_image(image_path,key)
        print("The image has been successfully decrypted and is stored at the path you provided.")

        
    while True:
        choose  = input("Type 'yes' to continue and 'no' to stop\n").lower()
        if choose in ['yes' , 'no']:
            break
        else :
            print("Invalid input! Please type 'yes' or 'no'.\n")

    if choose == 'no':
        end_session = False
        print("Thank you. Have a nice day!\n")

#end of the code