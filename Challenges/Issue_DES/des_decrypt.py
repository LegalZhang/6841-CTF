from Crypto.Cipher import DES
import base64

def unpad(text):
    return text.rstrip()

def main():
    # read des.txt
    try:
        with open('des.txt', 'r') as des_file:
            encrypted_base64 = des_file.read().strip()
    except FileNotFoundError:
        return

    # base64 decode
    encrypted_bytes = base64.b64decode(encrypted_base64)

    # brute force key
    for i in range(100000000):
        key = f"{i:08d}"
        cipher = DES.new(key.encode(), DES.MODE_ECB)

        try:
            decrypted_bytes = cipher.decrypt(encrypted_bytes)
            decrypted_text = unpad(decrypted_bytes.decode())

            # check if flag is in decrypted text
            if "flag{" in decrypted_text:
                print("KEY: ", key)
                print("FLAG: ", decrypted_text)
                break
        except:
            # invalid key
            continue

if __name__ == '__main__':
    main()
