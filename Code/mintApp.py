import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

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

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
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
# Set up Web Page App
################################################################################

# Tile info and Welcome
st.title("A A C C")
st.header("Australian Authority of Carbon Credits")
st.image(Image.open('../Images/claudio-testa--SO3JtE3gZo-unsplash.jpg'))
st.header("Welcome to the CarbCred Minting System")

# select recipient account
st.write("Choose an account to recieve the new CarbCreds")
accounts = w3.eth.accounts
recipient_address = st.selectbox("Select Account", options=accounts)
# enter number of CarbCreds to mint
mint_quantity = st.text_input("Enter the number of CarbCreds to Mint")
st.markdown("---")



################################################################################
# Mint CarbCreds and transfer to account
################################################################################

st.write("Enter Authorised Minter's Credentials")

if check_password(): # Check That the user is authorised to mint
    st.header("Credentials Approved!")
    # use confirmation button to proceed with minting
    if st.button(f"Confirm Mint {mint_quantity} CarbCreds"):
        
        # perform minting
        contract.functions.mint(recipient_address, (int(mint_quantity))).transact({'from': recipient_address, 'gas': 3000000})
        
        st.markdown("---")
        st.header(f"{mint_quantity} new CarbCreds Registerd to {recipient_address}")
        st.markdown("---")


else:
    st.header("You are not Authorised!!")

    






    # # Use the `pin_artwork` helper function to pin the file to IPFS
    # artwork_ipfs_hash, token_json = pin_artwork(artwork_name, file)

    # artwork_uri = f"ipfs://{artwork_ipfs_hash}"

    # tx_hash = contract.functions.registerArtwork(
    #     address,
    #     artwork_name,
    #     artist_name,
    #     int(initial_appraisal_value),
    #     artwork_uri,
    #     token_json['image']
    # ).transact({'from': address, 'gas': 1000000})
    # receipt = w3.eth.waitForTransactionReceipt(tx_hash)


    # st.write("Transaction receipt mined:")
    # st.write(dict(receipt))
    # st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
    # st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{artwork_ipfs_hash})")
    # st.markdown(f"[Artwork IPFS Image Link](https://ipfs.io/ipfs/{token_json['image']})")












# ################################################################################
# # Register New Artwork
# ################################################################################
# st.markdown("## Register New Artwork")
# artwork_name = st.text_input("Enter the name of the artwork")
# artist_name = st.text_input("Enter the artist name")
# initial_appraisal_value = st.text_input("Enter the initial appraisal amount")

# # Use the Streamlit `file_uploader` function create the list of digital image file types(jpg, jpeg, or png) that will be uploaded to Pinata.
# file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])

# if st.button("Register Artwork"):
#     # Use the `pin_artwork` helper function to pin the file to IPFS
#     artwork_ipfs_hash, token_json = pin_artwork(artwork_name, file)

#     artwork_uri = f"ipfs://{artwork_ipfs_hash}"

#     tx_hash = contract.functions.registerArtwork(
#         address,
#         artwork_name,
#         artist_name,
#         int(initial_appraisal_value),
#         artwork_uri,
#         token_json['image']
#     ).transact({'from': address, 'gas': 1000000})


#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     st.write("Transaction receipt mined:")
#     st.write(dict(receipt))
#     st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
#     st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{artwork_ipfs_hash})")
#     st.markdown(f"[Artwork IPFS Image Link](https://ipfs.io/ipfs/{token_json['image']})")

# st.markdown("---")


# ################################################################################
# # Appraise Art
# ################################################################################
# st.markdown("## Appraise Artwork")
# tokens = contract.functions.totalSupply().call()
# token_id = st.selectbox("Choose an Art Token ID", list(range(tokens)))
# new_appraisal_value = st.text_input("Enter the new appraisal amount")
# appraisal_report_content = st.text_area("Enter details for the Appraisal Report")

# if st.button("Appraise Artwork"):

#     # Make a call to the contract to get the image uri
#     image_uri = str(contract.functions.imageUri(token_id).call())
    
#     # Use Pinata to pin an appraisal report for the report content
#     appraisal_report_ipfs_hash =  pin_appraisal_report(appraisal_report_content+image_uri)

#     # Copy and save the URI to this report for later use as the smart contract’s `reportURI` parameter.
#     report_uri = f"ipfs://{appraisal_report_ipfs_hash}"

#     tx_hash = contract.functions.newAppraisal(
#         token_id,
#         int(new_appraisal_value),
#         report_uri,
#         image_uri

#     ).transact({"from": w3.eth.accounts[0]})
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     st.write(receipt)
# st.markdown("---")

# ################################################################################
# # Get Appraisals
# ################################################################################
# st.markdown("## Get the appraisal report history")
# art_token_id = st.text_input("Artwork ID")
# if st.button("Get Appraisal Reports"):
#     appraisal_filter = contract.events.Appraisal.createFilter(
#         fromBlock=0, argument_filters={"tokenId": art_token_id}
#     )
#     reports = appraisal_filter.get_all_entries()
#     if reports:
#         for report in reports:
#             report_dictionary = dict(report)
#             st.markdown("### Appraisal Report Event Log")
#             st.write(report_dictionary)
#             st.markdown("### Pinata IPFS Report URI")
#             report_uri = report_dictionary["args"]["reportURI"]
#             report_ipfs_hash = report_uri[7:]
#             image_uri = report_dictionary["args"]["artJson"]
#             st.markdown(
#                 f"The report is located at the following URI: "
#                 f"{report_uri}"
#             )
#             st.write("You can also view the report URI with the following ipfs gateway link")
#             st.markdown(f"[IPFS Gateway Link](https://ipfs.io/ipfs/{report_ipfs_hash})")
#             st.markdown("### Appraisal Event Details")
#             st.write(report_dictionary["args"])
#             st.image(f'https://ipfs.io/ipfs/{image_uri}')
#     else:
#         st.write("This artwork has no new appraisals")





# st.markdown("## Get the appraisal report history")
# art_token_id = st.number_input("Artwork ID", value=0, step=1)
# if st.button("Get Appraisal Reports"):
#     appraisal_filter = contract.events.Appraisal.createFilter(
#         fromBlock=0, argument_filters={"tokenId": art_token_id}
#     )
#     reports = appraisal_filter.get_all_entries()
#     if reports:
#         for report in reports:
#             report_dictionary = dict(report)
#             st.markdown("### Appraisal Report Event Log")
#             st.write(report_dictionary)
#             st.markdown("### Pinata IPFS Report URI")
#             report_uri = report_dictionary["args"]["reportURI"]
#             report_ipfs_hash = report_uri[7:]
#             image_uri = report_dictionary["args"]["artJson"]
#             st.markdown(
#                 f"The report is located at the following URI: "
#                 f"{report_uri}"
#             )
#             st.write("You can also view the report URI with the following ipfs gateway link")
#             st.markdown(f"[IPFS Gateway Link](https://ipfs.io/ipfs/{report_ipfs_hash})")
#             st.markdown("### Appraisal Event Details")
#             st.write(report_dictionary["args"])
#             st.image(f'https://ipfs.io/ipfs/{image_uri}')
#     else:
#         st.write("This artwork has no new appraisals")