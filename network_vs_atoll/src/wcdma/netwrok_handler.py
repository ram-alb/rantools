def get_cell_network_params(row):
    """
    Get network cell parameters for comparing.

    Args:
        row (namedtuple): cell parameters fetched from network

    Returns:
        dict: a dict with parameters for comparing
    """
    return {
        parameter: getattr(row, parameter)
        for parameter in row._fields
        if parameter != 'cell'
    }
