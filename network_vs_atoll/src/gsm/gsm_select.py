from collections import namedtuple

from utils.atoll import select


def select_network_params():
    """
    Select network cell parameters.

    Returns:
        list: a list of namedtuples
    """
    sql_command = """
        SELECT
            bscname,
            sitename,
            cell,
            lac,
            cellid,
            bcch,
            ncc,
            bcc,
            tchfreqs,
            hsn,
            maio
        FROM gsmcells2
        WHERE operator = 'Kcell'
    """

    row_factory = namedtuple(
        'NetworkParams',
        [
            'bsc',
            'site',
            'cell',
            'lac',
            'cellid',
            'bcch',
            'ncc',
            'bcc',
            'tch',
            'hsn',
            'maio',
        ],
    )

    return select(sql_command, row_factory=row_factory)


def select_atoll_cell_params():
    """
    Select atoll cell parameters.

    Returns:
        list: a list of namedtuples
    """
    sql_command = """
        SELECT
            t.bsc,
            t.site_name,
            t.tx_id,
            t.lac,
            t.cell_identity,
            t.control_channel,
            t.bsic,
            t.channels,
            h.hsn
        FROM atoll_mrat.gtransmitters t
            LEFT JOIN atoll_mrat.gtrgs h
                ON t.tx_id = h.tx_id
        WHERE t.active = -1
            AND h.trx_type = 'TCH'
    """

    row_factory = namedtuple(
        'AtollParams',
        [
            'bsc',
            'site',
            'cell',
            'lac',
            'cellid',
            'bcch',
            'bsic',
            'tch',
            'hsn',
        ],
    )

    return select(sql_command, row_factory=row_factory)


def select_atoll_maio():
    """
    Select maio data from atoll.

    Returns:
        list: a list of namedtuples
    """
    sql_command = """
        SELECT
            trx.tx_id,
            trx.maio
        FROM atoll_mrat.gtrxs trx
        WHERE trx.trx_type = 'TCH'
        ORDER BY trx.tx_id
    """

    row_factory = namedtuple(
        'Maio',
        [
            'cell',
            'maio',
        ],
    )

    return select(sql_command, row_factory=row_factory)
