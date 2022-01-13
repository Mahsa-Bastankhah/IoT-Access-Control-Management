# IoT-Access-Control-Management
In this work, we implemented an attribute-based access control management system for IoT devices. We used blockchain technology to guarantee the transparency of the access grant process. And also we use the blockchain to keep the record of all the access requests.
## Elements
The elements of our designs are as follows:
1) IoT devices: The devices let anyone with a valid token access them.
2) Users: The user submit their access request to the blockchain. If the request was successful a new token in minted for the user that can be used later to access the device.
3) Device owners: They enter the specification of the device in the ID-contract. The owner of the device decides about the policies that define who can access their device.
## Workflow
Our systems is consists of 4 contracts:
1) ID-contract
2) Policy-contract
3) Judge-contract
4) Token-contract

The attributes of new users and new devices are stored on the ID contract. 
The policies that define who can have access to which devices are stored on the policy-contract and are available to everyone. When a new user sends an access request to the blockchain, the judge-contract
checks if the user's attributes meet the requirements stored on policy-contract. If the user was eligible, the judge contract sends a token mint request to the token-contract. The token-contract mints a new token for the user and stores it on the blockchain. Then the user can send an access request to the device. The device checks the validity of the user's token on the blockchain and if the token was valid, grants access to the user. 
