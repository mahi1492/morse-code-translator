print("\n\n***MORSE CODE TRANSLATOR***")

# set up the morse code dictionary
def morse(text):
    # function to encrypt
    encrypt = {
                'A':'.-', 'B':'-...', 'C':'-.-.',
                'D':'-..', 'E':'.', 'F':'..-.',
                'G':'--.', 'H':'....', 'I':'..',
                'J':'.---', 'K':'-.-', 'L':'.-..',
                'M':'--', 'N':'-.', 'O':'---',
                'P':'.--.', 'Q':'--.-', 'R':'.-.',
                'S':'...', 'T':'-', 'U':'..-',
                'V':'...-', 'W':'.--', 'X':'-..-',
                'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-', ' ' : '/'
               }

    # function to decrypt
    decrypt = {value: key for key, value in encrypt.items()}

    # check for encryption or decryption
    if '-' in text:
        return ''.join(decrypt[i] for i in text.split())

    else:
        return ' '. join(encrypt[i] for i in text.upper())

# input the text
string = input("\nEnter the text to be converted (morse code / english): ")

# print out the translation
print(morse(string))
