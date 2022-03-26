import json
import os
from audioop import add

from dotenv import find_dotenv, load_dotenv
from web3 import Web3

load_dotenv(find_dotenv())

ganache_url = os.environ.get("URL")
web3 = Web3(Web3.HTTPProvider(ganache_url))

sender = os.environ.get("SENDER")
receiver = os.environ.get("RECEIVER")
private_key = os.environ.get("SENDER_PRIVATE_KEY")

#get the nonce
nonce = web3.eth.getTransactionCount(sender)
#build transaction
tx = {
    'nonce':nonce,
    'to': receiver,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}
#sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#get transaction hash
hexa_hash = web3.toHex(tx_hash)
print(hexa_hash)
