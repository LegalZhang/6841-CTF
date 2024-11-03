from Crypto.Cipher import DES
import base64

def pad(text):
    # key has to be multiple of 8
    while len(text) % 8 != 0:
        text += ' '
    return text

def main():
    # read flag.txt
    try:
        with open('flag.txt', 'r') as flag_file:
            plaintext = flag_file.read().strip()
    except:
        return

    # read key.txt
    try:
        with open('key.txt', 'r') as key_file:
            key = key_file.read().strip()
            if len(key) != 8 or not key.isdigit():
                print("Invalid key")
                return
    except:
        return

    cipher = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_text = cipher.encrypt(padded_text.encode())

    encrypted_base64 = base64.b64encode(encrypted_text).decode()

    # write encrypted text to des.txt
    with open('des.txt', 'w') as des_file:
        des_file.write(encrypted_base64)

    print("Encrypted text: ", encrypted_base64)

if __name__ == '__main__':
    main()
