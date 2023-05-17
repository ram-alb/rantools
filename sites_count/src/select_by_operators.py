from collections import namedtuple

from sites_count.src.select_sites import select_sites


def select_by_operators(requested_date):
    """
    Select site count data counted by operators.

    Args:
        requested_date (datetime.date): The requested date to filter the data

    Returns:
        list: A list of rows fetched from the database.
    """
    sql_command = """
        SELECT * FROM sites_by_operators
        WHERE created_at = :requested_date
    """

    sql_params = {'requested_date': requested_date}

    row_factory = namedtuple('SitesByOperators', [
        'created_at',
        'total',
        'gsm',
        'wcdma',
        'lte',
        'nr5g',
        'iot',
        'kcell_total',
        'kcell_gsm',
        'kcell_wcdma',
        'kcell_lte',
        'kcell_nr5g',
        'kcell_iot',
        'tele2_total',
        'tele2_gsm',
        'tele2_wcdma',
        'tele2_lte',
        'tele2_nr5g',
        'beeline_total',
        'beeline_gsm',
        'beeline_wcdma',
        'beeline_lte',
        'beeline_nr5g',
    ])

    return select_sites(sql_command, sql_params, row_factory)
