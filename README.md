# Project-3: CarbCreds Token 
**FinTech Group Assessment 3**

### Table of Contents
- [Group Members](#group-members)
- [Introduction](#introduction)
- [Our Goal](#our-goal)
- [Dependencies/Libraries](#dependencieslibraries)
- [Parts of the Project](#parts-of-the-project)
    * [Project Setup](#project-setup)
    * [Minting of CarbCreds](#minting-of-carbcreds)
    * [Trading CarbCreds](#trading-carbcreds)
    * [Voting on CarbCred Transactions](#voting-on-carbcred-transactions)
- [Future Opportunities Given Time and Resources](#future-opportunities-given-time-and-resources)
    * [Useful Resources for Future Develpoment](#useful-resources-for-future-develpoment)
- [Reference list](#reference-list)

## Group Members of 3 Squared

- Matt Lewis (ML789)
- Suraj Shrestha (Suraj567255)
- Raelyn Sangil (RPSangil)
- Thomas Gosper (Gosper23)

## Introduction

At the UN Glasgow climate conference, a new global agreement - the Glasgow Climate Pact - was reached at the COP26 summit.[<sup>1</sup>](#reference-list) This agreement will set the tone for the global agenda on climate change for the next decade and Australia has modified their previous target that included net zero emissions by 2050 to achieve up to 35 per cent reduction by 2030.[<sup>2</sup>](#reference-list)

With the up coming legislation changes that will enforce companies to conduct business in a carbon neutral way, a whole new industry has begun to bloom. This industry utilizes carbon capture technology to provides carbon offsetting as a service to other companies. A new form of fungible token has emerged, CarbCreds.[<sup>3</sup>](#reference-list)

[Back to Table of Contents](#Table-of-Contents)

## Our Goal

This project aims to develop:

1. A smart contract based crypto token to represent a value of captured carbon in the form of CarbCreds.
2. A minting application to allow authorises governing personnel to mint and distribute CardCreds as rewards for captured carbon.
3. A transfer application to allow business to bussiness trading of CarbCreds.
3. A multi-signature smart contract that allows voting by company directors to approve a transaction.

## Parts of the Project

### Project setup

To set up this project.

<ins>Importing tokens into Metamask</ins>
1. Ensure MetaMask and Ganache are linked
- To ensure that the mintApp and transferApp work effectively, it is important to ensure that Ganache is showing as a Network in MetaMask as shown below:

![Ganache in Network](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Ganache%20linked%20with%20metamask.png)

- To do this, in the drop down box on the top right of MetaMask webpage, selected add network. Using the details displayed in Genache, fill in the New RPC URL, Chain ID and provide a currency symbol as displayed below:

![Ganache linking in Metamask](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Ganache%20linking%20with%20Metamask.png)

2. Import Ganache Account
- Once Metamask is added, import all Genache accounts using the private key to MetaMask. This will allow for transacting across multiple accounts in the environment.

- Within MetaMask, click on the coloured circle in the top right of MetaMask and click "Import Account". This will bring you to a page where MetaMask asks for a Private key to import an account.

![Circle in Metamask](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Circle%20in%20MM.png)

- In Ganache, find the key icon that is to the right of the first account and click on it. Copy the Private Key as shown below. 

![Ganache 1](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Ganache%201.png)

![Ganache 2](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Adding%20a%20MM%20Account.png)

- Paste private key into the section in MetaMask and hit "Import". MetaMask will then import this Ganache Account. For the purpose of this exercise, we have renamed the accounts for similicity. By clicking on the three dots next to "Account X", click on "Account Details" and rename the account. We have named them as "G Acc X" as shown below. 

![Ganache 3](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Import%20Ganache%20Acc.png)

3. Import Tokens (CCD)
- Once MetaMask has been loaded with your Genache accounts, its now time to import CarbonCred tokens (CCD). 
- To do this, first open the solidity code file in Remix. Compile and deploy contract and check for the green tick at the bottom of the page as shown below:
- Once the contract has been deployed in Remix, on the lefthand side of Remix, the contract will now show under deployed contract. Click on the copy button below the "Deployed Contact" title as seen below. This is will allow for linking the smart contract with MetaMask and Genache. 

![RemixCode](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Remix%20Code.png)

- The next step will need to be completed for each of your Genache accounts in MetaMask. First, click on "Import Tokens" shown below. 

![Import Tokens](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Import%20tokens%201.png)

- Paste the previous copied Solidity Contract Address that was copied from Remix into the first box. Type "CCD" for CarbonCredit into the token symbol box. Leave Token Decimal blank and then click Add Custom Token.

![Import Tokens 2](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Import%20tokens%202.png)

![Import Tokens 3](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Import%20tokens%203.png)

- You should now see CCD in your respective account. It is important you replicate these steps for Importing Tokens (CCD) for each account within your MetaMask as this will help keep record of which account holds how many CCDs. 

![Import Tokens 4](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Images/Import%20tokens%204.png)

<ins>Setting up LogIn Credentials for CarbonCred Site</ins>

Both streamlit apps require the use of a username and password for the validation process. To set up the validation process, create a login details in the secrets.toml file using the same layout as demonstrated below. To run this code, it is not essentual as you can use the existing login details, however it is good practice. 

[Back to Table of Contents](#Table-of-Contents)

### Minting of CarbCreds

https://user-images.githubusercontent.com/101629446/187858890-c87342a7-754f-4282-86fc-2c52a1cb6e39.mov

If for any reason this video does not work, please see [Minting Screen Capture video](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Videos/Minting_Screencapture.mov) for a place to download the video.

### Trading CarbCreds 

Please see here for where to download [Transfer Screen Capture Video](https://github.com/RPSangil/Project-3/blob/cfd6525dfebabf177867e50dc5dd50f1a6483210/Videos/Transfer_Screen_Capture.mov).

### Voting on CarbCred Transactions

In blockchain-based applications, activities might need to be authorised by multiple blockchain addresses. A transaction could indicate multi-party authorisation using a digital signature scheme that allows a group of addresses to sign the transaction. Such a signature is known as a multisignature. Depending on the chosen multisignature algorithm, we can enforce that the transaction is signed by all or a subset of the authorised addresses. A multisignature mechanism can be designed to require m out of n private keys to authorise a transaction, in which m is the threshold of authorisation (2 ≤ m ≤ n). A smart contract’s owner/manager can pre-define a group of addresses that can authorise a transaction and set the minimal number of authorisations required to approve a payment. [<sup>4</sup>](#reference-list)

This project has explored the use of [Multi-signature contract](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Code/Contracts/5-11%20Multisig%20wallet.sol) as a meants of voting on the approval of transactions. Enabling companies to vote on transactions for CarbCreds can helo to protect them from corporate espionage and financial fraud.

Below are some iamges of the contract functioning.

<ins>Compiled without Errors</ins>

![Compiled](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_compiled.PNG)

This contract was compiled using 0.5.17+commit.d19bba13 with no errors.

<ins>Assigned Addresses and Approvals Required</ins>

![Assigned Addresses and Approvals Required](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_assign_owners_and_2ApprovalsRequired.PNG)

For this demontration, 2 factors were indicated when deploying the contract:

1. Multiple address (owners). For the demonstration, 3 addresses were chosen.
2. Number of approvals required for the transaction to execute. For the demonstration, 2 (the majority) was indicated.

<ins>Deposit Function Working</ins>

![Deposit Function Working](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_Deposit_function_working.PNG)

We successfully deposited 1 ether into the cotnract.

<ins>Submit Transaction Function Working</ins>

![Submit Transaction Function Working]https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_submitTransaction_working.PNG)

The submitTransaction function was used to submit a transfer of the 1 ether to an address outside of the Multi-signature contract.

<ins>Display Amount of Approvals Required Working</ins>

![Call Amount of Approvals Required Working](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_display_approvalRequired.PNG)

The call shows that 2 approvals are required for the transaction to execute.

<ins>Approve Transaction Function Working</ins>

![Approve Transaction Function Working](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_ApproveTransaction_working.PNG)

One of the assigned addresses was used to approve the transaction.

<ins>Call to Check if an Owner has Approved a Transaction Working</ins>

![Call to Check if an Owner has Approved a Transaction Working](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_isApproved_working.PNG)

The call shows which address was used and confirmed that approval has been given by this address (true).

<ins>Revoke Approval of Transaction Function Working</ins>

![Revoke Approval of Transaction Function Working](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_RevokeApproval_working.PNG)

The Revoke approval function is working and approval was then regiven by the same address.

<ins>Execute Transaction after Aprovals Function Working</ins>

![Execute Transaction after Aprovals Function Working](https://github.com/RPSangil/Project-3/blob/8613b3c4d47a519826e0c220c326bbbb1902ce77/Images/5_11_MSG_ExecuteTransaction_working.PNG)

Once enough approval were made, the transaction was able to execute.

[Back to Table of Contents](#Table-of-Contents)

## Future Opportunities Given Time and Resources

Given more time, the project would have explored and implemented a front end python application that would enable users to use the Multi-Signature Contract for trading CarbCreds.

Areas this project could explore in the future would be:

- Implementation of carbon capture and consumption protocols in line with future legislation.
- An auditing system to be used by governing parties to enforce and monitor there protocols.
- Further implementation of a decentralised system.
- An automated balancing of company net zero.

### Useful Resources for Future Develpoment

- [ERC20 EIP](https://eips.ethereum.org/EIPS/eip-20)
- [ERC20 info](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/)
- [ERC20 Burnable](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#ERC20Burnable)
- [How to Run an Ethereum Node: Local](https://ethereum.org/en/run-a-node/)
- [Vitural node via dApp](https://docs.dappnode.io/get-started/intro/)

[Back to Table of Contents](#Table-of-Contents)

## Reference list

- [<sup>1</sup> COP26: What was agreed at the Glasgow climate conference?](https://www.bbc.com/news/science-environment-56901261)
- [<sup>2</sup> Australia Welcomes Positive Outcomes at COP26 ](https://www.minister.industry.gov.au/ministers/taylor/media-releases/australia-welcomes-positive-outcomes-cop26)
- [<sup>3</sup> Climate Solutions Fund: How you can benefit](https://www.cleanenergyregulator.gov.au/csf/how-you-can-benefit/Pages/how-you-can-benefit.aspx#:~:text=By%20running%20a%20project%2C%20you,gas%20emissions%20stored%20or%20avoided)
- [<sup>4</sup> CSIRO: Multiple Authorisation (aka., Multisignature)](https://research.csiro.au/blockchainpatterns/general-patterns/security-patterns/multiple-authorization/)
- [Image used in Minting App Source](https://unsplash.com/photos/-SO3JtE3gZo)
- [Passwords Code Source](https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso)
- [Multi-Sig Wallet Code Source](https://solidity-by-example.org/app/multi-sig-wallet/)
- [Image for Transfer App Source]()

[Back to Table of Contents](#Table-of-Contents)


