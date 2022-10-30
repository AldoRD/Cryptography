from operator import xor
from Crypto.Random.random import getrandbits
import base64

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def textToBinary(text):
    res = ''.join(format(i, '08b') for i in bytearray(text, encoding ='utf-8'))
    return str(res)

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def prbg():
    x = int(input('Introduce the lenght of the pseudorandom bit: '))
    randomBit = getrandbits(x)
    randomBitHex = hex(randomBit)
    print (">> Decimal: {}".format(randomBit))
    print (">> Hexadecimal: {}".format(randomBitHex))
    print("\n")

def binaryBase64():
    sample_string = input("Introduce a binary string: ")
    sample_string_bytes = repr(sample_string).encode('ascii')
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    print(">> Encoded string: {}".format(base64_string))
    print("\n")

def binaryBase64s(sample_string):
    sample_string_bytes = repr(sample_string).encode('ascii')
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string

def base64Binary(base64_string):
    base64_bytes = base64_string.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    
    return message
    

def oneTimePad():
    #Input of plaintext
    m = input('Plaintext: ')

    #Converts message to a binary string
    m_bin = textToBinary(str(m))
    # print(m_bin) debug line

    #Key generation
    k = ''
    for i in range(0,len(m_bin)):
        #generates a pseudorandom num (1 / 0)
        rdm_num = getrandbits(1)
        k = k + str(rdm_num)

    #XOR
    #cipherthext
    c = ''
    aux = 0
    for i in range(len(m_bin)):
        aux = (int(m_bin[i]) ^ int(k[i]))
        c = c + str(aux) 

    #Key in base 64
    k64 = binaryBase64s(k)

    #ciphertext in base 64
    c64 = binaryBase64s(c)

    print('>> Ciphertext C in base 64: {}'.format(c64))
    print('>> Key in base 64: {}'.format(k64))
    print("\n")

def decode():
    c64 = input('Ciphertext: ')
    k64 = input('Key: ')

    #Decoding base64 strings
    c = base64Binary(c64)
    k = base64Binary(k64)
    c = c.replace("'","")
    k = k.replace("'","")

    #XOR
    #message / plaintext
    m = ''
    aux = 0
    for i in range(len(c)):
        aux = (int(c[i]) ^ int(k[i]))
        m = m + str(aux) 
    
    m = decode_binary_string(m)

    print(">> Plaintext: {}".format(m))
    print("\n")

def menu():
    print('[1] Generate Pseudorandom Bit')
    print('[2] Convert any binary string into a string in base 64')
    print('[3] One time pad')
    print('[4] Decode')
    print('[0] Exit')

def main():
    menu()
    option = int(input("Select one option: "))

    while option != 0:
        if option == 1:
            #Pseudorandom bit generator
            prbg()
            pass
        elif option == 2:
            #Bin to Base 64
            binaryBase64()
            pass
        elif option == 3:
            #One time pad
            oneTimePad()
            pass
        elif option == 4:
            #Decode
            decode()
            pass
        else:
            print("Invalid option.")
        print
        menu()
        option = int(input("Select one option: "))

main()