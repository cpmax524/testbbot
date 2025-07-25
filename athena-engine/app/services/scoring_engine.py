from . import moralis_service

def calculate_mvrv_score(mvrv_ratio):
    """
    Calculates the MVRV score.
    """
    if mvrv_ratio > 3.0:
        return -8
    elif mvrv_ratio > 2.5:
        return -6
    elif mvrv_ratio > 2.0:
        return -4
    elif mvrv_ratio > 1.5:
        return -2
    elif mvrv_ratio > 1.0:
        return 2
    elif mvrv_ratio > 0.8:
        return 5
    elif mvrv_ratio > 0.6:
        return 8
    else:
        return 10

def calculate_exchange_netflow_score(exchange_netflow):
    """
    Calculates the exchange netflow score.
    """
    if exchange_netflow > 10000:
        return -7
    elif exchange_netflow > 5000:
        return -5
    elif exchange_netflow > 1000:
        return -3
    elif exchange_netflow < -10000:
        return 9
    elif exchange_netflow < -5000:
        return 7
    elif exchange_netflow < -1000:
        return 5
    else:
        return 0

def calculate_lth_supply_ratio_score(lth_supply_ratio):
    """
    Calculates the LTH supply ratio score.
    """
    if lth_supply_ratio > 0.7:
        return 8
    elif lth_supply_ratio > 0.6:
        return 6
    elif lth_supply_ratio < 0.4:
        return -6
    else:
        return 0

def calculate_funding_rates_score(funding_rates):
    """
    Calculates the funding rates score.
    """
    if funding_rates > 0.1:
        return -9
    elif funding_rates > 0.05:
        return -7
    elif funding_rates < -0.1:
        return 9
    elif funding_rates < -0.05:
        return 7
    else:
        return 0

def calculate_athena_score(address: str, chain: str):
    """
    Calculates the Athena score for a given address.
    """
    # These are placeholder values. In a real application, you would fetch this data from the Moralis API.
    mvrv_ratio = 1.2
    exchange_netflow = -6000
    lth_supply_ratio = 0.65
    funding_rates = -0.06

    mvrv_score = calculate_mvrv_score(mvrv_ratio)
    exchange_netflow_score = calculate_exchange_netflow_score(exchange_netflow)
    lth_supply_ratio_score = calculate_lth_supply_ratio_score(lth_supply_ratio)
    funding_rates_score = calculate_funding_rates_score(funding_rates)

    athena_score = (mvrv_score + exchange_netflow_score + lth_supply_ratio_score + funding_rates_score) / 4
    return athena_score
