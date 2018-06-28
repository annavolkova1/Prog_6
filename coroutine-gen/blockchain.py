import hashlib as hasher
import datetime as date
import string
import itertools

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """ Конструктор нового объекта """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """ Функция для создания нового блока """
        sha = hasher.sha256()
        sha.update(
            (str(self.index) + str(self.timestamp) +
             str(self.data) + str(self.previous_hash)).encode('utf-8')
        )
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "This is first block data", str(0))


def next_block(last_block):

    current_timestamp = date.datetime.now()

    current_index = last_block.index + 1

    current_data = str(current_index) + string.ascii_lowercase

    current_hash = last_block.hash

    return Block(current_index, current_timestamp, current_data, current_hash)


def create_blockchain():
    blockchain = [create_genesis_block()]
    for index in itertools.count():
        data = yield
        block = next_block(blockchain[index])
        yield block.hash
        blockchain.append(block)


blockchain = create_blockchain()
x = input('enter')
next(blockchain)
res = 0
while x == 'e':
    res = blockchain.send(res)
    next(blockchain)
    print(res)
    x = input('enter')


blockchain = [create_genesis_block()]
number_of_blocks = 5


for i in range(5):
    new_block = next_block(blockchain[i])
    blockchain.append(new_block)
    # print(f"Data: {new_block.data}, New block is : {new_block.hash} \n")
    print ("Data : {} ".format(new_block.data))
    print("New block is : {} \n".format(new_block.hash))