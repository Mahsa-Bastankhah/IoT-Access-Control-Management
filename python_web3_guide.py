# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:08:32 2020

@author: nicole
"""

import json
from web3 import Web3
import pprint
from datetime import datetime
import pickle

transactions = []
with open(r"transactions.pickle","wb") as output_file:
    pickle.dump(transactions,output_file)

# We connect to infura node
ropsten_url = "https://ropsten.infura.io/v3/c6f5d9f33f4b457a9c25a4b97a2ae9b8"
web3 = Web3(Web3.HTTPProvider(ropsten_url))

# id_contract Address and abi
# We compile and depoly the smart contracts with remix, then copy the address and abi for here. In order to remoce the line breaks in abi, we use https://www.textfixer.com/tools/remove-line-breaks.php

# make sure to update the addresses and abi's
id_contract_abi = json.loads(
    '[ { "inputs": [ { "internalType": "address", "name": "_admin", "type": "address" }, { "internalType": "address", "name": "_attributeAuthority", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceConfirmed", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "DeviceDelegated", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceDeleted", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "DeviceModified", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "domainName", "type": "string" } ], "name": "NewDomain", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "UserConfirmed", "type": "event" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" }, { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "devicetype", "type": "string" } ], "name": "addDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" } ], "name": "addDomain", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "role", "type": "string" } ], "name": "addUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceOwner", "type": "address" } ], "name": "confirmDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "confirmUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "delegateDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "deleteDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "devices", "outputs": [ { "components": [ { "internalType": "address", "name": "deviceOwner", "type": "address" }, { "internalType": "string", "name": "device_type", "type": "string" }, { "internalType": "string", "name": "domainName", "type": "string" } ], "internalType": "struct ID_contract.Attribute", "name": "attribute", "type": "tuple" }, { "internalType": "bool", "name": "status", "type": "bool" }, { "internalType": "address", "name": "delegatee", "type": "address" }, { "internalType": "bool", "name": "existing", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceAttributes", "outputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" } ], "name": "getDomain", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddr", "type": "address" } ], "name": "getUserAttributes", "outputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "modifyDeviceAttr", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "userList", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "users", "outputs": [ { "internalType": "string", "name": "role", "type": "string" }, { "internalType": "bool", "name": "existing", "type": "bool" }, { "internalType": "bool", "name": "status", "type": "bool" } ], "stateMutability": "view", "type": "function" } ]')
id_contract_address = '0x2C26F7F6851cFa4232fD3981A78bD61c879F7894'

token_contract_abi = json.loads([
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "holder_object_action_hash",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "usage_times",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "usage_duration",
                "type": "uint256"
            }
        ],
        "name": "issueToken",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "_from",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "OnValueChanged",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "token_holder",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "object",
                "type": "address"
            },
            {
                "internalType": "string",
                "name": "action",
                "type": "string"
            }
        ],
        "name": "usageCountDown",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "token_holder",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "object",
                "type": "address"
            },
            {
                "internalType": "string",
                "name": "action",
                "type": "string"
            }
        ],
        "name": "getToken",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
])
token_contract_address = '0x14E8BA4AA4A5282B106A98cC202B98E6aEb518C2'

policy_contract_abi = json.loads(
    '[ { "inputs": [ { "internalType": "address", "name": "_admin", "type": "address" }, { "internalType": "address", "name": "_attributeAuthority", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceConfirmed", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "DeviceDelegated", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceDeleted", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "DeviceModified", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": false, "internalType": "string", "name": "domainName", "type": "string" } ], "name": "NewDomain", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "UserConfirmed", "type": "event" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" }, { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "devicetype", "type": "string" } ], "name": "addDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" }, { "internalType": "address", "name": "owner", "type": "address" } ], "name": "addDomain", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "role", "type": "string" } ], "name": "addUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceOwner", "type": "address" } ], "name": "confirmDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "confirmUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "delegateDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "deleteDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "devices", "outputs": [ { "components": [ { "internalType": "address", "name": "deviceOwner", "type": "address" }, { "internalType": "string", "name": "device_type", "type": "string" }, { "internalType": "string", "name": "domainName", "type": "string" } ], "internalType": "struct ID_contract.Attribute", "name": "attribute", "type": "tuple" }, { "internalType": "enum ID_contract.Status", "name": "status", "type": "uint8" }, { "internalType": "address", "name": "delegatee", "type": "address" }, { "internalType": "bool", "name": "existing", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceAttributes", "outputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" } ], "name": "getDomain", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddr", "type": "address" } ], "name": "getUserAttributes", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "modifyDeviceAttr", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "userList", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "users", "outputs": [ { "internalType": "string", "name": "role", "type": "string" }, { "internalType": "bool", "name": "existing", "type": "bool" }, { "internalType": "enum ID_contract.Status", "name": "status", "type": "uint8" } ], "stateMutability": "view", "type": "function" } ]')
policy_contract_address = '0xa3d8FCEC4A88D35b4D05311f8CcaBABB459eEd86'

judge_contract_abi = json.loads(
    '[ { "inputs": [ { "internalType": "address", "name": "_admin", "type": "address" }, { "internalType": "address", "name": "_attributeAuthority", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceConfirmed", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "DeviceDelegated", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceDeleted", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "DeviceModified", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "domainName", "type": "string" } ], "name": "NewDomain", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "UserConfirmed", "type": "event" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" }, { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "devicetype", "type": "string" } ], "name": "addDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" } ], "name": "addDomain", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "role", "type": "string" } ], "name": "addUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceOwner", "type": "address" } ], "name": "confirmDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "confirmUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "delegateDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "deleteDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "devices", "outputs": [ { "components": [ { "internalType": "address", "name": "deviceOwner", "type": "address" }, { "internalType": "string", "name": "device_type", "type": "string" }, { "internalType": "string", "name": "domainName", "type": "string" } ], "internalType": "struct ID_contract.Attribute", "name": "attribute", "type": "tuple" }, { "internalType": "bool", "name": "status", "type": "bool" }, { "internalType": "address", "name": "delegatee", "type": "address" }, { "internalType": "bool", "name": "existing", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceAttributes", "outputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" } ], "name": "getDomain", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddr", "type": "address" } ], "name": "getUserAttributes", "outputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "modifyDeviceAttr", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "userList", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "users", "outputs": [ { "internalType": "string", "name": "role", "type": "string" }, { "internalType": "bool", "name": "existing", "type": "bool" }, { "internalType": "bool", "name": "status", "type": "bool" } ], "stateMutability": "view", "type": "function" } ]')
judge_contract_address = '0x52c0b32088655305469e26C0da9BDC8DbafBf36A'

# instantiating contracts
id_contract = web3.eth.contract(address=id_contract_address,abi=id_contract_abi)
token_contract = web3.eth.contract(address=token_contract_address,abi=token_contract_abi)
policy_contract = web3.eth.contract(address=policy_contract_address,abi=policy_contract_abi)
judge_contract = web3.eth.contract(address=judge_contract_address,abi=judge_contract_abi)

# in order to test the functions, we need some accounts. We can create an account with the following script.
account1 = web3.eth.account.create('entropy phrase 3')
account1_address = account1.address
account1_prv = account1.privateKey.hex()
# We can get ether from https://faucet.metamask.io/
print(web3.fromWei(web3.eth.getBalance(account1_address),'Ether'))
# I created the followign accounts
admin_prv = '79a37d3c9e07af3d25b8f49ec39fc34d7d607d7a325ceeccf749278b404b4003'
admin_addr = '0xfC9ccF610Aa5D8636C00913D85700eebbB53A445'

# let atribute authority be the same as admin for simplicity
attribute_authority_prv = admin_prv
attribute_authority_address = admin_addr

account1_prv = '0x6160662302861275ebd089eaaab260787993f475425f3ef1a47b387bdc87e90f'
account1_addr = '0x66a3a45be309143d2EF028EE5dDf1e51900ABf60'

token_supervisor_prv_key = '0x90d5d2ea260a008e2af56c10e42e83f0ed593713942f876969ab43a33642f7dc'
token_supervisor_addr = '0x2B59473afb6F8f6C7Ff3F079B3428f82DBBE58d0'

device1_prv = '0x5f8ca16d5c8d94207246ecd33be88e60006569e67d7c75d08f7640c8467bfe46'
device1_address = '0xBb1AB1E750776d7cEa64e43910272C260518f670'

device2_prv = '0x5f8ca16d5c8d94207246ecd33be88e60006569e67d7c75d08f7640c8467bfe46'
device2_address = '0xBb1AB1E750776d7cEa64e43910272C260518f670'

user1_prv = '0x5f8ca16d5c8d94207246ecd33be88e60006569e67d7c75d08f7640c8467bfe46'
user1_addr = '0xBb1AB1E750776d7cEa64e43910272C260518f670'


## Begining of ID Contract Functions
# The following two functions show how to write into the smart contract

def add_device(domainName,deviceAddr,devicetype,owner_prv_key,owner_address):
    nonce = web3.eth.getTransactionCount(owner_address)
    tx = id_contract.functions.addDevice(domainName,deviceAddr,devicetype).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Adding Device"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('Device is added successfully.',tx_hash)

    else:
        return ('Adding failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# add_device('first_domain',device1_address,'light_sensor',account1_prv,account1_addr)


def confirmDevice(deviceOwner,device_prv_key,device_address):
    nonce = web3.eth.getTransactionCount(device_address)
    tx = id_contract.functions.confirmDevice(deviceOwner).buildTransaction({'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=device_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    with open(r"transactions.pickle","rb") as input_file:
        transactionList = pickle.load(input_file)
    transactionList.append([tx_hash,"Confirmation"])
    with open(r"transactions.pickle","wb") as output_file:
        pickle.dump(transactionList,output_file)
    return ('Device is confirmed successfully.',tx_hash)


# confirmDevice(account1_addr,device1_prv,device1_address)


# The following functions shows how to call a function and read something. 

def getDeviceAttributes(device_address):
    (device_owner,device_type,device_domain,device_status) = id_contract.functions.getDeviceAttributes(
        device_address).call()
    return (device_owner,device_type,device_domain,device_status)


# getDeviceAttributes(device1_address)


######################################
def add_Domain(domainName,owner_prv_key,owner_address):
    nonce = web3.eth.getTransactionCount(owner_address)
    tx = id_contract.functions.addDomain(domainName).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Adding Domain"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('Domain is added successfully.',tx_hash)
    else:
        return ('Adding failed.')
        pprint.pprint(dict(tx_receipt))


# add_Domain('first_domain',account1_prv,account1_addr)


######################################
def add_User(role,user1_prv,user1_addr):
    nonce = web3.eth.getTransactionCount(user1_addr)
    tx = id_contract.functions.addUser(role).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=user1_prv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Adding User"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('User is added successfully.',tx_hash)
    else:
        return ('Adding failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# add_User('test_user',user1_prv,user1_addr)


###################################

def confirm_user(authority_prv,authority_addr,userAddress):
    nonce = web3.eth.getTransactionCount(authority_addr)
    tx = id_contract.functions.confirmUser(userAddress).buildTransaction({'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=authority_prv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    with open(r"transactions.pickle","rb") as input_file:
        transactionList = pickle.load(input_file)
    transactionList.append([tx_hash,"Confirmation"])
    with open(r"transactions.pickle","wb") as output_file:
        pickle.dump(transactionList,output_file)
    return ('user is confirmed successfully.',tx_hash)


# confirm_user(authority_prv,authority_addr,er1_addr)


##################################
def delegate_device(deviceAddr,delegatee,owner_addr,owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = id_contract.functions.delegateDevice(deviceAddr,delegatee).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Delegation"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('delegated successfully.',tx_hash)
    else:
        return ('delegation failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# delegate_device(device1_address,account2_addr,account1_prv,account1_addr)


#############################################
def modify_device_attr(deviceAddr,deviceType,owner_addr,owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = id_contract.functions.modifyDeviceAttr(deviceAddr,deviceType).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Attributes"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('device attribute modified successfully.',tx_hash)
    else:
        return ('modifying failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# modify_device_attr(device1_address,"camera",account1_prv,account1_addr)


##################################################

def delete_device(deviceAddr,owner_addr,owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = id_contract.functions.deleteDevice(deviceAddr).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Deleting Device"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('device is deleted successfully.',tx_hash)
    else:
        return ('deleting failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# delete_device(device1_address,account1_prv,account1_addr)


############################################################
def get_Device_Owner(device_address):
    owner_adr = id_contract.functions.getDeviceOwner(device_address).call()
    return owner_adr


# get_Device_Owner(device1_address)


###################################################################
def get_Domain(domainName):
    (domain_created,domain_owner,domain_deviceAddr) = id_contract.functions.getDomain(domainName).call()
    return (domain_created,domain_owner,domain_deviceAddr)


# get_Domain("test")


###################################################################
def get_User_Attributes(userAddr):
    (user_role,user_status) = id_contract.functions.getUserAttributes(userAddr).call()
    return (user_role,user_status)


# get_User_Attributes(user1_addr)


###################################################################### END of ID Contract Functions
############################################################################################################ Begining of Token Contract Functions

def get_Token(token_holder,object_adr,action):
    (token_existing,token_issuedate,token_expireddate,token_usage_times) = token_contract.functions.getToken(
        token_holder,object_adr,action).call()
    return (token_existing,token_issuedate,token_expireddate,token_usage_times)


# get_Token(user1_addr,device1_address,"read")


###################################################################### END of Token Contract Functions
############################################################################################################ Begining of Policy Contract Functions
def add_device_policy(device,action,permitted_owner,permitted_device_type,permitted_domain_name,permitted_usage_times,
                      permitted_usage_duration,owner_addr,owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = policy_contract.functions.add_device_policy(device,action,permitted_owner,permitted_device_type,
                                                     permitted_domain_name,permitted_usage_times,
                                                     permitted_usage_duration).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Policy"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('policy is added successfully.',tx_hash)
    else:
        return ('adding policy failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# add_device_policy(device1_address,"read",account1_addr,"camera","test",24,1,account1_addr,account1_prv)


###########################################################
def add_user_policy(device,action,permitted_role,permitted_usage_times,permitted_usage_duration,owner_addr,
                    owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = policy_contract.functions.add_user_policy(device,action,permitted_role,permitted_usage_times,
                                                   permitted_usage_duration).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Policy"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('policy is added successfully.',tx_hash)
    else:
        return ('adding policy failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# add_user_policy(device1_address,"read","user",24,1,account1_addr,account1_prv)


###############################################################

def remove_policy(device,action,policy_index,owner_addr,owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = policy_contract.functions.remove_policy(device,action,policy_index).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Policy"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('policy is removed successfully.',tx_hash)
    else:
        return ('removing policy failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# remove_policy(device1_address,"read",1,account1_addr,account1_prv)


################################################################

def add_special_id(device,action,special_id,owner_addr,owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = policy_contract.functions.add_special_id(device,action,special_id).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Policy"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('special id is added successfully.',tx_hash)
    else:
        return ('adding special id failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# add_special_id(device1_address,"read",user1_addr,account1_addr,account1_prv)


###################################################################
def remove_special_id(device,action,special_id,owner_addr,owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = policy_contract.functions.remove_special_id(device,action,special_id).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Policy"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('special id is removed successfully.',tx_hash)
    else:
        return ('removing special id failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# remove_special_id(device1_address,"read",user1_addr,account1_addr,account1_prv)


######################################################################
def get_device_policy_size(owner,device,action):
    policy_length = policy_contract.functions.get_device_policy_size(owner,device,action).call()
    return policy_length


get_device_policy_size(account1_addr,device1_address,"read")


########################################################################
def get_user_policy_size(owner,device,action):
    policy_length = policy_contract.functions.get_user_policy_size(owner,device,action).call()
    return policy_length


# get_user_policy_size(account1_addr,device1_address,"read")


#########################################################################
def get_special_list_size(owner,device,action):
    list_length = policy_contract.functions.get_special_list_size(owner,device,action).call()
    return list_length


# get_special_list_size(account1_addr,device1_address,"read")


############################################################################
def get_Device_Policy(Hash,num):
    (policy_owner,policy_device_type,policy_domain,policy_usage_times,
     policy_usage_duration) = policy_contract.functions.get_Device_Policy(Hash,num).call()
    return (policy_owner,policy_device_type,
            policy_domain,policy_usage_times,
            policy_usage_duration)


# get_Device_Policy("",1)


################################################
def get_User_Policy(Hash,num):
    (policy_role,policy_usage_times,policy_usage_duration) = policy_contract.functions.get_User_Policy(Hash,num).call()
    return (policy_role,policy_usage_times,
            policy_usage_duration)


# get_User_Policy("",1)


###################################################################### END of Policy Contract Functions
############################################################################################################ Begining of Judge Contract Functions

def accessReq_ByDevice(requestedObjectAddress,action,requestor_addr,requestor_prv_key):
    nonce = web3.eth.getTransactionCount(requestor_addr)
    tx = judge_contract.functions.accessReqByDevice(requestedObjectAddress,action).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=requestor_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Token"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('request is sent successfully.',tx_hash)
    else:
        return ('requesting failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# accessReq_ByDevice(device1_address,"read",device2_address,device2_prv)


###################################################################
def accessReq_ByUser(requestedObjectAddress,action,requestor_addr,requestor_prv_key):
    nonce = web3.eth.getTransactionCount(requestor_addr)
    tx = judge_contract.functions.accessReqByUser(requestedObjectAddress,action).buildTransaction(
        {'nonce': nonce,'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx,private_key=requestor_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        with open(r"transactions.pickle","rb") as input_file:
            transactionList = pickle.load(input_file)
        transactionList.append([tx_hash,"Policy"])
        with open(r"transactions.pickle","wb") as output_file:
            pickle.dump(transactionList,output_file)
        return ('request is sent successfully.',tx_hash)
    else:
        return ('requesting failed.',tx_hash)
        pprint.pprint(dict(tx_receipt))


# accessReq_ByUser(device1_address,"read",user1_addr,user1_prv)
###################################################################### END of Judge Contract Functions
#################################### Access device
def AccessDevice(requestedObjectAddress,action,requestor_addr):
    (token_existing,token_issuedate,token_expireddate,token_usage_times) = get_Token(requestor_addr,
                                                                                     requestedObjectAddress,action)
    now = datetime.now()
    if token_existing == True and now > token_issuedate and now < token_expireddate and token_usage_times > 0:
        nonce = web3.eth.getTransactionCount(token_supervisor_adr)
        tx = token_contract.functions.usageCountDown(requestor_addr,requestedObjectAddress,action).buildTransaction(
            {'nonce': nonce,'gas': 2000000})
        signed_tx = web3.eth.account.signTransaction(tx,private_key=token_supervisor_prv_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        if tx_receipt["status"] == 1:
            with open(r"transactions.pickle","rb") as input_file:
                transactionList = pickle.load(input_file)
            transactionList.append([tx_hash,"Access"])
            with open(r"transactions.pickle","wb") as output_file:
                pickle.dump(transactionList,output_file)
            return True
        else:
            return False
    else:
        return False


################################################################################################ list of all transactions
def GetAllTransactions():
    with open(r"transactions.pickle","rb") as input_file:
        transactionList = pickle.load(input_file)
    return transactionList
#################################################################################################
