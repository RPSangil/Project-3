pragma solidity ^0.5.11;

// Contract for a Multisignature Wallet.
contract MultiSigWallet {
    //---Events---//

    // This is fired when CarbCreds are deposited into the MultiSigWallet.
    event Deposit (address indexed sender, uint amount, uint balance);
    /* This is fired when a transaction is submitted and awaiting for other owners to approve.
    [txIndex] is the index where the transaction is stored. */
    event SubmitTransaction (address indexed owner, uint indexed txIndex, address indexed to, uint value, bytes data);
    // This is fired when other owners approve the transaction.
    event ApproveTransaction (address indexed owner, uint indexed txIndex);
    // This is fired when a transaction has been approved but owners wish to unapprove the transaction.
    event RevokeApproval (address indexed owner, uint indexed txIndex);
    // This is fired when there are sufficient amount of approvals for the transaction.
    event ExecuteTransaction (address indexed owner, uint indexed txIndex);

    //---State Variables---//

    // Stores the array of address of the MultiSigWallet owners.
    address[] public owners;
    //Checks that msg.sender is an owner.
    mapping(address => bool) public isOwner;
    // Number of owner approvals necessary for the transaction to be executed.
    uint public numApprovalsRequired;

    // Stores the transaction information.
    struct Transaction {
        // [address] the transaction is executed.
        address to;
         // Amount of CarbCreds sent to the [to] address.
        uint value;
        // Data to be sent to the [to] address.
        bytes data;
        // Once the transaction is executed, we will set the bool to true.
        bool executed;
        // count of approvals.
        uint numApprovals;
    }

    // Stores that the transaction has been approved by an owner.
    mapping(uint => mapping(address => bool)) public isApproved;
    // Stored in the struct.
    Transaction[] public transactions;

    //---Modifiers used in Functions---//

    // Checks that only an owner can proceed.
    modifier onlyOwner() {
        require(isOwner[msg.sender], "not owner");
        _;
    }
    // Checks that only existing transactions can proceed.
    modifier txExists(uint _txIndex) {
        require(_txIndex < transactions.length, "tx does not exist");
        _;
    }
    // Checks that only trasnactions not previously approved by this owner can proceed.
    modifier notApproved(uint _txIndex) {
        require(!isApproved[_txIndex][msg.sender], "tx already approved");
        _;
    }
    // Checks that only transactions not yet executed can proceed.
    modifier notExecuted(uint _txIndex) {
        require(!transactions[_txIndex].executed, "tx already executed");
        _;
    }
    
    //---Constructor---//

    // [address] is the addresses of the owners, [uint] required approvals necessary for transaction to be executed.
    constructor(address[]memory _owners, uint _numApprovalsRequired) public {
        // Checks that there is at least 1 owner.
        require(_owners.length > 0, "owners required");
        // Checks that the number of approvals required is greater than 0 AND less than or equal to the number of owners.
        require(_numApprovalsRequired > 0 && _numApprovalsRequired <= _owners.length, "invalid number of required approvals");

        // Loop to save [owner] to [owners] state variable.
        for (uint i = 0; i < _owners.length; i++) {
            // Grabs address from the array of addresses.
            address owner = _owners[i];
            // checks that [address] cannot be equal to [address[0]].
            require(owner != address (0), "invalid owner");
            // checks that [owner] is unique.
            require(!isOwner[owner], "owner not unique");
            // Inserts [owner] into [isOwner] mapping.
            isOwner[owner] = true;
            // Pushes [owner] into [owners] state variable.
            owners.push(owner);

        }
        // [numApprovalsRequired] state variable is equal to [_numApprovalsRequired] from the input.
        numApprovalsRequired = _numApprovalsRequired;
    }

    //---Functions---//

    // Fallback function
    function () payable external {
        emit Deposit(msg.sender, msg.value, address (this).balance);
    }
    // Easy deposit
    function deposit() payable external {
        emit Deposit(msg.sender, msg.value, address (this).balance);
    }
    // Enables a trasnaction to be submitted for approval.
    function submitTransaction (address _to, uint _value, bytes memory _data) 
        public
        onlyOwner
    {
        uint txIndex = transactions.length;
        //Parameters pushed into the Transaction array.
        transactions.push(Transaction({
            to: _to,
            value: _value,
            data: _data,
            executed: false,
            numApprovals: 0
        }));
        
        emit SubmitTransaction(msg.sender, txIndex, _to, _value, _data);
    }
    // Enables owners to provide approval for the transaction and adds to the count of approvals.
    function approveTransaction (uint _txIndex)
        public
        onlyOwner
        txExists(_txIndex)
        notExecuted(_txIndex)
        notApproved(_txIndex)
    {
        Transaction storage transaction = transactions[_txIndex];
        isApproved[_txIndex][msg.sender] = true;
        transaction.numApprovals += 1;

        emit ApproveTransaction(msg.sender, _txIndex);
    }
    // Enables execution of the transaction after enough approvals are confirmed.
    function executeTransaction (uint _txIndex)
        public 
        onlyOwner
        txExists(_txIndex)
        notExecuted(_txIndex)
    {
        Transaction storage transaction = transactions[_txIndex];

        require(transaction.numApprovals >= numApprovalsRequired, "cannot execute tx");
        transaction.executed = true;
        (bool success, ) = transaction.to.call.value(transaction.value)(transaction.data);
        require(success, "tx failed");

        emit ExecuteTransaction(msg.sender, _txIndex);
    }
    // Enables owners to revoke their approval in the event of a change of mind.
    function revokeApproval(uint _txIndex)
        public
        onlyOwner
        txExists(_txIndex)
        notExecuted(_txIndex)
    {   
        // Checks that the owner had approved the transaction previously.
        require(isApproved[_txIndex][msg.sender], "tx not approved");
        isApproved[_txIndex][msg.sender] = false;
        
        emit RevokeApproval(msg.sender, _txIndex);
    }
}