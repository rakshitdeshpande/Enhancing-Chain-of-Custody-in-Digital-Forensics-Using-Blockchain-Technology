import hashlib
import json
from datetime import datetime

# Define a block in the blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index) + str(self.timestamp) + json.dumps(self.data) + self.previous_hash
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

# Define the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.utcnow()), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.utcnow()),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class ForensicLogger:
    def __init__(self):
        self.blockchain = Blockchain()

    def log_image_forensic_data(self, image_id, metadata):
        forensic_data = {
            "image_id": image_id,
            "metadata": metadata,
            "timestamp": str(datetime.utcnow()),
        }
        self.blockchain.add_block(forensic_data)

    def display_chain(self):
        for block in self.blockchain.chain:
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print("----------------------------------------")

if __name__ == "__main__":
    logger = ForensicLogger()

    # Log forensic data for images
    logger.log_image_forensic_data("IMG123", {"owner": "Alice", "location": "Server 1"})
    logger.log_image_forensic_data("IMG124", {"owner": "Bob", "location": "Server 2"})

    # Display the blockchain
    logger.display_chain()

    # Validate the chain
    print("Is blockchain valid : ", logger.blockchain.is_chain_valid())
