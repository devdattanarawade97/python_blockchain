# Simple Blockchain in Python

This is a basic implementation of a blockchain in Python. It demonstrates the core concepts of a blockchain, including:

* **Blocks:** Data structures that store transactions and are linked together.
* **Proof-of-Work:** A mechanism for achieving consensus and adding blocks to the chain.
* **Hashing:** Used to secure the blockchain and ensure data integrity.

## How it Works

1. **Block Structure:** Each block contains an index, a list of transactions, a timestamp, the hash of the previous block, and a nonce.

2. **Genesis Block:** The first block in the chain is the genesis block. It is created manually.

3. **Proof-of-Work:** This implementation uses a simple Proof-of-Work algorithm. To add a new block, a nonce is incremented until the block's hash starts with four zeros.

4. **Adding Blocks:** New blocks are created with a list of transactions and added to the chain after successful Proof-of-Work.

## Files

* **`blockchain.py`:**  Contains the main code for creating and managing the blockchain.
* **`block.py`:**  (Not provided) Should contain the `Block` class definition with the necessary attributes and methods (index, transactions, timestamp, previous hash, nonce, hash calculation).
* **`transaction.py`:** (Not provided) Should contain the `Transaction` class definition to represent transactions.

## Usage

1. **Implement `block.py` and `transaction.py`:** Create these files and define the `Block` and `Transaction` classes according to the descriptions above.
2. **Run `blockchain.py`:** This will create a blockchain with a genesis block and 5 additional blocks.

## Limitations

* **Simplified Proof-of-Work:** The Proof-of-Work algorithm is simplified for demonstration purposes. Real blockchains use more complex algorithms.
* **No Networking:** This implementation does not include any networking functionality.
* **No Difficulty Adjustment:** The difficulty of the Proof-of-Work is not dynamically adjusted.
* **Basic Transaction Handling:** The `Transaction` class is very basic and does not include any validation or security features.


## Disclaimer

This code is for educational purposes only and should not be used in a production environment.

## Contributing

Feel free to fork this repository and make improvements. Pull requests are welcome!