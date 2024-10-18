from block import Block
from transaction import Transaction
import time

# blockchain
blockchain = []

# create genesis block
def create_genesis_block():
    blockchain.append(Block(0, [], time.time(), '0', 0))

# proof of work
def proof_of_work(previous_block, transaction):
    nonce = 0
    while True:
        new_block = Block(previous_block.index + 1, transaction, time.time(), previous_block.hash, nonce)
        if new_block.hash[0:4] == '0000':  # Increased difficulty to 4 leading zeros
            return new_block
        nonce += 1

# add 5 blocks to blockchain
create_genesis_block()  # Create genesis block outside the loop

for i in range(1, 6):  # Start from 1 since genesis block is already created
    transaction = [Transaction('alice', 'bob', '10')]
    new_block = proof_of_work(blockchain[len(blockchain) - 1], transaction)
    blockchain.append(new_block)

    print('Block {} has been mined.'.format(new_block.index))
    print('The hash of block {} is {}'.format(new_block.index, new_block.hash))