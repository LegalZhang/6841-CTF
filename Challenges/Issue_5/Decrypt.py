import base64

with open('ciphertext.txt', 'r') as input_file, open('hashes.txt', 'w') as output_file:
    for line in input_file:
        base64_encoded = line.strip()
        # decode base64
        md5_bytes = base64.b64decode(base64_encoded)
        md5_hex = md5_bytes.hex()
        output_file.write(md5_hex + '\n')
