from network_vs_atoll.src.compare import compare
from network_vs_atoll.src.handler import handle_diffs
from network_vs_atoll.src.wcdma.atoll_handler import (
    get_cell_atoll_params,
    handle_atoll_wcdma_params,
)
from network_vs_atoll.src.wcdma.netwrok_handler import get_cell_network_params
from network_vs_atoll.src.wcdma.wcdma_select import (
    select_atoll_params,
    select_network_params,
)


def wcdma_main():
    """
    Compare WCDMA network and atoll parameters.

    Returns:
        dict: keys - rnc names, values - list of dicts with cell diffs
    """
    selected_network_params = select_network_params()

    selected_atoll_params = select_atoll_params()
    atoll_params = handle_atoll_wcdma_params(selected_atoll_params)

    diffs = compare(
        'WCDMA',
        selected_network_params,
        get_cell_network_params,
        atoll_params,
        get_cell_atoll_params,
    )

    return handle_diffs('rnc', diffs)
