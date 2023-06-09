from network_vs_atoll.src.compare import compare
from network_vs_atoll.src.handler import handle_diffs
from network_vs_atoll.src.nr5g.atoll_handler import (
    get_atoll_cell_params,
    handle_atoll_nr_params,
)
from network_vs_atoll.src.nr5g.network_handler import get_network_cell_params
from network_vs_atoll.src.nr5g.nr_select import (
    select_atoll_params,
    select_network_params,
)


def nr_main():
    """
    Compare NR network and atoll parameters.

    Returns:
        dict: keys - subnetworks, values - list of dicts with cell diffs
    """
    selected_network_params = select_network_params()

    selected_atoll_params = select_atoll_params()
    atoll_params = handle_atoll_nr_params(selected_atoll_params)

    diffs = compare(
        'NR',
        selected_network_params,
        get_network_cell_params,
        atoll_params,
        get_atoll_cell_params,
    )

    return handle_diffs('subnetwork', diffs)
