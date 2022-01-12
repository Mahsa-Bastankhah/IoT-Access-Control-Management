//author Setareh Ghorshi
const id_contract = artifacts.require('ID_contract');
const policy_contract = artifacts.require('policy_contract');
const { soliditySha3 } = require("web3-utils");
contract ('policy_contract',accounts  =>{

    it('test1_deploy', async()=>{
        const ID_contract = await id_contract.new(accounts[4]);
        const Policy_contract = await policy_contract.new(ID_contract.address);
        console.log(Policy_contract.address);
        assert(Policy_contract.address !== '');
        });

    it('test2_add_policy', async()=>{
        const ID_contract = await id_contract.new(accounts[4]);
        const Policy_contract = await policy_contract.new(ID_contract.address);
        await ID_contract.addDomain("test", accounts[0], [accounts[1]],["sensor"],
										{ from: accounts[4]});
        const policy = {owner : accounts[0], device_type: "sensor" , domain:"test", usage_times : 3, time_intervals:[2]};
        await Policy_contract.add_policy(accounts[1],"read",policy,{from: accounts[0]});
        const hashed = soliditySha3(accounts[0],accounts[1],"read");
        return Policy_contract.getPolicy.call(hashed,0).then(function(result){
            
            assert(result[0] == accounts[0]);
            assert(result[1] == "sensor");
            assert(result[2] == 'test');
            assert(result[3].words[0] == 3);
            assert(result[4][0].words[0] == 2);
        })
        
        });
    it('test3_remove_policy', async()=>{
        const ID_contract = await id_contract.new(accounts[4]);
        const Policy_contract = await policy_contract.new(ID_contract.address);
        await ID_contract.addDomain("test", accounts[0], [accounts[1]],["sensor"],
        { from: accounts[4]});
        const policy = {owner : accounts[0], device_type: "sensor" , domain:"test", usage_times : 3, time_intervals:[2]};
        await Policy_contract.add_policy(accounts[1],"read",policy,{from: accounts[0]});
        const policy2 = {owner : accounts[0], device_type: "camera" , domain:"test", usage_times : 3, time_intervals:[2]};
        await Policy_contract.add_policy(accounts[1],"read",policy2,{from: accounts[0]});
        return Policy_contract.remove_policy.call(accounts[1],"read",policy,{from: accounts[0]}).then(function(result){
            assert(result == true);
        })
        
        });
    it('test4_add_special_id', async()=>{
        const ID_contract = await id_contract.new(accounts[4]);
        const Policy_contract = await policy_contract.new(ID_contract.address);
        await ID_contract.addDomain("test", accounts[0], [accounts[1]],["sensor"],
        { from: accounts[4]});
        await Policy_contract.add_special_id(accounts[1],"read",accounts[2],{from:accounts[0]});
        const hashed = soliditySha3(accounts[0],accounts[1],"read");
        const result = await Policy_contract.special_list_map(hashed,0);
        assert(result == accounts[2]);
        });
    it('test5_remove_special_id', async()=>{
        const ID_contract = await id_contract.new(accounts[4]);
        const Policy_contract = await policy_contract.new(ID_contract.address);
        await ID_contract.addDomain("test", accounts[0], [accounts[1]],["sensor"],
        { from: accounts[4]});
        await Policy_contract.add_special_id(accounts[1],"read",accounts[2],{from:accounts[0]});
        return Policy_contract.remove_special_id.call(accounts[1],"read",accounts[2],{from:accounts[0]}).then(function(result){
            assert(result == true);
        })
        
        });
    
});
