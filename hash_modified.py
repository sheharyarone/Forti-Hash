from Utils.helper import b2Tob16, preprocessMessage, chunker, initializer
from Utils.utils import *
from Utils.constants import *
import numpy as np

import numpy as np

def generate_words(initial_words):
    # Convert initial words to a NumPy array for easier manipulation
    initial_words_array = np.array(initial_words, dtype=np.uint32)

    # 1. Initialize a new matrix of shape (48, 32) with random 0's and 1's
    new_matrix = np.random.randint(0, 2, size=(48, 32), dtype=np.uint32)

    # 2. Apply operations to update the new matrix based on the initial words
    for i in range(48):
        # Example operations:
        # XOR each row of the new matrix with the corresponding row of the initial words
        new_matrix[i] ^= initial_words_array[i % 16]
        # Bitwise AND each row of the new matrix with the reverse of the corresponding row of the initial words
        new_matrix[i] &= np.flip(initial_words_array[i % 16], axis=0)
        # Bitwise OR each row of the new matrix with the bitwise NOT of the corresponding row of the initial words
        new_matrix[i] |= ~initial_words_array[i % 16]
        # Rotate each row of the new matrix by a random amount
        shift_amount = np.random.randint(1, 32)
        new_matrix[i] = np.roll(new_matrix[i], shift_amount)
        # Add a random constant to each row of the new matrix
        constant = np.random.randint(0, 2**32, dtype=np.uint32)
        new_matrix[i] += constant

    # 3. Combine initial words and newly generated words
    final_words = np.vstack((initial_words_array, new_matrix))

    return final_words.tolist()  # Convert back to list for compatibility




def sha256(message,salt): 
    k = initializer(K)
    h0, h1, h2, h3, h4, h5, h6, h7 = initializer(h_hex)
    chunks = preprocessMessage(message,salt)
    for chunk in chunks:
        w = chunker(chunk, 32)
        # Generate words
        final_words = generate_words(w)
        w = final_words
        # Print the final words (for demonstration only)
        # print(final_words)
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7
        for j in range(64):
            S1 = XORXOR(rotr(e, 6), rotr(e, 11), rotr(e, 25) )
            ch = XOR(AND(e, f), AND(NOT(e), g))
            temp1 = add(add(add(add(h, S1), ch), k[j]), w[j])
            S0 = XORXOR(rotr(a, 2), rotr(a, 13), rotr(a, 22))
            m = XORXOR(AND(a, b), AND(a, c), AND(b, c))
            temp2 = add(S0, m)
            h = g
            g = f
            f = e
            e = add(d, temp1)
            d = c
            c = b
            b = a
            a = add(temp1, temp2)
        h0 = add(h0, a)
        h1 = add(h1, b)
        h2 = add(h2, c)
        h3 = add(h3, d)
        h4 = add(h4, e)
        h5 = add(h5, f)
        h6 = add(h6, g)
        h7 = add(h7, h)
    digest = ''
    for val in [h0, h1, h2, h3, h4, h5, h6, h7]:
        digest += b2Tob16(val)
    return digest

if __name__ == '__main__':
    verdict = 'y'
    while verdict == 'y':
        input_message = input('Type or copy your message here: ')
        salt=input("Your salt value")
        print('Your message: ', input_message)
        print('Your salt: ', salt)
        
        print('Hash: ', sha256(input_message,salt))
        verdict = input('Do you want to tryte another text? (y/n): ').lower()