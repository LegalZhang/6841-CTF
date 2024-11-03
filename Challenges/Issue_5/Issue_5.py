import hashlib
import base64

def compute_encrypto(char):
    md5_hash = hashlib.md5(char.encode()).hexdigest()
    md5_bytes = bytes.fromhex(md5_hash)
    base64_encoded = base64.b64encode(md5_bytes).decode('utf-8')
    return base64_encoded

def main():
    # read flag.txt
    try:
        with open('flag.txt', 'r') as flag_file:
            content = flag_file.read()
    except FileNotFoundError:
        print("flag.txt not found")
        return

    # write ciphertext
    with open('ciphertext.txt', 'w') as output_file:
        for char in content:
            if char.isalpha():  #only encrypt alphabets
                md5_base64 = compute_encrypto(char)
                output_file.write(md5_base64 + '\n')

    print("ciphertext.txt generated")

if __name__ == '__main__':
    main()
