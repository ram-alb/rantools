from collections import namedtuple

from utils.atoll import select


def select_network_params():
    """
    Select WCDMA network parameters.

    Returns:
        list: a list of namedtuples
    """
    sql_command = """
        SELECT
            rncname,
            sitename,
            utrancell,
            localcellid,
            uarfcndl,
            psc,
            lac,
            rac,
            sac
        FROM wcdmacells2
        WHERE operator = 'Kcell'
    """

    row_factory = namedtuple(
        'NetworkParams',
        [
            'rnc',
            'site',
            'cell',
            'cellid',
            'uarfcndl',
            'psc',
            'lac',
            'rac',
            'sac',
        ],
    )

    return select(sql_command, row_factory=row_factory)


def select_atoll_params():
    """
    Select WCDMA parameters from atoll.

    Returns:
        list: list of namedtuples
    """
    sql_command = """
        SELECT
            rnc_name,
            site_name,
            cell_id,
            cell_identity,
            carrier,
            scrambling_code,
            lac,
            rac,
            sac
        FROM atoll_mrat.ucells
        WHERE active = -1
    """

    row_factory = namedtuple(
        'AtollParams',
        [
            'rnc',
            'site',
            'cell',
            'cellid',
            'uarfcndl',
            'psc',
            'lac',
            'rac',
            'sac',
        ],
    )

    return select(sql_command, row_factory=row_factory)
