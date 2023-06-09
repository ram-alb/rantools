import re


def handle_node(node):
    """
    Handle node selected from network.

    Args:
        node (str): a node name (site, bsc)

    Returns:
        str: if node is None returns empty string
    """
    if node:
        return node
    return ''


def handle_parameter(parameter):
    """
    Handle cell parameter.

    Args:
        parameter (int): a parameter value

    Returns:
        int: returns -1 if selected parameter is None
    """
    if parameter or parameter == 0:
        return parameter
    return -1


def handle_maio_tch(parameter):
    """
    Handle maio and tch data.

    Args:
        parameter (str): a maio or tch values

    Returns:
        str: handled value
    """
    if parameter is None:
        return ''
    formated_parameter = re.sub(';', ', ', parameter)
    sorted_parameter = sorted(formated_parameter.split(', '))
    return ', '.join(sorted_parameter)


def get_network_cell_params(row):
    """
    Get parameters for comparing with atoll values.

    Args:
        row (namedtuple): a cell data selected from network

    Returns:
        dict
    """
    cell_params = {}
    for param_name in row._fields:
        if param_name == 'cell':
            continue
        elif param_name in {'site', 'bsc'}:
            cell_params[param_name] = handle_node(getattr(row, param_name))
        elif param_name in {'tch', 'maio'}:
            cell_params[param_name] = handle_maio_tch(getattr(row, param_name))
        else:
            cell_params[param_name] = handle_parameter(getattr(row, param_name))
    return cell_params
