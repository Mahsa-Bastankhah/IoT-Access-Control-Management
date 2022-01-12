const ID_contract = artifacts.require('ID_contract');

contract('ID_contract' , accounts => {
	
it("it should add a domain", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	//let logs = call.logs;
	let domain = await instanse.getDomain(domainName);
	assert.equal(domain[0], true);
	assert.equal(domain[1] , accounts[1]);
	
	let device = await instanse.devices(accounts[2]);
	assert.equal(device[2].toNumber(), 0);
	assert.equal(device[4] , true);
	
	let attribute = await instanse.getAttributes(accounts[2]);
	assert.equal(attribute[0] , owner);
	assert.equal(attribute[1] , "sensor");
	assert.equal(attribute[2] , domainName);		

});
  
  
  
  
  
  
  
it("it should prevent non admin user to add domain", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];
	try{
		await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[1]});
		assert.fail();
	}
	catch(error){
		assert(error.message.includes('Caller is not admin'));
		return;}
	assert(false);
});
	
	
	
	
	
it("it should prevent adding an existing domain", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	try{
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	assert.fail();
	}
	catch(error){
		assert(error.message.includes('This domain already exists'));
		return;}
	
	assert(false);
});
	
	
	
	
	
it("it should add device", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
										
	await instanse.addDevices(domainName, [accounts[4] , accounts[5]],["actuator" , "actuator"],
										{ from: owner});
										
	let device = await instanse.devices(accounts[4]);
	assert.equal(device[2].toNumber(), 0);
	assert.equal(device[4] , true);
	
	let attribute = await instanse.getAttributes(accounts[4]);
	assert.equal(attribute[0] , owner);
	assert.equal(attribute[1] , "actuator");
	assert.equal(attribute[2] , domainName);		

});






it("it should prevent any user but owner domain to add device", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	try{
		await instanse.addDevices(domainName, [accounts[4] , accounts[5]],["actuator" , "actuator"],
										{ from: accounts[3]});
		assert.fail();
	}
	catch(error){
		assert(error.message.includes("Caller is not the domain owner"));
		return;}
	assert(false);
});




it("it should prevent from adding device to a non existing domain", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	try{
		await instanse.addDevices(domainName, [accounts[4] , accounts[5]],["actuator" , "actuator"],
										{ from: accounts[1]});
		assert.fail();
	}
	catch(error){
		
		assert(error.message.includes("Caller is not the domain owner")); 
		// this call creates above error ealier than not existing domain error
		return;}
	assert(false);
});




it("it should add a device and then the device should confirm its owner", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	await instanse.confirmation(domainName , owner , { from: accounts[2]});
										
	let device = await instanse.devices(accounts[2]);
	assert.equal(device[2].toNumber(), 1);	

});




it("it shouldn't let a non added device to be confirmed", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	
	try{
		await instanse.confirmation(domainName , owner , { from: accounts[4]});
		assert.fail();
	}
	catch(error){
		return;}
	assert(false);	
});



it("it shouldn prevent the device from confirm to a wrong owner", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	
	try{
		await instanse.confirmation(domainName , accounts[3] , { from: accounts[2]});
		assert.fail();
	}
	catch(error){
		assert(error.message.includes("Owner address doesn't match")); 
		return;}
	assert(false);	
});



it("it shouldn prevent the device from confirm to a wrong domainName", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainNameA = "domain_A";
	const domainNameB = "domain_B";
	const owner = accounts[1];	
	await instanse.addDomain(domainNameA, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	await instanse.addDomain(domainNameB, owner, [accounts[4] , accounts[5]],["sensor" , "sensor"],
										{ from: accounts[0]});
	
	try{
		await instanse.confirmation(domainNameB , owner , { from: accounts[2]});
		assert.fail();
	}
	catch(error){
		return;}
	assert(false);	
});
	
	



it("owner delegates the device to a user and then the new delegatee delegates it to another user", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	const delegatee = accounts[6];
	const nextDelegatee = accounts[7];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	await instanse.confirmation(domainName , owner , { from: accounts[2]});
	await instanse.delegateDevice(accounts[2], delegatee,{ from: owner});
	
	let device = await instanse.devices(accounts[2]);
	assert.equal(device[3] , delegatee , "the first delegation didn't happen");	
	
	
	await instanse.delegateDevice(accounts[2], nextDelegatee,{ from: delegatee});
	device = await instanse.devices(accounts[2]);
	assert.equal(device[3] , nextDelegatee , "the second delegation didn't happen");	
});



it("it should prevent to delegate a non confirmed device", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	const delegatee = accounts[6];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	try{
		await instanse.delegateDevice(accounts[2], delegatee,{ from: owner});
		assert.fail();
	}
	catch(error){
		assert(error.message.includes("This device hasn't confirmed yet")); 
		return;}
	assert(false);	
});


it("it should prevent a non eligible user from delegating the device", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	const delegatee = accounts[6];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	await instanse.confirmation(domainName , owner , { from: accounts[2]});
	
	try{
		await instanse.delegateDevice(accounts[2], delegatee,{ from: accounts[7]});
		assert.fail();
	}
	catch(error){
		const preventFound = error.message.search('prevent') >= 0;
		assert(!preventFound, `${error}`);
		return;}
	assert(false);	
});



it("it should modify a device", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	const delegatee = accounts[6];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
										
	await instanse.modifyDeviceAttr(accounts[2] , "actuator",{ from: owner});
	let attribute = await instanse.getAttributes(accounts[2]);
	assert.equal(attribute[1] , "actuator");

});


it("it should prevent a non owner or delegatee user to modify the device", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	const delegatee = accounts[6];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
	try{
		await instanse.modifyDeviceAttr(accounts[2] , "actuator",{ from: accounts[6]});
		assert.fail();
	}
	catch(error){
		const preventFound = error.message.search('prevent') >= 0;
		assert(!preventFound, `${error}`);
		return;}
	assert(false);	

});


it("it should delete a device", async () => {
	const instanse = await ID_contract.new({from: accounts[0]});
	const domainName = "domain_A";
	const owner = accounts[1];	
	const delegatee = accounts[6];
	await instanse.addDomain(domainName, owner, [accounts[2] , accounts[3]],["sensor" , "sensor"],
										{ from: accounts[0]});
										
	await instanse.deleteDevice(accounts[2] , { from: owner});
	let device = await instanse.devices(accounts[2]);
	assert.equal(device[4] , false);
});


	
  
  
  
  
});
