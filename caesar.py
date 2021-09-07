def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    for i in range(len(plaintext)) :
        char = plaintext[i]
        ciphertext += chr((ord(char) + key - 65) % 26 + 65)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    for i in range(len(plaintext)) :
        char = plaintext[i]
        ciphertext += chr((ord(char) + key - 65) % 26 + 65)
    return plaintext


