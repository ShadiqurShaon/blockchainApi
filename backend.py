from hashlib import sha256
import json
import time


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.panding_transection = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0,[],time.time(),"0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
    
    def last_block(self):
        return self.chain[-1]

    difficulty = 2

    def proof_of_work(self,block):
        block.nonce = 0
        block_hash = block.compute_hash()
        while not block_hash.startswith('0'*Blockchain.difficulty):
            block.nonce+=1
            block_hash = block.compute_hash()
        
        return block_hash;

    def add_block_to_chain(self,block,proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block,proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True
    

    def is_valid_proof(self,block,block_hash):
        return (block_hash.startswith('0'*Blockchain.difficulty) and block_hash ==block.compute_hash())


    def add_new_transection(self,transection):
        self.panding_transection.append(transection)

    
    def mine(self):
        if not self.panding_transection:
            return False
        lastblock = self.last_block
        newblock = Block(
            index = lastblock.index + 1,
            transactions = self.panding_transection,
            timestamp = time.time(),
            previous_hash = lastblock.hash
        )

        proof = self.proof_of_work(newblock)
        self.add_block_to_chain(newblock,proof)
        self.panding_transection = []
        return newblock.index 