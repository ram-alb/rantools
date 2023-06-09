from collections import namedtuple

from utils.atoll import select


def select_network_params():
    """
    Select NR network parameters.

    Returns:
        list: a list of namedtuples
    """
    sql_command = """
        SELECT
            subnetwork,
            sitename,
            cellname,
            cellid,
            nrpci,
            nrtac,
            rachrootsequence,
            arfcndl,
            bschannelbwdl
        FROM nrcells
    """

    row_factory = namedtuple(
        'NetworkParams',
        [
            'subnetwork',
            'site',
            'cell',
            'cellid',
            'pci',
            'tac',
            'prach',
            'arfcndl',
            'bandwidth',
        ],
    )

    return select(sql_command, row_factory=row_factory)


def select_atoll_params():
    """
    Select NR parameters from atoll.

    Returns:
        list: list of namedtuples
    """
    sql_command = """
        SELECT
            t.site_name,
            c.cell_id,
            c.unique_id,
            c.pci,
            c.tac,
            c.prach_rsi_list,
            c.carrier
        FROM atoll_mrat.xgcells5gnr c
            LEFT JOIN atoll_mrat.xgtransmitters t
                ON c.tx_id = t.tx_id
        WHERE c.active = -1
    """

    row_factory = namedtuple(
        'AtollParams',
        [
            'site',
            'cell',
            'cellid',
            'pci',
            'tac',
            'prach',
            'carrier',
        ],
    )

    return select(sql_command, row_factory=row_factory)
