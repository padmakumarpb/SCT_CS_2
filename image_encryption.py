from PIL import Image
import numpy as np



def encrypt_image(image_path,key_value):
    image_to_be_protected = Image.open(image_path)
    pixels = np.array(image_to_be_protected)
    modified_pixels = np.copy(pixels)
    modified_pixels[:, :, [0,2]] = modified_pixels[:, :, [2,0]]
    key_value = key_value % 256
    encrypted_pixels = modified_pixels ^ key_value
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image_path = input("Please enter the path to save the encrypted image: ")
    encrypted_image.save(encrypted_image_path)

def decrypt_image(encrypted_image_path,key_value):
    encrypted_image = Image.open(image_path)
    encrypted_pixels = np.array(encrypted_image)
    modified_pixels = np.copy(encrypted_pixels)
    modified_pixels[:, :, [0, 2]] = modified_pixels[:, :, [2, 0]]
    key_value = key_value % 256
    decrypted_pixels = modified_pixels ^ key_value
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image_path = input("Please enter the path to save the decrypted image: ")
    decrypted_image.save(decrypted_image_path)


end_session = True
while end_session:

    ask_the_user = input("Type 'encrypt' for Encryption and 'decrypt' for Decryption\n").lower()

    if ask_the_user not in ["encrypt" , "decrypt"]:
        print("Invalid input!\n")
        continue
    image_path = input("Please enter the path to the image file: ")
    key = int(input("Enter the key value : "))
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