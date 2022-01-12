pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract Token_contract {


address public Judge_sc;
	/*
		Define struct to represent role based token data.
	*/
	struct AttributeToken {
		address object;
		uint id;					// token id
		bool initialized;			// check whether token has been initialized
		bool isValid;				// flage to indicate whether token valid, used for temporary dispense operation
		uint256 issuedate;			// token issued date
		uint256 expireddate;		// token expired date
		uint256 permissiblenumberofuses;
	}

	// Global state variables
	//address private Judge_sc = address(judgeContract);
	mapping(address => AttributeToken) attributetokens;

	// event handle function
	event OnValueChanged(address indexed _from, uint _value);

	/*
	Function: Initilized token data given address.
	*/
	
	constructor() public{
	    Judge_sc = msg.sender;
	    
	}
	function initialize(address recipient, address object, uint256 duration_sec, uint256 permissiblenumberofuses) public {
            
			//set id and initialized flag
			require(msg.sender == Judge_sc);
			attributetokens[recipient].id = 1;
			attributetokens[recipient].initialized = true;
			attributetokens[recipient].object = object;
			attributetokens[recipient].issuedate = now;
			attributetokens[recipient].expireddate = now + duration_sec;
			attributetokens[recipient].permissiblenumberofuses = permissiblenumberofuses;
			//disable token
			attributetokens[recipient].isValid = false;

			// notify OnValueChanged event
			emit OnValueChanged(recipient, attributetokens[recipient].id);	
			

	}

	/* 
		function: query token data given address and return general token data
	*/
	function getTokenStatus(address recipient) public view returns (uint, 
																			bool, 
																			bool, 
																			uint256, 
																			uint256,
																			uint256) {
			return(	attributetokens[recipient].id, 
					attributetokens[recipient].initialized,
					attributetokens[recipient].isValid,
					attributetokens[recipient].issuedate,
					attributetokens[recipient].expireddate,
					attributetokens[recipient].permissiblenumberofuses
					);
	}

	// Set isValid flag call function
	function setAttributeToken_isValid(address recipient, bool isValid) public  {
		require(msg.sender == Judge_sc);
			attributetokens[recipient].id += 1;
			attributetokens[recipient].isValid = isValid;
			emit OnValueChanged(recipient, attributetokens[recipient].id);

		
	}

	// Set time limitation call function
	function setAttributeToken_expireddate(address recipient, 
									uint256 issueddate, 
									uint256 expireddate) public  {
		require(msg.sender == Judge_sc);
			attributetokens[recipient].id += 1;
			attributetokens[recipient].issuedate = issueddate;
			attributetokens[recipient].expireddate = expireddate;
			emit OnValueChanged(recipient, attributetokens[recipient].id);

	}

	// Set permissible number of uses
	function setAttributeToken_permissiblenumberofuses(address recipient, 
									uint256 permissiblenumberofuses) public  {
	require(msg.sender == Judge_sc);
			attributetokens[recipient].id += 1;
			attributetokens[recipient].permissiblenumberofuses = permissiblenumberofuses;
			emit OnValueChanged(recipient, attributetokens[recipient].id);
	
	}

	// Reduce permissible number of uses after using the Token
	function setAttributeToken_UsedaSingleTime(address recipient) public {
		require(msg.sender == Judge_sc);
			attributetokens[recipient].id += 1;
			attributetokens[recipient].permissiblenumberofuses = attributetokens[recipient].permissiblenumberofuses - 1;
			emit OnValueChanged(recipient, attributetokens[recipient].id);

	}

}
