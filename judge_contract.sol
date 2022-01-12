//@author Setareh Ghorshi

pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;
import "./Token_contract.sol";
import "./ID_contract.sol";
import "./policy_contract.sol";

contract judge_contract{

	/*
	other contracts 
	*/
    ID_contract public idContract;
	policy_contract public policyContract;
    Token_contract public tokenContract;
    uint device_policy_size;
    uint user_policy_size;
	uint special_list_size;
	address public idAddr;
	address public policyAddr;
	address public tokenAddr;
    
	/*
        Function: Initialize contracts and addresses
        inputs:
            IDadmin: the id of the admin 
            attributeAuthority: the address of the attribute authority
    */
	constructor (address IDadmin, address attributeAuthority) public{
	    idContract = new ID_contract(IDadmin, attributeAuthority);
	    policyContract = new policy_contract(address(idContract));
		idAddr = address(idContract);
		policyAddr = address(policyContract);

	}


    /*
        Function: Takes access requests from a device and issues tokens.
        input:
            requestedObjectAddress: the address of the object to be accessed
            action: (read, write, ...)
        output:
            true if a token is initiates, false otherwise.
    */
	function accessReqByDevice(address requestedObjectAddress, string memory action) public returns(bool){
	    
	    //Gets attributes of subject and object devices from the id contract.
	    (address subject_owner , string memory subject_device_type , string memory subject_domain, bool subject_status) = idContract.getDeviceAttributes(msg.sender);
	    (address object_owner , , , bool object_status ) = idContract.getDeviceAttributes(requestedObjectAddress);
	    
        //only confirmed devices 
	    require(subject_status==true && object_status ==true); 
	    
	    device_policy_size = policyContract.get_device_policy_size(object_owner,requestedObjectAddress,action);
	    special_list_size = policyContract.get_special_list_size(object_owner,requestedObjectAddress,action);
	    
	    bytes32 owner_object_action_hash = keccak256(abi.encodePacked(object_owner,requestedObjectAddress,action)); 
	    bytes32 holder_object_action_hash = keccak256(abi.encodePacked(msg.sender,requestedObjectAddress,action)); 
	    
	    // check special ids first
	    for (uint256 i=0; i<special_list_size ; i++){
	       
	    address special_id = policyContract.special_list_map(owner_object_action_hash,i); 
	    // issues token for special ids
	    if (msg.sender == special_id){
	        
	        tokenContract.issueToken(holder_object_action_hash,100, 100000);
	        
	        return true;}
	        
	    }
    // Issues token regarding policies
	   for (uint256 j=0 ; j<device_policy_size ; j++){
	       
	   (address policy_owner , string memory policy_device_type , string memory policy_domain, uint policy_usage_times, uint policy_usage_duration) = policyContract.get_Device_Policy(owner_object_action_hash,j);
	   
	   if (subject_owner == policy_owner && keccak256(abi.encodePacked(subject_device_type)) == keccak256(abi.encodePacked(policy_device_type)) && keccak256(abi. encodePacked(subject_domain)) == keccak256(abi. encodePacked(policy_domain))){
	       
	    tokenContract.issueToken(holder_object_action_hash, policy_usage_times, policy_usage_duration);
	        return true;}
	    
	    }
	    return false;
	    
	    
	}

	    
/*
    Function: Takes access requests from a user and issues tokens.
    input:
        requestedObjectAddress: the address of the object to be accessed
        action: (read, write, ...)
        token_contract_address: the address of the token contract
    output:
        true if a token is initiates, false otherwise.
*/	    
function accessReqByUser(address requestedObjectAddress, string memory action, address token_contract_address) public returns(bool)	{
	    //Gets attributes of subject and object devices from the id contract.
	    (string memory subject_role, bool subject_status) = idContract.getUserAttributes(msg.sender);
	    (address object_owner ,  , , bool object_status ) = idContract.getDeviceAttributes(requestedObjectAddress);
	    
	    require(subject_status==true && object_status ==true); //only confirmed device and user 
	    
	    tokenContract = Token_contract(token_contract_address);
	    
	    user_policy_size = policyContract.get_user_policy_size(object_owner,requestedObjectAddress,action);
	    special_list_size = policyContract.get_special_list_size(object_owner,requestedObjectAddress,action);
	    
	    bytes32 owner_object_action_hash = keccak256(abi.encodePacked(object_owner,requestedObjectAddress,action));
	    bytes32 holder_object_action_hash = keccak256(abi.encodePacked(msg.sender,requestedObjectAddress,action)); 
	   
	    
	    // check special ids first
	    for (uint256 i=0; i<special_list_size ; i++){
	       
	    address special_id = policyContract.special_list_map(owner_object_action_hash,i); 
	     
	    if (msg.sender == special_id){
	        
	        tokenContract.issueToken(holder_object_action_hash, 100,10000);
	        
	        return true;}
	    }
	    
	    // Issues token regarding policies
	    for (uint256 j=0 ; j< user_policy_size ; j++){
	       
	   (string memory policy_role, uint policy_usage_times, uint policy_usage_duration) = policyContract.get_User_Policy(owner_object_action_hash,j);
	   
	   if (keccak256(abi.encodePacked(subject_role)) == keccak256(abi.encodePacked(policy_role))){
	       
	         tokenContract.issueToken(holder_object_action_hash,policy_usage_times,policy_usage_duration);
	         
	        return true;}
	    
	    }
	    return false;  
	   
	}
	
	
	    
}
