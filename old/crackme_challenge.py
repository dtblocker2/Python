# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE07b34c`_6N"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def encode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)



def decode_secret(secret):
    for i in range(0,99):
        rotate_const = i

    # Storage for decoded secret
        decoded = ""

    # decode loop
        for c in secret:
            index = alphabet.find(c)
            if index-rotate_const+1 >= 0:
                original_index = (index - rotate_const)+1
                decoded = decoded + alphabet[original_index]
            else:
                original_index = index - rotate_const + len(alphabet) + 1
                decoded = decoded + alphabet[original_index]
        print(decoded)
        print("")

decode_secret(f"A:4@r%uL`M-^M0c0AbcM-MFE07b34c`_6N")