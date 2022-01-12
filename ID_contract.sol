pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract ID_contract {
    
    address admin;
    enum Status { pending , confirmed }
    
    struct Attribute{
        address deviceOwner;
        string device_type; // humidity sensor, motion sensor, light sensor, actuator, ...
        string domainName; // for example domain A, B, ...
        // I have no idea what other attributes can be!
    }

    
        struct Device {
            address deviceAddress;
            Attribute attribute;
            Status status;
            address delegatee;
            bool existing;
        }
    
       struct Domain {
        //string domainName; 
        bool created;  // if true, this domain name already exists
        address owner; // address of the owner
        address[] devicesAddr;   // adress of devices
    }
    
    mapping(string => Domain)  domains; // maps domianNmae to Domains
    mapping(address => Device) public devices;// maps addresses to devices
    
    
    
    //////////////////////////////////////////// Modifiers ////////////////////////////////////////////////
    
    // modifier to check if caller is admin
    modifier onlyAdmin() {  
        require(msg.sender == admin, "Caller is not admin");
        _;
    }
    
    modifier onlyDomainOwner(string memory domainName) {  
        require(msg.sender == domains[domainName].owner , "Caller is not the domain owner");
        _;
    }
    
    modifier onlyExistingDomains(string memory domainName) {  
        require(domains[domainName].created , "This domain doesn't exists");
        _;
    }
    
    modifier onlyNonExistingDomains(string memory domainName) {  
        require(!domains[domainName].created , "This domain already exists");
        _;
    }
    
    
    modifier onlyExistingDevice(address deviceAddr){  
        require(devices[deviceAddr].existing == true , "This device doesn't exists");
        _;
    }
    
    modifier onlyConfirmedDevice(address deviceAddr){  
        require(devices[deviceAddr].status == Status.confirmed , "This device hasn't confirmed yet");
        _;
    }
    
    modifier onlyDeviceOwnerOrDelegatee(address deviceAddr){
        if ( devices[deviceAddr].delegatee != address(0) )
            require( msg.sender == devices[deviceAddr].delegatee , "only delegatee can modify devices");
        else
             require( msg.sender == devices[deviceAddr].attribute.deviceOwner , "only domain owner can modify devices");
        _;
    }
    
    
    
    //////////////////////////////////////////// Events ////////////////////////////////////////////////
    
    event NewDomain(address owner , string domainName);
    event DeviceConfirmed(address owner, address deviceAddr ,string domainName);
    event DeviceModified(address deviceAddr , string deviceType);
    event DeviceDelegated(address deviceAddr , address delegatee);
    event DeviceDeleted(address deviceAddr);
    
    
    

    constructor(address _admin) public {
        admin = _admin;
    }

    /**
     * @dev adds a new domain called by the owner
     * @param domainName name of added domain 
     * @param owner owner of this domain
     * @param devicesAddr addresses of this domain's devices
     * @param devicetype attributes of this domain's devices
     * @param deviceOwners owners of the  devices
     */
    function addDomain(string memory domainName,
                       address owner,  
                       address[] memory devicesAddr ,
                       string[] memory devicetype,
                       address[] memory deviceOwners)
    public onlyAdmin onlyNonExistingDomains(domainName){
        
        domains[domainName].created = true;
        domains[domainName].owner = owner;
        domains[domainName].devicesAddr = devicesAddr;
        
        for(uint i = 0; i < devicesAddr.length; i++){
            Attribute memory devicesAttr = Attribute(deviceOwners[i] , devicetype[i] , domainName);
            Device memory device = Device(devicesAddr[i] , devicesAttr,
                                          Status.pending , address(0) , true);
            devices[devicesAddr[i]] = device;
        }
        emit NewDomain(owner , domainName);
    }
    
    /**
     * @dev adds new devices to a existing domain called by the owner
     * @param domainName name of domain
     * @param devicesAddr addresses of added devices
     * @param devicetype attributes of added devices
     * @param deviceOwners owners of the  devices
     */
    function addDevices(string memory domainName ,
                        address[] memory devicesAddr ,
                        string[] memory devicetype ,
                        address[] memory deviceOwners) public 
    onlyDomainOwner(domainName) onlyExistingDomains(domainName){
        
        for(uint i = 0; i < devicesAddr.length; i++){
            Attribute memory devicesAttr = Attribute(deviceOwners[i] , devicetype[i] , domainName);
            Device memory device = Device(devicesAddr[i] , devicesAttr,
                                          Status.pending , address(0) , true);
            domains[domainName].devicesAddr.push(devicesAddr[i]);
            devices[devicesAddr[i]] = device;
        }
    }
    
    /**
     * @dev a pending device calls this function to confirm its owner and as a result this devices 
     * becomes a confirmed device
     * @param domainName name of the corresponding domain
     * @param deviceOwner address of the corresponding domain owner
     */
    function confirmation(string memory domainName , address deviceOwner) onlyExistingDomains(domainName) public returns(bool) {
        
        Device memory device = devices[msg.sender];
        Domain memory domain = domains[domainName];
        
        require(device.attribute.deviceOwner == deviceOwner , "Owner address doesn't match");

        bool found = false;
        
        for(uint i = 0; i < domain.devicesAddr.length; i++){
            if(domain.devicesAddr[i] == msg.sender){
                found = true;
            }
        }
        require(found , "this device isn't added by any domain owner");
        

        devices[msg.sender].status = Status.confirmed;
        emit DeviceConfirmed(domains[domainName].owner , msg.sender , domainName);

        
    }
    
     /**
     * @dev delegates the ownership of a device to another owner or device 
     * @param deviceAddr address of the delegated device
     * @param delegatee address of the delegatee
     */
    function delegateDevice(address deviceAddr, address delegatee)
    public onlyConfirmedDevice(deviceAddr) onlyDeviceOwnerOrDelegatee(deviceAddr)
    onlyExistingDevice(deviceAddr){
        
        devices[deviceAddr].delegatee = delegatee;
        emit DeviceDelegated(deviceAddr , delegatee);
    }
    
    
     /**
     * @dev modifying features of a device
     * @param deviceAddr address of the modified device
     * @param deviceType new attributes
     */
     
    function modifyDeviceAttr(address deviceAddr , string memory deviceType) 
    onlyDeviceOwnerOrDelegatee(deviceAddr) 
    onlyExistingDevice(deviceAddr) public{
        devices[deviceAddr].attribute.device_type = deviceType;
        emit DeviceModified(deviceAddr , deviceType);
        
    }
    

    
    
    
        /**
     * @dev deleting a device
     * @param deviceAddr address of the modified device
     */
     
    function deleteDevice(address deviceAddr) 
        onlyDeviceOwnerOrDelegatee(deviceAddr)
        onlyExistingDevice(deviceAddr) public{
    
    
    Domain memory domain = domains[devices[deviceAddr].attribute.domainName];
    
     for(uint i = 0; i < domain.devicesAddr.length; i++){
            if(domain.devicesAddr[i] == deviceAddr){
                delete domain.devicesAddr[i];
                break;
            }
     }
    delete devices[deviceAddr];
    emit DeviceDeleted(deviceAddr);
    }
    

        
    
    function getDeviceOwner(address deviceAddr)  public returns (address){
        Device memory device = devices[deviceAddr];
        Attribute memory attr = device.attribute;
        address owner_adr = attr.deviceOwner;
        return owner_adr; 
    }
    
    /**
    * @dev Returns domain
    * @param domainName name of the domain
    * @return domain
    */
    function getDomain(string memory domainName)  public view returns (bool  , address , address[] memory ){
        
        return (domains[domainName].created , domains[domainName].owner , domains[domainName].devicesAddr);

    }
    
    /**
    * @dev Returns attributes of a device
    * @param deviceAddr of device
    * @return attributes
    */
    function getAttributes(address deviceAddr)  public view returns (address,string memory,string memory){
        
        return (devices[deviceAddr].attribute.deviceOwner, devices[deviceAddr].attribute.device_type, devices[deviceAddr].attribute.domainName);

    }

}
