from PIL import Image
import os

def encrypt_image(image_path, key, save_path):
    try:
        # Open the image
        image = Image.open(image_path)
        pixels = image.load()
        
        # Get image dimensions
        width, height = image.size
        
        # Encrypt the image by adding the key to each pixel's value
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
        
        # Save the encrypted image
        encrypted_image_path = os.path.join(save_path, "encrypted_image.png")
        image.save(encrypted_image_path)
        print(f"Encrypted image saved as {encrypted_image_path}")
    
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(image_path, key, save_path):
    try:
        # Open the image
        image = Image.open(image_path)
        pixels = image.load()
        
        # Get image dimensions
        width, height = image.size
        
        # Decrypt the image by subtracting the key from each pixel's value
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
        
        # Save the decrypted image
        decrypted_image_path = os.path.join(save_path, "decrypted_image.png")
        image.save(decrypted_image_path)
        print(f"Decrypted image saved as {decrypted_image_path}")
    
    except Exception as e:
        print(f"Error during decryption: {e}")


    save_path = "D:\\internship\\prodigy\\p m"
    
    # Ensure the directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    image_path = input("Enter the path to the image (e.g., 'example.jpg'): ").strip()
    key = int(input("Enter the encryption/decryption key (integer): "))
    
    mode = input("Do you want to encrypt or decrypt the image? (e/d): ").lower().strip()
    
    if mode == 'e':
        encrypt_image(image_path, key, save_path)
    elif mode == 'd':
        decrypt_image(image_path, key, save_path)
    else:
        print("Invalid mode selected. Please choose 'e' for encryption or 'd' for decryption.")
