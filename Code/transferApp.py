import os
import json
from pickle import TRUE
from turtle import onclick
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
from web3 import Account
from web3.gas_strategies.time_based import medium_gas_price_strategy

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI"))) # HTTP://127.0.0.1:7545 from Ganache

################################################################################
# Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./Contracts/Compiled/mintCarbCred_abi.json')) as f:   
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()

################################################################################
# Password Function
################################################################################
# Source: https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso

def check_password(user_ID, pass_ID, pasword_set):
    """Returns `True` if the user had a correct password."""

    def password_entered(user_ID, pass_ID, pasword_set):
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state[user_ID] in st.secrets[pasword_set]
            and st.session_state[pass_ID]
            == st.secrets[pasword_set][st.session_state[user_ID]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state[pass_ID]  # don't store username + password
            del st.session_state[user_ID]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered(user_ID, pass_ID, pasword_set), key = user_ID)
        st.text_input(
            "Password", type="password", on_change=password_entered(user_ID, pass_ID, pasword_set), key = pass_ID
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered(user_ID, pass_ID, pasword_set), key = user_ID)
        st.text_input(
            "Password", type="password", on_change=password_entered(user_ID, pass_ID, pasword_set), key = pass_ID
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

## example code for the password Action
# if check_password():
#     st.write("Here goes your normal Streamlit app...")
#     st.button("Click me")

################################################################################
# Set up def send_transaction function
################################################################################

def send_transaction(w3, account, to, ether_value):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    value = w3.toWei(ether_value, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value})

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": 0,
        "nonce": w3.eth.getTransactionCount(account.address)
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)

################################################################################
# Set up Web Page App
################################################################################

# Tile info and Welcome
st.title("A A C C")
st.header("Australian Authority of Carbon Credits")
st.image(Image.open('../Images/claudio-testa--SO3JtE3gZo-unsplash.jpg'))
st.header("Welcome to the CarbCred B2B Trading System")


################################################################################
# Select Accounts and display balance
################################################################################

# select Seller account
st.subheader("Account Details")
accounts = w3.eth.accounts
seller_address = st.selectbox("Seller's Account", options=accounts)
# fetch and display balance
# CCD
seller_CCD_balance = contract.functions.balanceOf(seller_address).call()
st.write(f"Seller CCD Balance: {seller_CCD_balance}")
# ETH
seller_wei_balance = w3.eth.get_balance(seller_address)
seller_ETH_balance = w3.fromWei(seller_wei_balance, "ether")
st.write(f"Seller ETH Balance: {seller_ETH_balance}")
st.markdown("---")

# select Buyer account
accounts = w3.eth.accounts
buyer_address = st.selectbox("Buyer's Account", options=accounts)
# fetch and display balance
# ETH
buyer_wei_balance = w3.eth.get_balance(buyer_address)
buyer_ETH_balance = w3.fromWei(buyer_wei_balance, "ether")
st.write(f"Buyer ETH Balance: {buyer_ETH_balance}")
# CCD
buyer_CCD_balance = contract.functions.balanceOf(buyer_address).call()
st.write(f"Seller CCD Balance: {buyer_CCD_balance}")

# confirm accounts are not the same account
if seller_address == buyer_address:
    st.subheader("ERROR!! Same Account Selcted")
    accounts_approved = False
else:
    accounts_approved = True
st.markdown("---")

################################################################################
# Set up Trade Details
################################################################################

# Enter number of CarbCreds to Sell
st.subheader("Trade Details")
CCD_quantity = st.number_input("Enter CarbCred Quantiy from Seller", min_value=0,step=1)

# Enter number of ETH to pay
st.subheader("Agreed Value of Etherium to Pay by Buyer")
ETH_quantity = st.number_input("Enter ETH Quantiy", min_value=0)
st.markdown("---")

# confirm that the accoust hve sufficient balance for the trade
if seller_CCD_balance >= CCD_quantity and buyer_ETH_balance >= ETH_quantity:
    trade_value_approved = True
else:
    st.subheader("Insuficiant Funds!!")


################################################################################
# Confirm Buyer and Seller Approval
################################################################################

st.subheader("Confirm Buyer and Seller Approval")

# # Comfirm Company names and link their passwords
# seller_company = accounts.index(seller_address)
# seller_password_set = "COMPANY " + str((seller_company + 1))

# buyer_company = accounts.index(buyer_address)
# buyer_password_set = "COMPANY " + str((buyer_company + 1))

# # Enter Password details
# st.write(f"Enter Seller's Credentials: {seller_password_set}")
# seller_approved = check_password("SUser", "SPass", seller_password_set )
# if seller_approved:
#     st.subheader(f"{seller_password_set} APPROVED!!")

# st.write(f"Enter Buyer's Credentials: {buyer_password_set}")
# buyer_approved = check_password("BUser", "BPass", buyer_password_set)
# if buyer_approved:
#     st.subheader(f"{buyer_password_set} APPROVED!!")


buyer_approved = True
seller_approved = True

st.markdown("---")



################################################################################
# Action Trade and display fianl balances
################################################################################
# Confirm requirements met for trade to proceed
# True * True * True = True //// True * True * False = False

transaction_complete = False

st.write(transaction_complete)

if accounts_approved * seller_approved * buyer_approved * trade_value_approved:
    if st.button("Action Trade", disabled = transaction_complete):

        #### Transfer the CCD from Seller to Buyer
        # send CCD
        # transferFrom(from, to, amount)
        contract.functions.approve(seller_address,CCD_quantity).transact({'from': seller_address, 'gas': 3000000})
        contract.functions.transferFrom(seller_address, buyer_address, CCD_quantity).transact({'from': seller_address, 'gas': 3000000})

        #### Transfer the ETH from Buyer to the Seller

        account = Account.privateKeyToAccount("fc72b370af79ceb3b1ad466f01dfd3c0f553de9398507f92078e4d6f5375cc98")
        send_transaction(w3, account, buyer_address, ETH_quantity)

        st.write(f"{account.address}")


        ###########
        # Final Balances
        # fetch and display balance of Seller
        st.subheader("Seller Final Balance")
        # CCD
        seller_CCD_balance = contract.functions.balanceOf(seller_address).call()
        st.write(f"Seller CCD Balance: {seller_CCD_balance}")
        # ETH
        seller_wei_balance = w3.eth.get_balance(seller_address)
        seller_ETH_balance = w3.fromWei(seller_wei_balance, "ether")
        st.write(f"Seller ETH Balance: {seller_ETH_balance}")
        st.markdown("---")

        # fetch and display balance of Buyer
        st.subheader("Buyer Final Balance")
        # ETH
        buyer_wei_balance = w3.eth.get_balance(buyer_address)
        buyer_ETH_balance = w3.fromWei(buyer_wei_balance, "ether")
        st.write(f"Buyer ETH Balance: {buyer_ETH_balance}")
        # CCD
        buyer_CCD_balance = contract.functions.balanceOf(buyer_address).call()
        st.write(f"Buyer CCD Balance: {buyer_CCD_balance}")

        # Disable button
        transaction_complete = True

else:
    st.write("Error with request, review entered data")