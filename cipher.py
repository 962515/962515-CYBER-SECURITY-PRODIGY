letters='abcdefghijklmnopqrstuvwxyz'
length=len(letters)


def encrypt(plaintext,key):
    ciphertext=""
    for letter in plaintext:
        letter ==letter.lower()
        if not letter =="":
            index = letters.find(letter)
            if index== -1:
                ciphertext +=letter
            else:
                new_index= index + int(key)
                if new_index >=length:
                    new_index-=length
                ciphertext +=letters[new_index]

    return ciphertext


def decrypt(ciphertext,key):
    plaintext=""
    for letter in ciphertext:
        letter ==letter.lower()
        if not letter =="":
            index = letters.find(letter)
            if index== -1:
                plaintext +=letter
            else:
                new_index= index - int(key)
                if new_index <0:
                    new_index+=length
                plaintext +=letters[new_index]

    return plaintext


print("*******************************************************************************")
print("Caesar Cipher program")

print("Do you want encrypt and decrypt:")
user_input=input('e/d:').lower()

if user_input =='e':
    print("ENCRYPTION MODE")
    key=input("enter the key(1 TO 25): ")
    text=input("Enter the text:")
    ciphertext=encrypt(text, key)
    print(f'Ciphertext:{ciphertext}')


elif user_input =='d':
    print("DECRYPTION MODE")
    key=input("enter the key(1 TO 25): ")
    text=input("Enter the text:")
    plaintext=decrypt(text,key)
    print(f'Ciphertext:{plaintext}')

