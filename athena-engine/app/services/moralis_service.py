import moralis
from decouple import config

MORALIS_API_KEY = config('MORALIS_API_KEY')

def get_native_balance(address: str, chain: str):
    """
    Get the native balance of a given address.
    """
    params = {
        "address": address,
        "chain": chain,
    }
    return moralis.evm_api.balance.get_native_balance(api_key=MORALIS_API_KEY, params=params)

def get_token_balances(address: str, chain: str):
    """
    Get the token balances of a given address.
    """
    params = {
        "address": address,
        "chain": chain,
    }
    return moralis.evm_api.token.get_wallet_token_balances(api_key=MORALIS_API_KEY, params=params)

def get_token_transfers(address: str, chain: str):
    """
    Get the token transfers of a given address.
    """
    params = {
        "address": address,
        "chain": chain,
    }
    return moralis.evm_api.token.get_wallet_token_transfers(api_key=MORALIS_API_KEY, params=params)

def get_nft_transfers(address: str, chain: str):
    """
    Get the NFT transfers of a given address.
    """
    params = {
        "address": address,
        "chain": chain,
    }
    return moralis.evm_api.nft.get_wallet_nft_transfers(api_key=MORALIS_API_KEY, params=params)

def get_block(block_number_or_hash: str, chain: str):
    """
    Get a block by its number or hash.
    """
    params = {
        "block_number_or_hash": block_number_or_hash,
        "chain": chain,
    }
    return moralis.evm_api.block.get_block(api_key=MORALIS_API_KEY, params=params)

def get_date_to_block(date: str, chain: str):
    """
    Get the closest block to a given date.
    """
    params = {
        "date": date,
        "chain": chain,
    }
    return moralis.evm_api.block.get_date_to_block(api_key=MORALIS_API_KEY, params=params)

def get_token_price(address: str, chain: str):
    """
    Get the price of a given token.
    """
    params = {
        "address": address,
        "chain": chain,
    }
    return moralis.evm_api.token.get_token_price(api_key=MORALIS_API_KEY, params=params)
