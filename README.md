# Project-3: Carbon Credits - Blockchain
**FinTech Group Assessment 3**

### Table of Contents
- [Group Members](#group-members)
- [Introduction](#introduction)
- [Our Goal](#our-goal)
- [Dependencies/Libraries](#dependencieslibraries)
- [Parts of the Project](#parts-of-the-project)
    * [Minting of Carbon Credits](#minting-of-carbon-credits)
    * [Buying Carbon Credits from Government](#buying-carbon-credits-from-government)
    * [Trading Carbon Credits between companies](#trading-carbon-credits-between-companies)
    * [Voting on Carbon Credit Transactions](#voting-on-carbon-credit-transactions)
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

With the up coming legislation changes that will enforce companies to conduct business in a carbon neutral way, a whole new industry has begun to bloom. This industry utilizes carbon capture technology to provides carbon offsetting as a service to other companies. A new form of fungible token has emerged, Carbon Credits.[<sup>3</sup>](#reference-list)

[Back to Table of Contents](#Table-of-Contents)

## Our Goal

A Government Organisation has approached 3 Squared for a product solution regarding upcoming developments of the Carbon Neutral Agreement made at COP26.

This project aims to:

1. Produce a smart contract in which Carbon Credits are minted by the Government Organisation only. 
2. Produce a smart contract that facilitates a Carbon Capture Company to purchase Carbon Credits from the government for declaration of carbon.
3. Produce a smart contract that facilitates the purchase of Carbon Credits for funds.
4. Produce a smart contract that facilitates company board members to vote on where a Carbon Credit transaction shold be approved or not.

[Back to Table of Contents](#Table-of-Contents)

## Dependencies/Libraries

`insert list of libraries or technologies necessary to be installed or used for this project`

[Back to Table of Contents](#Table-of-Contents)

## Parts of the Project

### Project setup
To set up this project.


Importing tokens into Metamask
1. Ensure MetaMask and Ganache are linked
* To ensure that the mintApp and transferApp work effectively, it is important to ensure that Ganache is showing as a Network in MetaMask as shown below:
![Ganache in Network]("C:\Users\thoma\Bootcamp\Project-3\Images\Ganache linked with metamask.png")
* To do this, in the drop down box on the top right of MetaMask webpage, selected add network. Using the details displayed in Genache, fill in the New RPC URL, Chain ID and provide a currency symbol as displayed below:
![Ganache linking in Metamask]("C:\Users\thoma\Bootcamp\Project-3\Images\Ganache linking with Metamask.png")

2. Import Ganache Account
* Once Metamask is added, import all Genache accounts using the private key to MetaMask. This will allow for transacting across multiple accounts in the environment.

* Within MetaMask, click on the coloured circle in the top right of MetaMask and click "Import Account". This will bring you to a page where MetaMask asks for a Private key to import an account.
![Circle in Metamask]("C:\Users\thoma\Bootcamp\Project-3\Images\Circle in MM.png")

* In Ganache, find the key icon that is to the right of the first account and click on it. Copy the Private Key as shown below. 
![Ganache 1]("C:\Users\thoma\Bootcamp\Project-3\Images\Ganache 1.png")
![Ganache 2]("C:\Users\thoma\Bootcamp\Project-3\Images\Adding a MM Account.png")

* Paste private key into the section in MetaMask and hit "Import". MetaMask will then import this Ganache Account. For the purpose of this exercise, we have renamed the accounts for similicity. By clicking on the three dots next to "Account X", click on "Account Details" and rename the account. We have named them as "G Acc X" as shown below. 
![Ganache 3]("C:\Users\thoma\Bootcamp\Project-3\Images\Import Ganache Acc.png")

3. Import Tokens (CCD)
* Once MetaMask has been loaded with your Genache accounts, its now time to import CarbonCred tokens (CCD). 
* To do this, first open the solidity code file in Remix. Compile and deploy contract and check for the green tick at the bottom of the page as shown below:

* Once the contract has been deployed in Remix, on the lefthand side of Remix, the contract will now show under deployed contract. Click on the copy button below the "Deployed Contact" title as seen below. This is will allow for linking the smart contract with MetaMask and Genache. 
![RemixCode]("C:\Users\thoma\Bootcamp\Project-3\Images\Remix Code.png")
* The next step will need to be completed for each of your Genache accounts in MetaMask. First, click on "Import Tokens" shown below. 
![Import Tokens]("C:\Users\thoma\Bootcamp\Project-3\Images\Import tokens 1.png")
* Paste the previous copied Solidity Contract Address that was copied from Remix into the first box. Type "CCD" for CarbonCredit into the token symbol box. Leave Token Decimal blank and then click Add Custom Token.
![Import Tokens 2]("C:\Users\thoma\Bootcamp\Project-3\Images\Import tokens 2.png")
![Import Tokens 3]("C:\Users\thoma\Bootcamp\Project-3\Images\Import tokens 3.png")
* You should now see CCD in your respective account. It is important you replicate these steps for Importing Tokens (CCD) for each account within your MetaMask as this will help keep record of which account holds how many CCDs. 
![Import Tokens 4]("C:\Users\thoma\Bootcamp\Project-3\Images\Import tokens 4.png")


### Setting up LogIn Credentials for CarbonCred site
Both streamlit apps require the use of a username and password for the validation process. To set up the validation process, create a login details in the secrets.toml file using the same layout as demonstrated below. To run this code, it is not essentual as you can use the existing login details, however it is good practice. 


### Minting of Carbon Credits

`insert meat of the project here`

### Buying Carbon Credits from Government

`insert meat of the project here`

### Trading Carbon Credits between companies

`insert meat of the project here`

### Voting on Carbon Credit Transactions

`insert meat of the project here`

[Back to Table of Contents](#Table-of-Contents)

## Future Opportunities Given Time and Resources

`insert list of potential next steps for the project`

`insert additional questions to research if given more time`

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

[Back to Table of Contents](#Table-of-Contents)


