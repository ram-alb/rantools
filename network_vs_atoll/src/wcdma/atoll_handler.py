import re


def get_node(node):
    """
    Return node name if it is not None else empty string.

    Args:
        node (str, None): a node name

    Returns:
        str
    """
    return node if node else ''


def get_int_parameter(parameter):
    """
    Return parameter as int instanse.

    Args:
        parameter (str, int): a parameter value

    Returns:
        int
    """
    if parameter is None:
        return -1
    if isinstance(parameter, str):
        numeric_parameter = re.sub(r'\D', '', parameter)
        return int(numeric_parameter)
    return parameter


def handle_atoll_wcdma_params(atoll_params):
    """
    Handle all atoll parameters to be ready for comparing.

    Args:
        atoll_params (list): a list of namedtuples with NR params

    Returns:
        dict: keys are the cells, values are the dicts with cell parameters
    """
    atoll_params_dict = {}
    for row in atoll_params:
        atoll_params_dict[row.cell] = {
            'rnc': get_node(row.rnc),
            'site': get_node(row.site),
            'cellid': get_int_parameter(row.cellid),
            'uarfcndl': get_int_parameter(row.uarfcndl),
            'psc': get_int_parameter(row.psc),
            'lac': get_int_parameter(row.lac),
            'rac': get_int_parameter(row.rac),
            'sac': get_int_parameter(row.sac),
        }
    return atoll_params_dict


def get_cell_atoll_params(cell, atoll_params):
    """
    Get parameters for one cell from atoll WCDMA cell data.

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
            'rnc': '',
            'site': '',
            'cellid': -1,
            'uarfcndl': -1,
            'psc': -1,
            'lac': -1,
            'rac': -1,
            'sac': -1,
        }
    return atoll_cell_params
