//author Mahsa Bastankhah

const Token_contract = artifacts.require("Token_contract");


contract("Token_contract", accounts => {

it("should initialize a token", async () => {
	const instance = await Token_contract.new({from: accounts[0]});
	const recipient = accounts[1];
	const object = accounts[8];
	const duration_sec = 100;
	const numOfUses = 10;
	
	const result = await instance.initialize(recipient, object , duration_sec, numOfUses , { from: accounts[0] });
	
	const token = await instance.getTokenStatus(recipient);
	//console.log(token);
	assert.equal(token[0].toNumber() , 1);
	assert.equal(token[1] , true);
	assert.equal(token[2] , false);
	assert.equal(token[5].toNumber() , numOfUses);

});

it("should prevent initializing a token by someone but judge smart contract", async () => {
	const instance = await Token_contract.new({from: accounts[0]});
	const recipient = accounts[1];
	const object = accounts[8];
	const duration_sec = 100;
	const numOfUses = 10;
	
	try{
		await instance.initialize(recipient, object , duration_sec, numOfUses , { from: accounts[1] });
		assert.fail();
	}
	catch(error){
		const preventFound = error.message.search('prevent') >= 0;
		assert(!preventFound, `${error}`);
		return;}
	assert(false);

});

it("should make a token valid", async () => {
	const instance = await Token_contract.new({from: accounts[0]});
	const recipient = accounts[1];
	const object = accounts[8];
	const duration_sec = 100;
	const numOfUses = 10;
	
	await instance.initialize(recipient, object , duration_sec, numOfUses , { from: accounts[0] });
	await instance.setAttributeToken_isValid(recipient, true , { from: accounts[0] }) 
	
	const token = await instance.getTokenStatus(recipient);
	//console.log(token);
	assert.equal(token[0].toNumber() , 2);
	assert.equal(token[2] , true);
});


it("should change the number of use attribute", async () => {
	const instance = await Token_contract.new({from: accounts[0]});
	const recipient = accounts[1];
	const object = accounts[8];
	const duration_sec = 100;
	const numOfUses = 10;
	const newNumOfUses = 30;
	
	await instance.initialize(recipient, object , duration_sec, numOfUses , { from: accounts[0] });
	await instance.setAttributeToken_permissiblenumberofuses(recipient, newNumOfUses , { from: accounts[0] }) 
	
	const token = await instance.getTokenStatus(recipient);
	//console.log(token);
	assert.equal(token[0].toNumber() , 2);
	assert.equal(token[5].toNumber() , newNumOfUses);
});



it("should change the number of uses after a single use of token", async () => {
	const instance = await Token_contract.new({from: accounts[0]});
	const recipient = accounts[1];
	const object = accounts[8];
	const duration_sec = 100;
	const numOfUses = 10;
	
	await instance.initialize(recipient, object , duration_sec, numOfUses , { from: accounts[0] });
	await instance.setAttributeToken_UsedaSingleTime(recipient, { from: accounts[0] }) 
	
	const token = await instance.getTokenStatus(recipient);
	//console.log(token);
	assert.equal(token[0].toNumber() , 2);
	assert.equal(token[5].toNumber() , numOfUses - 1);
});





});
