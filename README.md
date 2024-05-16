# Forti Hash Algorithm

## Overview

The Forti Hash algorithm is a cryptographic hash function designed to produce a secure and reliable hash value for input data. It employs a combination of operations including bitwise manipulation, rotation, mixing functions, and constant modification to generate the hash digest.

## Implementation

The algorithm is implemented in Python and consists of two main components:

1. **Generation of Words**: Initial words are combined with a randomly generated matrix through a series of operations including XOR, bitwise AND, bitwise OR, rotation, and addition of random constants.

2. **Hash Computation**: The hash computation involves processing the input message in chunks, applying a series of operations on each chunk, and updating the hash values iteratively. Operations include rotation, bitwise manipulation, mixing functions, and constant modification.

## Usage

To use the Forti Hash algorithm:

1. Import the necessary functions and constants from the provided modules.
2. Call the `Algo()` function with the message to be hashed and an optional salt parameter.
3. The function returns the hash digest as a hexadecimal string.

Example:

```python
from Utils.helper import preprocessMessage
from Utils.constants import K, h_hex
from FortiHash import Algo

message = "Hello, world!"
salt = "random_salt"

# Preprocess message
preprocessed_message = preprocessMessage(message, salt)

# Compute hash
hash_digest = Algo(preprocessed_message, salt)

print("Hash Digest:", hash_digest)
