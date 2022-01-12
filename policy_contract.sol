pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

import "./ID_contract.sol";

contract policy_contract{
    ID_contract ID; 
    //this mapping is used to specify the permitted attributes of the devices that want to access another device
    mapping (bytes32 => device_attr_const[]) public device_attr_const_map; 
    //this mapping is used to specify the permitted attributes of the users that want to access a device
    mapping (bytes32 => user_attr_const[]) public user_attr_const_map;
    mapping (bytes32 => address[]) public special_list_map; // includes special ids of both devices and users
    string[3] actions = ['read','write','execute']; // possible actions for each object
    
    
    constructor(address id_contract_address) public{
        ID = ID_contract(id_contract_address);
    }
    
    
    
    // Attributes and constraints are both in this struct. This struct is basically a policy. In a policy, attributes
    // specify the conditions that should be met prior to issuance of an access token. On the other hand, contsraints 
    // specify conditions on some parameters when the access token is being used.
    struct device_attr_const{
        address owner;
        string device_type; // humidity sensor, motion sensor, light sensor, actuator, ...
        string domain; // for example domain A, B, ...
        uint usage_times; // the maximum number of times that access will be granted for one access token
        uint usage_duration;  // for example, [time1, time2, time3, time4] means that access time should be either 
                                // between time1 and time2, ot between time3 and time4.
        // We can add more attributes like:
        // string manufacturer;
        // string network_address; // can be IP address, or mac adreess, or other addresses in the network.
                                
    }
    
    struct user_attr_const{
        string role;
        uint usage_times; //The number of times the user is valid to use the device
        uint usage_duration; // The time interval whithin which the user is valid to use the device
        // uint[] time_intervals;
    }
    
    
    /*
    function: owner adds policies for a device
    inputs: 
        device: the address of the device to have access
        action: the type of action
        permitted_owner: owner of the device to have access
        permitted_device_type: type of the device (camera, actuator, motion sensor, ...)
        permitted_domain_name: the domain which the device belongs to.
        permitted_usage_times: the valid number of times for the access 
        permitted_usage_duration: the valid time interval(s) for the access 
    output:
        true if sucessfully pushed the policy in the mapping for device attributes
    */
    function add_device_policy(address device, string memory action, address permitted_owner, 
            string memory permitted_device_type, string memory permitted_domain_name, uint permitted_usage_times, uint permitted_usage_duration) 
                         public returns (bool){
        address device_owner = ID.getDeviceOwner(device);  // get the address of the owner of the device to be accessed
        require(msg.sender == device_owner); // the caller of the function should be the owner of the device to be accessed
        require(is_valid_action(action)); // checks if the action is valid
        device_attr_const memory permitted_device_attr_const = device_attr_const(permitted_owner, permitted_device_type, permitted_domain_name, permitted_usage_times, permitted_usage_duration);
        //pushes the new attributes to the list of devices who can access to the device
        device_attr_const_map[keccak256(abi.encodePacked(device_owner,device,action))].push(permitted_device_attr_const); 
        return true;
    }
    
    
    /*
    function: owner adds policies for a user
    inputs: 
        device: the address of the device to have access
        action: the type of action
        permitted_role: role of the user.
        permitted_usage_times: the valid number of times for the access 
        permitted_usage_duration: the valid time interval(s) for the access 
    output:
        true if sucessfully pushed the policy in the mapping for user attributes
    */
    function add_user_policy(address device, string memory action, string memory permitted_role, uint permitted_usage_times, uint permitted_usage_duration) 
                         public returns (bool){
        address device_owner = ID.getDeviceOwner(device);  // get the address of the owner of the device to be accessed
        require(msg.sender == device_owner); // the caller of the function should be the owner of the device to be accessed
        require(is_valid_action(action)); // checks if the action is valid
        user_attr_const memory permitted_user_attr_const = user_attr_const(permitted_role, permitted_usage_times, permitted_usage_duration);
        //pushes the new attributes to the list of users who can access to the device
        user_attr_const_map[keccak256(abi.encodePacked(device_owner,device,action))].push(permitted_user_attr_const);
        return true;
    }
    
    
    /*
    function: owner removes a policy
    input:
        device: the address of the device
        action: The permitted action of the policy 
        policy_index: the index of the policy in the list
    output:
        true if successfully removed the policy false otherwise.
    */
    function remove_policy(address device, string memory action, uint policy_index) 
                        public returns (bool){
        address device_owner = ID.getDeviceOwner(device);  // get the address of the owner of the device to be accessed
        require(msg.sender == device_owner); // the caller of the function should be the owner of the device to be accessed
        require(is_valid_action(action)); // checks if the action is valid
        // the policy index should be within the range of the length of the policy list
        if (policy_index <= device_attr_const_map[keccak256(abi.encodePacked(device_owner,device,action))].length){
            delete device_attr_const_map[keccak256(abi.encodePacked(device_owner,device,action))][policy_index] ; //removes the policy from the list
            return true;
        }
        return false;
        
    }
                        




    /*
    function: owner adds a special id
    input:
        device: the address of the device to be accessed
        action: The permitted action 
        special_id: the address of the special id to access the device
    output:
        True if successfully added the special id false otherwise.
    */
    function add_special_id(address device, string memory action, address special_id) public returns(bool){
        address device_owner = ID.getDeviceOwner(device);  // get the address of the owner of the device to be accessed
        require(msg.sender == device_owner); // the caller of the function should be the owner of the device to be accessed
        require(is_valid_action(action));  // checks if the action is valid
        special_list_map[keccak256(abi.encodePacked(device_owner,device,action))].push(special_id); // adds the special id to the list
        return true;
    }
    
    
    
    /*
    function: owner removes a special id
    input:
        device: the address of the device to be accessed
        action: The permitted action 
        special_id: the address of the special id to access the device
    output:
        True if successfully removed the special id false otherwise.
    */
     function remove_special_id(address device, string memory action, address special_id) public returns(bool){
        address device_owner = ID.getDeviceOwner(device);  // get the address of the owner of the device to be accessed
        require(msg.sender == device_owner); // the caller of the function should be the owner of the device to be accessed
        require(is_valid_action(action));  // checks if the action is valid
        uint id_index ;
        bool found = false;
        for (uint i=0; i<special_list_map[keccak256(abi.encodePacked(device_owner,device,action))].length; i++){
            if(special_list_map[keccak256(abi.encodePacked(device_owner,device,action))][i] == special_id){// checks if the special id matches the one to remove
                id_index = i;
                found = true;
                break;
            }
        }
        if(!found){// checks if the special id exists within the list
            return false;
        }else{
            delete special_list_map[keccak256(abi.encodePacked(device_owner,device,action))][id_index] ; //deletes the special id
        }
        return true;
    }
    
    
    /*
    function: checks if an action is valid
    input:
        action: the action to be checked
    output:
        true if the action is valid false otherwise.
    */
    function is_valid_action(string memory action) internal view returns(bool){
        for (uint i=0; i<actions.length; i++){
            if (keccak256(abi.encodePacked(actions[i])) == keccak256(abi.encodePacked(action))){ //string comparison
                return true;
            }
        }
        return false;
    }
    
    
    /*
    function: gets the size of the policy of the device
    input:
        owner: the owner of the device to be accessed
        device: the address of the device to be accessed
        action: The permitted action
    output:
        the size of the policy list of the device.
    */
    function get_device_policy_size(address owner, address device, string memory action) public view returns(uint){
        return device_attr_const_map[keccak256(abi.encodePacked(owner,device,action))].length;
    }
    
    /*
    function: gets the size of the policy of the user
    input:
        owner: the owner of the device to be accessed
        device: the address of the device to be accessed
        action: The permitted action
    output:
        the size of the policy list of the user.
    */
    function get_user_policy_size(address owner, address device, string memory action) public view returns(uint){
        return user_attr_const_map[keccak256(abi.encodePacked(owner,device,action))].length;
    }
    
    /*
    function: gets the number of the special ids
    input:
        owner: the owner of the device to be accessed
        device: the address of the device to be accessed
        action: The permitted action
    output:
        the size of the special id list.
    */
    function get_special_list_size(address owner, address device, string memory action) public view returns(uint){
        return special_list_map[keccak256(abi.encodePacked(owner,device,action))].length;
    }
    
    /*
    function: gets the policies of the device
    input:
        hash: The hash of the device owner, device address and the action
        num: the index of the policy in the list
    output:
        the policy related to the device
    */
    function get_Device_Policy(bytes32 hash, uint256 num) public view returns(address,string memory,string memory,uint,uint){
        
        return (device_attr_const_map[hash][num].owner,device_attr_const_map[hash][num].device_type,device_attr_const_map[hash][num].domain,device_attr_const_map[hash][num].usage_times, device_attr_const_map[hash][num].usage_duration); 
        //,device_attr_const_map[hash][num].time_intervals);
    }
    
    /*
    function: gets the policies of the user
    input:
        hash: The hash of the device owner, device address and the action
        num: the index of the policy in the list
    output:
        the policy related to the user
    */
    function get_User_Policy(bytes32 hash, uint256 num) public view returns(string memory, uint, uint){
        
        return (user_attr_const_map[hash][num].role, user_attr_const_map[hash][num].usage_times, user_attr_const_map[hash][num].usage_duration); 
    }
    
    
}    
