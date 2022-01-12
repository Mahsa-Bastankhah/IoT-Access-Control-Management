# IoT-Access-Control-Management
In this work, we implemented an attribute-based access control management system for IoT devices. We used blockchain technology to guarantee the transparency of the access grant process. And also we use the blockchain to keep the record of all the access requests.
## Elements
The elements of our designs are as follows:
1) IoT devices: The devices let anyone with a valid token use them.
2) users: users request access to the devices and pay for them.
3) device owners: they enter the specification of the device in the smart ID contract. The owner of the device decides about the policies who can access their device.
## Workflow
The policies of accessing devices are stored on the blockchain("policy-contract") and are available to everyone. When a new user sends an access request to the blockchain, the "judge-contract"
checks if the user's attributes meet the requirements stored on policy-contract. If the user was eligible, the judge contract sends a token mint request to the "token-contract". The token-contract mints a new token for the user and stores it on the blockchain. Then the user can send an access request to the device. The device checks the validity of the user's token on the blockchain and if the token was valid, grants access to the user. 
