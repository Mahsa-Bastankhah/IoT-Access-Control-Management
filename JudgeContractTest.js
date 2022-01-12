const judge_contract = artifacts.require('judge_contract');
const id_contract = artifacts.require('ID_contract');
const token_contract = artifacts.require('token_contract');
const policy_contract = artifacts.require('policy_contract');
contract ('judge_contract',accounts =>{

    it('test1_deploy', async()=>{
        const Judge_contract = await judge_contract.new(accounts[6]);
        console.log(Judge_contract.address);
        assert(Judge_contract.address !== '');
        });
    it('test2_request', async()=>{
        ///// create needed data in other contracts
        const Judge_contract = await judge_contract.new(accounts[6]);
        var Policy_contract="";
        var Token_contract="";
        var ID_contract="";
        return await Judge_contract.policyAddr.call().then(async function(result){
         Policy_contract = await policy_contract.at(result);
         return await Judge_contract.tokenAddr.call().then(async function(result){
            
            Token_contract = await token_contract.at(result);
            return await Judge_contract.idAddr.call().then(async function(result){
           
                ID_contract = await id_contract.at(result);
                await ID_contract.addDomain("test", accounts[0], [accounts[1]],["sensor"],
                                        { from: accounts[6]});
        await ID_contract.addDomain("test2", accounts[5], [accounts[3]],["sensor"],
                                        { from: accounts[6]});
        await ID_contract.addDomain("test3", accounts[5], [accounts[4]],["sensor"],
										{ from: accounts[6]});
        const policy = {owner : accounts[5], device_type: "sensor" , domain:"test2", usage_times : 3, time_intervals:[2]};
        await Policy_contract.add_policy(accounts[1],"read",policy,{from: accounts[0]});
        await Policy_contract.add_special_id(accounts[1],"read",accounts[2],{from:accounts[0]});
       
        ///// both requests should be accepted
        await Judge_contract.accessReq.call(accounts[1],"read",{from:accounts[3]});  
        await Judge_contract.accessReq.call(accounts[1],"read",{from:accounts[2]});
              
       
        })
        
        
               });

           });
        });
        
        
        
        
    
        });
