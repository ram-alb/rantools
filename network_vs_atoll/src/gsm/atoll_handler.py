import re


def handle_atoll_parameter(atoll_parameter):
    """
    Handle GSM atoll parameter to make it int instance.

    Args:
        atoll_parameter (str or int): GSM parameter from atoll

    Returns:
        int
    """
    if atoll_parameter in {0, '0'}:
        return 0
    if not atoll_parameter:
        return -1
    if isinstance(atoll_parameter, str):
        parameter = re.sub(r'\D', '', atoll_parameter)
        return int(parameter)
    return int(atoll_parameter)


def handle_maio_data(selected_maio):
    """
    Handle GSM maio data selected from atoll.

    Args:
        selected_maio (list): a list of namedtuples fetched from atoll

    Returns:
        dict: each key is a cell, value is maio data
    """
    maios = {}
    for maio_data in selected_maio:
        if maio_data.maio or maio_data.maio == 0:
            maio = str(maio_data.maio)
            maios.setdefault(maio_data.cell, []).append(maio)
        else:
            maios.setdefault(maio_data.cell, []).append('-1')

    return maios


def handle_bsic(atoll_bsic):
    """
    Handle bsic selected from atoll.

    Args:
        atoll_bsic (str): GSM cell BSIC from atoll

    Returns:
        tuple: ncc and bcc
    """
    if atoll_bsic == '0':
        return (0, 0)
    elif atoll_bsic is None:
        return (-1, -1)
    elif len(atoll_bsic) == 1:
        return (0, int(atoll_bsic))

    ncc = int(atoll_bsic[0])
    bcc = int(atoll_bsic[1])
    return (ncc, bcc)


def handle_atoll_tch(atoll_tch, bcch):
    """
    Handle tch data selected from atoll.

    Args:
        atoll_tch (str): tch data from atoll
        bcch (int): bcch value selected from atoll

    Returns:
        str: handled tch data from atoll

    """
    if not atoll_tch or not atoll_tch.replace(' ', ''):
        return ''
    tch_list = atoll_tch.split(' ')

    sorted_tch_list = sorted(
        [tch for tch in tch_list if tch and tch != str(bcch)],
    )

    return ', '.join(sorted_tch_list)


def handle_gsm_atoll_data(selected_cell_data, selected_maio_data):
    """
    Handle all GSM parameters selected from atoll.

    Args:
        selected_cell_data (list): a list of namedtuples with GSM params
        selected_maio_data (list): a list of namedtuples with maio data

    Returns:
        dict: keys are the cells, values are the dicts with cell parameters

    """
    maios = handle_maio_data(selected_maio_data)

    atoll_params = {}
    for cell in selected_cell_data:
        ncc, bcc = handle_bsic(cell.bsic)
        bcch = handle_atoll_parameter(cell.bcch)
        try:
            maio = maios[cell.cell]
        except KeyError:
            maio = ['-1']
        atoll_params[cell.cell] = {
            'bsc': cell.bsc if cell.bsc else '',
            'site': cell.site,
            'lac': handle_atoll_parameter(cell.lac),
            'cellid': handle_atoll_parameter(cell.cellid),
            'bcch': bcch,
            'ncc': ncc,
            'bcc': bcc,
            'tch': handle_atoll_tch(cell.tch, bcch),
            'hsn': handle_atoll_parameter(cell.hsn),
            'maio': ', '.join(sorted(maio)),
        }

    return atoll_params


def get_atoll_cell_params(cell, atoll_params):
    """
    Get parameters for one cell from atoll gsm cell data.

    Args:
        cell (str): a cell name
        atoll_params (dict): keys are cells, values are dicts of cell parameters

    Returns:
        dict: dict with parameters if cell found or default values
    """
    try:
        cell_atoll_params = atoll_params[cell]
    except KeyError:
        cell_atoll_params = {
            'bsc': '',
            'site': '',
            'lac': -1,
            'cellid': -1,
            'bcch': -1,
            'ncc': -1,
            'bcc': -1,
            'tch': '',
            'hsn': -1,
            'maio': '',
        }
    return cell_atoll_params
