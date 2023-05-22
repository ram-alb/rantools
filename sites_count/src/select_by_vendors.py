from collections import namedtuple

from sites_count.src.select_sites import select


def select_by_vendors(requested_date):
    """
    Select site count data counted by vendors.

    Args:
        requested_date (datetime.date): The requested date to filter the data

    Returns:
        list: A list of rows fetched from the database.
    """
    sql_command = """
        SELECT * FROM sites_by_vendors
        WHERE created_at = :requested_date
    """

    sql_params = {'requested_date': requested_date}

    row_factory = namedtuple('SitesByVendors', [
        'created_at',
        'ericsson_total',
        'ericsson_gsm',
        'ericsson_wcdma',
        'ericsson_lte',
        'ericsson_nr5g',
        'ericsson_iot',
        'zte_total',
        'zte_gsm',
        'zte_wcdma',
        'huawei_total',
        'huawei_gsm',
        'huawei_wcdma',
        'huawei_lte',
        'huawei_nr5g',
        'nokia_total',
        'nokia_gsm',
        'nokia_wcdma',
        'nokia_lte',
        'nokia_nr5g',
    ])

    return select(sql_command, sql_params, row_factory)
