from fastapi import FastAPI
from blockchain import Blockchain

# Building Blockchain
blockchain = Blockchain()

# Web App
app = FastAPI()

@app.get('/mineBlock')
async def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    return {'message': 'You mined a block', 'data': block}

@app.get('/getChain')
async def get_chain():
    return blockchain.chain