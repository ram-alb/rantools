from network_vs_atoll.src.compare import compare
from network_vs_atoll.src.gsm.atoll_handler import (
    get_atoll_cell_params,
    handle_gsm_atoll_data,
)
from network_vs_atoll.src.gsm.gsm_select import (
    select_atoll_cell_params,
    select_atoll_maio,
    select_network_params,
)
from network_vs_atoll.src.gsm.network_handler import get_network_cell_params
from network_vs_atoll.src.handler import handle_diffs


def gsm_main():
    """
    Compare GSM network params with atoll params.

    Returns:
        dict: keys - bscnames, values - list of dicts with cell diffs
    """
    selected_network_params = select_network_params()

    selected_atoll_cell_params = select_atoll_cell_params()
    selected_atoll_maio_params = select_atoll_maio()

    atoll_params = handle_gsm_atoll_data(
        selected_atoll_cell_params,
        selected_atoll_maio_params,
    )

    diffs = compare(
        'GSM',
        selected_network_params,
        get_network_cell_params,
        atoll_params,
        get_atoll_cell_params,
    )

    return handle_diffs('bsc', diffs)
