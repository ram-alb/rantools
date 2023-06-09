import re


def get_parameter(atoll_parameter):
    """
    Get atoll parameter handled for comparing.

    Args:
        atoll_parameter (str, int): a parameter value from atoll

    Returns:
        int
    """
    if atoll_parameter is None:
        return -1
    if isinstance(atoll_parameter, str):
        numeric_parameter = re.sub(r'\D', '', atoll_parameter)
        return int(numeric_parameter)
    return atoll_parameter


def get_prach(atoll_prach):
    """
    Get prach value from atoll data.

    Args:
        atoll_prach (str): a prach value from atoll

    Retruns:
        int: prach value changed to int value
    """
    if atoll_prach is None:
        return -1
    prach = atoll_prach.split('-')[0]
    return int(prach)


def parse_carrier(atoll_carrier):
    """
    Parse arfcndl and bandwidth from carrier data.

    Args:
        atoll_carrier (str): carrier data from atoll

    Returns:
        tuple: first item is arfcndl, second is bandwidth
    """
    if atoll_carrier is None:
        return (-1, -1)
    carrier = atoll_carrier.strip()
    carrier_data = carrier.split(' ')
    arfcndl = carrier_data[-1]
    bandwidth = carrier_data[0]
    return (int(arfcndl), int(bandwidth))


def handle_atoll_nr_params(atoll_params):
    """
    Handle all atoll parameters to be ready for comparing.

    Args:
        atoll_params (list): a list of namedtuples with NR params

    Returns:
        dict: keys are the cells, values are the dicts with cell parameters
    """
    atoll_params_dict = {}

    for row in atoll_params:
        arfcndl, bandwidth = parse_carrier(row.carrier)
        atoll_params_dict[row.cell] = {
            'site': row.site,
            'cellid': get_parameter(row.cellid),
            'pci': get_parameter(row.pci),
            'tac': get_parameter(row.tac),
            'prach': get_prach(row.prach),
            'arfcndl': arfcndl,
            'bandwidth': bandwidth,
        }

    return atoll_params_dict


def get_atoll_cell_params(cell, atoll_params):
    """
    Get parameters for one cell from atoll NR cell data.

    Args:
        cell (str): a cell name
        atoll_params (dict): keys are cells, values are dicts of cell parameters

    Returns:
        dict: dict with parameters if cell found or default values
    """
    try:
        atoll_cell_params = atoll_params[cell]
    except KeyError:
        atoll_cell_params = {
            'site': '',
            'cellid': -1,
            'pci': -1,
            'tac': -1,
            'prach': -1,
            'arfcndl': -1,
            'bandwidth': -1,
        }
    return atoll_cell_params
