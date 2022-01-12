# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:08:32 2020

@author: nicole
"""

import json
from web3 import Web3
import pprint
import time
import pickle

transactions = []  # list of transactions

# We connect to infura node
ropsten_url = "https://ropsten.infura.io/v3/c6f5d9f33f4b457a9c25a4b97a2ae9b8"
web3 = Web3(Web3.HTTPProvider(ropsten_url))

# id_contract Address and abi
# We compile and depoly the smart contracts with remix, then copy the address and abi for here. In order to remoce the line breaks in abi, we use https://www.textfixer.com/tools/remove-line-breaks.php

# make sure to update the addresses and abi's
id_contract_abi = json.loads(
    '[ { "inputs": [ { "internalType": "address", "name": "_admin", "type": "address" }, { "internalType": "address", "name": "_attributeAuthority", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceConfirmed", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "DeviceDelegated", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "DeviceDeleted", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "deviceAddr", "type": "address" }, { "indexed": false, "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "DeviceModified", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "domainName", "type": "string" } ], "name": "NewDomain", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "UserConfirmed", "type": "event" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" }, { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "devicetype", "type": "string" } ], "name": "addDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" } ], "name": "addDomain", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "role", "type": "string" } ], "name": "addUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceOwner", "type": "address" } ], "name": "confirmDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddress", "type": "address" } ], "name": "confirmUser", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "delegateDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "deleteDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "devices", "outputs": [ { "components": [ { "internalType": "address", "name": "deviceOwner", "type": "address" }, { "internalType": "string", "name": "device_type", "type": "string" }, { "internalType": "string", "name": "domainName", "type": "string" } ], "internalType": "struct ID_contract.Attribute", "name": "attribute", "type": "tuple" }, { "internalType": "bool", "name": "status", "type": "bool" }, { "internalType": "address", "name": "delegatee", "type": "address" }, { "internalType": "bool", "name": "existing", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceAttributes", "outputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" } ], "name": "getDeviceOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "domainName", "type": "string" } ], "name": "getDomain", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "userAddr", "type": "address" } ], "name": "getUserAttributes", "outputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "deviceAddr", "type": "address" }, { "internalType": "string", "name": "deviceType", "type": "string" } ], "name": "modifyDeviceAttr", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "userList", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "users", "outputs": [ { "internalType": "string", "name": "role", "type": "string" }, { "internalType": "bool", "name": "existing", "type": "bool" }, { "internalType": "bool", "name": "status", "type": "bool" } ], "stateMutability": "view", "type": "function" } ]')
id_contract_address = '0x03E26B0e1A8e4f402D471A783b6FF8b8C507c8dD'

token_contract_abi = json.loads(
    '[ { "inputs": [ { "internalType": "address", "name": "_judgeContract_address", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_from", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_value", "type": "uint256" } ], "name": "OnValueChanged", "type": "event" }, { "inputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "name": "AccessTokens", "outputs": [ { "internalType": "bool", "name": "existing", "type": "bool" }, { "internalType": "uint256", "name": "issuedate", "type": "uint256" }, { "internalType": "uint256", "name": "expireddate", "type": "uint256" }, { "internalType": "uint256", "name": "usage_times", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "token_holder", "type": "address" }, { "internalType": "address", "name": "object", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" } ], "name": "getToken", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "holder_object_action_hash", "type": "bytes32" }, { "internalType": "uint256", "name": "usage_times", "type": "uint256" }, { "internalType": "uint256", "name": "usage_duration", "type": "uint256" } ], "name": "issueToken", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "judgeContract_address", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "token_holder", "type": "address" }, { "internalType": "address", "name": "object", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" } ], "name": "usageCountDown", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]')
token_contract_address = Web3.toChecksumAddress('0xa19f8515b268fd37cc2ee3480f0af7a753b8f71a')

policy_contract_abi = json.loads(
    '[ { "inputs": [ { "internalType": "address", "name": "id_contract_address", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" }, { "internalType": "address", "name": "permitted_owner", "type": "address" }, { "internalType": "string", "name": "permitted_device_type", "type": "string" }, { "internalType": "string", "name": "permitted_domain_name", "type": "string" }, { "internalType": "uint256", "name": "permitted_usage_times", "type": "uint256" }, { "internalType": "uint256", "name": "permitted_usage_duration", "type": "uint256" } ], "name": "add_device_policy", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" }, { "internalType": "address", "name": "special_id", "type": "address" } ], "name": "add_special_id", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" }, { "internalType": "string", "name": "permitted_role", "type": "string" }, { "internalType": "uint256", "name": "permitted_usage_times", "type": "uint256" }, { "internalType": "uint256", "name": "permitted_usage_duration", "type": "uint256" } ], "name": "add_user_policy", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "device_attr_const_map", "outputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "string", "name": "device_type", "type": "string" }, { "internalType": "string", "name": "domain", "type": "string" }, { "internalType": "uint256", "name": "usage_times", "type": "uint256" }, { "internalType": "uint256", "name": "usage_duration", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "hash", "type": "bytes32" }, { "internalType": "uint256", "name": "num", "type": "uint256" } ], "name": "get_Device_Policy", "outputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "hash", "type": "bytes32" }, { "internalType": "uint256", "name": "num", "type": "uint256" } ], "name": "get_User_Policy", "outputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" } ], "name": "get_device_policy_size", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" } ], "name": "get_special_list_size", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" } ], "name": "get_user_policy_size", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" }, { "internalType": "uint256", "name": "policy_index", "type": "uint256" } ], "name": "remove_policy", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "device", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" }, { "internalType": "address", "name": "special_id", "type": "address" } ], "name": "remove_special_id", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "special_list_map", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "user_attr_const_map", "outputs": [ { "internalType": "string", "name": "role", "type": "string" }, { "internalType": "uint256", "name": "usage_times", "type": "uint256" }, { "internalType": "uint256", "name": "usage_duration", "type": "uint256" } ], "stateMutability": "view", "type": "function" } ]')
policy_contract_address = '0xC27Be8E6DfE39fC0d0722A5b2D1Cb73e872F3e62'

judge_contract_abi = json.loads(
    '[ { "inputs": [ { "internalType": "address", "name": "IDadmin", "type": "address" }, { "internalType": "address", "name": "attributeAuthority", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "address", "name": "requestedObjectAddress", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" } ], "name": "accessReqByDevice", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "requestedObjectAddress", "type": "address" }, { "internalType": "string", "name": "action", "type": "string" }, { "internalType": "address", "name": "token_contract_address", "type": "address" } ], "name": "accessReqByUser", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "idAddr", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "idContract", "outputs": [ { "internalType": "contract ID_contract", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "policyAddr", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "policyContract", "outputs": [ { "internalType": "contract policy_contract", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "tokenAddr", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "tokenContract", "outputs": [ { "internalType": "contract Token_contract", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" } ]')
judge_contract_address = Web3.toChecksumAddress('0x43e0ed4c8c0650185f1c310e21c9ae23e2114e6b')

# instantiating contracts
id_contract = web3.eth.contract(address=id_contract_address, abi=id_contract_abi)
token_contract = web3.eth.contract(address=token_contract_address, abi=token_contract_abi)
policy_contract = web3.eth.contract(address=policy_contract_address, abi=policy_contract_abi)
judge_contract = web3.eth.contract(address=judge_contract_address, abi=judge_contract_abi)

# in order to test the functions, we need some accounts. We can create an account with the following script.
# account1 = web3.eth.account.create('entropy phrase 3')
# account1_address = account1.address
# account1_prv = account1.privateKey.hex()
# We can get ether from https://faucet.metamask.io/
# print(web3.fromWei(web3.eth.getBalance(account1_address),'Ether'))

# We use the followign accounts for test
admin_prv = '79a37d3c9e07af3d25b8f49ec39fc34d7d607d7a325ceeccf749278b404b4003'  # Ethereum address
admin_addr = '0xfC9ccF610Aa5D8636C00913D85700eebbB53A445'  # private key

# We set the atribute authority be the same as admin for simplicity.
attribute_authority_prv = admin_prv
attribute_authority_address = admin_addr

token_supervisor_prv_key = '0x90d5d2ea260a008e2af56c10e42e83f0ed593713942f876969ab43a33642f7dc'
token_supervisor_addr = '0x2B59473afb6F8f6C7Ff3F079B3428f82DBBE58d0'

device1_prv = '0x5f8ca16d5c8d94207246ecd33be88e60006569e67d7c75d08f7640c8467bfe46'
device1_address = '0xBb1AB1E750776d7cEa64e43910272C260518f670'

device2_prv = 'a6a3abebb5223f45e52f3623f9d4ebc7d72a10d7e698c5e8405784123ee20b0a'
device2_address = '0x4167020fe858Dd5b2cc1cb812d917aa97D1A9cbC'

user1_prv = '6160662302861275ebd089eaaab260787993f475425f3ef1a47b387bdc87e90f'
user1_addr = '0x66a3a45be309143d2EF028EE5dDf1e51900ABf60'

user2_prv = '0xc0d90fe8c6273936aacfdea1dc00c0e3c7efd02cfb0143d98c19613ecf1f9862'
user2_addr = '0x39E44eBaE232083566163097D92218EB89Ac8655'

transaction_list = []


# With this function, a user can register a device.
# 'devicetype' (string) is the type of the device.
# 'deviceAddr' (address) is the address of the device.
# 'domainName' is the domain in which the device is registered.
# 'owner_prv_key' and 'owner_address' belong to the user and are needed to make the transaction.
def add_device(domainName, deviceAddr, devicetype, owner_prv_key, owner_address):
    nonce = web3.eth.getTransactionCount(owner_address)
    # call 'addDevice' function of the ID contract
    tx = id_contract.functions.addDevice(domainName, deviceAddr, devicetype).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Device Registration', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success', 'from': owner_address, 'to': id_contract_address,
                'input': {'device_type': devicetype, 'device_address': deviceAddr}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Device Registration', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed', 'from': owner_address, 'to': id_contract_address,
                'input': {'device_type': devicetype, 'device_address': deviceAddr}}
        return False, dict


# add_device('first_domain',device1_address,'light_sensor',admin_prv,admin_addr)
# add_device('first_domain',device1_address,'light_sensor',user1_prv,user1_addr)


######################################
# With this function, a user can register himself.
# 'role' (string) is the role of the user
# 'user_prv' and 'user_addr' belong to the user and are needed to make the transaction.
def add_User(role, user_prv, user_addr):
    nonce = web3.eth.getTransactionCount(user_addr)
    # call 'addUser' function of the ID contract
    tx = id_contract.functions.addUser(role).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=user_prv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Adding User', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success',
                'from': user_addr, 'to': id_contract_address, 'input': {'role': role}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Adding User', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed',
                'from': user_addr, 'to': id_contract_address, 'input': {'role': role}}
        transaction_list.append(dict)
        return False, dict


# add_User('test_user',user1_prv,user1_addr)
# add_User('worker',user2_prv,user2_addr)

###########################################################
# A user can add a policy for a device in his posession.
# 'device' is the address of the device.
# 'action' is the permitted action that can be done on the device (one of 'read','write','excecute').
# 'permitted_role' is the role that the requester should have.
# 'permitted_usage_times' (int) is the number of times the access will be granted.
# 'permitted_usage_duration' (int, in seconds) is the time interval during which the access will be granted. This interval begins upon the issuance of the access token.
# 'owner_addr' and 'owner_prv_key' belong to the user and are needed to make the transaction.
def add_user_policy(device, action, permitted_role, permitted_usage_times, permitted_usage_duration, owner_addr,
                    owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    # call 'add_user_policy' of the policy contract
    tx = policy_contract.functions.add_user_policy(device, action, permitted_role, permitted_usage_times,
                                                   permitted_usage_duration).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Creating Policy', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success', 'from': owner_addr, 'to': policy_contract_address,
                'input': {'device': device, 'action': action, 'permitted_role': permitted_role,
                          'permitted_usage_times': permitted_usage_times,
                          'permitted_usage_duration': permitted_usage_duration}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Creating Policy', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed', 'from': owner_addr, 'to': policy_contract_address,
                'input': {'device': device, 'action': action, 'permitted_role': permitted_role,
                          'permitted_usage_times': permitted_usage_times,
                          'permitted_usage_duration': permitted_usage_duration}}
        transaction_list.append(dict)
        return False, dict


# add_user_policy(device1_address,"read","user",24,1,account1_addr,account1_prv)


################################################################
# With this function, a user can specify another user as a special id for an action on a device in his posession, meaning that user has unconditional access for that action on that device.
# 'deivce' is the address of the deivce for which the id is specified.
# 'action' (string) is the action that the special id can perform on the device.
# 'owner_addr' and 'owner_prv_key' belong to the user and are needed to make the transaction.
def add_special_id(device, action, special_id, owner_addr, owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    # call 'add_special_id' of the policy contract
    tx = policy_contract.functions.add_special_id(device, action, special_id).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Adding Special Id', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success', 'from': owner_addr, 'to': policy_contract_address,
                'input': {'device': device, 'action': action, 'special_id': special_id}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Adding Special Id', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed', 'from': owner_addr, 'to': policy_contract_address,
                'input': {'device': device, 'action': action, 'special_id': special_id}}
        transaction_list.append(dict)
        return False, dict


# add_special_id(device1_address,"read",user1_addr,account1_addr,account1_prv)


###################################################################
# With this function, a user can request access token for an action on a device. If the user passes the policies, a token will be isseud for him in the token smart contract.
# 'requestedObjectAddress' is the address of the deivce that user wants the access token for.
# 'action' (string) is the action that the user wants to perform on the device.
# 'requestor_addr' and 'requestor_prv_key' belong to the user and are needed to make the transaction.
def tokenReq_ByUser(requestedObjectAddress, action, requestor_addr, requestor_prv_key):
    nonce = web3.eth.getTransactionCount(requestor_addr)
    # call 'accessReqByUser' of judge contract
    tx = judge_contract.functions.accessReqByUser(requestedObjectAddress, action,
                                                  token_contract_address).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=requestor_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Token Request', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success', 'from': requestor_addr, 'to': judge_contract_address,
                'input': {'requestedObjectAddress': requestedObjectAddress, 'action': action}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Token Request', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed',
                'from': requestor_addr, 'to': judge_contract_address,
                'input': {'requestedObjectAddress': requestedObjectAddress, 'action': action}}
        transaction_list.append(dict)
        return False, dict


# tokenReq_ByUser(device1_address,"read",user1_addr,user1_prv)


######################################################################
# With this function, a user can request to access a device and perform an action on it. The function looks for the associated token and if it exists, grants access to the user.
# 'requestedObjectAddress' is the address of the deivce that user wants to access.
# 'action' (string) is the action that the user wants to perform on the device.
# 'requestor_addr' is the address of the requetor user. Note that this function does not make a transaction, so private key is not needed.
def AccessDevice(requestedObjectAddress, action, requestor_addr):
    # query the token
    (token_existing, token_issuedate, token_expireddate, token_usage_times) = get_Token(requestor_addr,
                                                                                        requestedObjectAddress, action)
    now = int(time.time())
    # check the validity of the token
    if token_existing == True and now > token_issuedate and now < token_expireddate and token_usage_times > 0:
        nonce = web3.eth.getTransactionCount(token_supervisor_addr)
        # call 'usageCountDown' of token contract to record an access
        tx = token_contract.functions.usageCountDown(requestor_addr, requestedObjectAddress, action).buildTransaction(
            {'nonce': nonce, 'gas': 2000000})
        signed_tx = web3.eth.account.signTransaction(tx, private_key=token_supervisor_prv_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        if tx_receipt["status"] == 1:
            dict = {'hash': tx_hash.hex(), 'type': 'Access Request', 'block_number': tx_receipt["blockNumber"],
                    'Status': 'success', 'from': requestor_addr, 'to': token_contract_address,
                    'input': {'requestedObjectAddress': requestedObjectAddress, 'action': action}}
            transaction_list.append(dict)
            return True, dict
        else:
            dict = {'hash': tx_hash.hex(), 'type': 'Access Request', 'block_number': tx_receipt["blockNumber"],
                    'Status': 'failed', 'from': requestor_addr, 'to': token_contract_address,
                    'input': {'requestedObjectAddress': requestedObjectAddress, 'action': action}}
            transaction_list.append(dict)
            return False, dict
    else:
        return False, 'Access to device failed because of invalid token.'


# AccessDevice(device1_address, 'read',user2_addr)
# AccessDevice(device1_address, 'execute',user2_addr)

################################################################################################ list of all transactions
def GetAllTransactions():
    return transaction_list


#################################################################################################

# This function returns the transaction that registered devices belonged to the address 'owner_address'.
def GetDeviceTransactionsOfOwner(owner_address):
    device_transactions = [];
    for i in range(len(transaction_list)):
        if transaction_list[i]['type'] == 'Device Registration' and transaction_list[i]['from'] == owner_address:
            device_transactions.append(transaction_list[i])
    return device_transactions


# This function  returns the transaction that recorded policies for devices belonged to the address 'owner_address'.
def GetPolicyTransactionsOfOwner(owner_address):
    policy_transactions = [];
    for i in range(len(transaction_list)):
        if transaction_list[i]['type'] == 'Creating Policy' and transaction_list[i]['from'] == owner_address:
            policy_transactions.append(transaction_list[i])
    return policy_transactions


####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################    
############## The following functions are not invoked by the UI.

# With this function, a registered device can confirm its owner. In fact, this function should be invoke by the owner of the deivce, and from the IoT platform, to prove the ownership of the device. But, we put it here anyway.
# Unconfrmed devices are not recognized in the system. Owners cannot define policies for unconfirmed devices.
# 'deviceOwner' is the onwer of the device. This should match the owner that was previously recorded for the device by 'add_device' function.
# 'device_prv_key' and 'device_address' belong to the device and are needed to make the transaction.
def confirmDevice(deviceOwner, device_prv_key, device_address):
    nonce = web3.eth.getTransactionCount(device_address)
    # call 'confirmDevice' function of ID contract
    tx = id_contract.functions.confirmDevice(deviceOwner).buildTransaction({'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=device_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Device Confirmation', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success', 'from': device_address, 'to': id_contract_address,
                'input': {'device_owner': deviceOwner}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Device Confirmation', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed', 'from': device_address, 'to': id_contract_address,
                'input': {'device_owner': deviceOwner}}
        transaction_list.append(dict)
        return False, dict


# confirmDevice(account1_addr,device1_prv,device1_address)
# confirmDevice(user1_addr,device1_prv,device1_address)
# confirmDevice(user1_addr,device2_prv,device2_address)


# With this function, the attribute authority can confirm the registration of a user. Unconfirmed users cannot register devices and create policies for them.
# 'userAddress' is the address of the user to confirm.
# 'authority_prv' and 'authority_addr' belong to the attribute athority and are needed to make the transaction.
def confirm_user(authority_prv, authority_addr, userAddress):
    nonce = web3.eth.getTransactionCount(authority_addr)
    # call 'confirmUser' of ID contract
    tx = id_contract.functions.confirmUser(userAddress).buildTransaction({'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=authority_prv)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Conifrming User', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success', 'from': authority_addr, 'to': id_contract_address,
                'input': {'user_address': userAddress}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Confirming User', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed', 'from': authority_addr, 'to': id_contract_address,
                'input': {'user_address': userAddress}}
        transaction_list.append(dict)
        return False, dict


# confirm_user(attribute_authority_prv,attribute_authority_address,user1_addr)
# confirm_user(attribute_authority_prv,attribute_authority_address,user2_addr)


# This function returns the attributes of a device with address 'device_address'.
def getDeviceAttributes(device_address):
    (device_owner, device_type, device_domain, device_status) = id_contract.functions.getDeviceAttributes(
        device_address).call()
    return (device_owner, device_type, device_domain, device_status)


# getDeviceAttributes(device1_address)


######################################
# This function adds a domain named 'domainName'.
# 'user_prv_key' and 'user_address' belong to the user that makes this domain, and are neede to make the transaction.
def add_Domain(domainName, user_prv_key, user_address):
    nonce = web3.eth.getTransactionCount(user_address)
    # call 'addDomain' function in ID contract
    tx = id_contract.functions.addDomain(domainName).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=user_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        dict = {'hash': tx_hash.hex(), 'type': 'Adding Domain', 'block_number': tx_receipt["blockNumber"],
                'Status': 'success', 'from': user_address, 'to': id_contract_address,
                'input': {'domain_name': domainName}}
        transaction_list.append(dict)
        return True, dict
    else:
        dict = {'hash': tx_hash.hex(), 'type': 'Adding Domain', 'block_number': tx_receipt["blockNumber"],
                'Status': 'failed',
                'from': user_address, 'to': id_contract_address, 'input': {'domain_name': domainName}}
        transaction_list.append(dict)
        return False, dict


# add_Domain('first_domain',admin_prv,admin_addr)


##################################################
# This function deletes a device. Only the owner of a deivice can delete it.
# 'deviceAddr' is the address of the device to be deleted.
# 'owner_addr' and 'owner_prv_key' belong to the owner, and are neede to make the transaction.
def delete_device(deviceAddr, owner_addr, owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = id_contract.functions.deleteDevice(deviceAddr).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        return ('device is deleted successfully.', tx_hash)
    else:
        return ('deleting failed.', tx_hash)
        pprint.pprint(dict(tx_receipt))


# delete_device(device1_address,admin_addr,admin_prv)


############################################################
# This function returns the owner of a deivice with address 'device_address'.
def get_Device_Owner(device_address):
    owner_adr = id_contract.functions.getDeviceOwner(device_address).call()
    return owner_adr


# get_Device_Owner(device1_address)
# get_Device_Owner(device2_address)


###################################################################
# This function returns the information on a domain with the name 'domainName'.
def get_Domain(domainName):
    (domain_created, domain_owner, domain_deviceAddr) = id_contract.functions.getDomain(domainName).call()
    return (domain_created, domain_owner, domain_deviceAddr)


# get_Domain("first_domain")


###################################################################
# This function returns the attributes of a user with the address 'userAddr'. The attributes include the role and confirmation status of the user.
def get_User_Attributes(userAddr):
    (user_role, user_status) = id_contract.functions.getUserAttributes(userAddr).call()
    return (user_role, user_status)


# get_User_Attributes(user1_addr)
# get_User_Attributes(user2_addr)
# get_User_Attributes(admin_addr)


###################################################################
# This function returns information about a token.
# 'token_holder' is the address of the owner of the token.
# 'object_adr' is the address of the device that token gives access to.
# 'action' is the action that token allows to be performed on the device.
# These parameter define an access token.
def get_Token(token_holder, object_adr, action):
    (token_existing, token_issuedate, token_expireddate, token_usage_times) = token_contract.functions.getToken(
        token_holder, object_adr, action).call()
    return (token_existing, token_issuedate, token_expireddate, token_usage_times)


# get_Token(user1_addr,device1_address,"read")
# get_Token(user2_addr,device1_address,"read")
# get_Token(user2_addr,device1_address,"execute")

###################################################################
# With this function, a user can delete a special id for a device in his possession.
# 'device' is the address of the deivce that special id had access to.
# 'action' (string) is the action that special id could perform on the device.
# 'special_id' is the address of the special id.
# 'owner_addr' and 'owner_prv_key' belong to the owner of the device, and are needed to make the transaction.
def remove_special_id(device, action, special_id, owner_addr, owner_prv_key):
    nonce = web3.eth.getTransactionCount(owner_addr)
    tx = policy_contract.functions.remove_special_id(device, action, special_id).buildTransaction(
        {'nonce': nonce, 'gas': 2000000})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=owner_prv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt["status"] == 1:
        return ('special id is removed successfully.', tx_hash)
    else:
        return ('removing special id failed.', tx_hash)
        pprint.pprint(dict(tx_receipt))


# remove_special_id(device1_address,"read",user1_addr,account1_addr,account1_prv)


########################################################################
# This function returns the number of policies set for an action on a device.
# 'owner' is the address of the owner of the device.
# 'device' is the address of the device.
# 'action' (string) is the action.
def get_user_policy_size(owner, device, action):
    policy_length = policy_contract.functions.get_user_policy_size(owner, device, action).call()
    return policy_length


# get_user_policy_size(account1_addr,device1_address,"read")
# get_user_policy_size(user1_addr,device2_address,"read")
# get_user_policy_size(user1_addr,device2_address,"execute")

#########################################################################
# This function returns the number of special ids set for an action on a device.
# 'owner' is the address of the owner of the device.
# 'device' is the address of the device.
# 'action' (string) is the action.
def get_special_list_size(owner, device, action):
    list_length = policy_contract.functions.get_special_list_size(owner, device, action).call()
    return list_length


# get_special_list_size(account1_addr,device1_address,"read")


################################################
# This function returns the a policy set for an action on a device.
# hash is the hash of the concatenation of 'owner', 'device' and 'action'.
# 'num' is the number of the policy to query.
def get_User_Policy(Hash, num):
    (policy_role, policy_usage_times, policy_usage_duration) = policy_contract.functions.get_User_Policy(Hash,
                                                                                                         num).call()
    return (policy_role, policy_usage_times,
            policy_usage_duration)

# hash = web3.solidityKeccak(['address','address','string'], [user1_addr,device1_address, 'read'])
# get_User_Policy(hash,0)
