from collections import namedtuple

from sites_count.src.select_sites import select


def select_by_regions(requested_date):
    """
    Select site count data counted by regions.

    Args:
        requested_date (datetime.date): The requested date to filter the data

    Returns:
        list: A list of rows fetched from the database.
    """
    sql_command = """
        SELECT * FROM sites_by_regions
        WHERE created_at = :requested_date
    """

    sql_params = {'requested_date': requested_date}

    row_factory = namedtuple('SitesByRegions', [
        'created_at',
        'abay_region_total',
        'abay_region_gsm',
        'abay_region_wcdma',
        'abay_region_lte',
        'abay_region_nr5g',
        'akmola_region_total',
        'akmola_region_gsm',
        'akmola_region_wcdma',
        'akmola_region_lte',
        'akmola_region_nr5g',
        'aktobe_region_total',
        'aktobe_region_gsm',
        'aktobe_region_wcdma',
        'aktobe_region_lte',
        'aktobe_region_nr5g',
        'almaty_city_total',
        'almaty_city_gsm',
        'almaty_city_wcdma',
        'almaty_city_lte',
        'almaty_city_nr5g',
        'almaty_region_total',
        'almaty_region_gsm',
        'almaty_region_wcdma',
        'almaty_region_lte',
        'almaty_region_nr5g',
        'astana_total',
        'astana_gsm',
        'astana_wcdma',
        'astana_lte',
        'astana_nr5g',
        'atyrau_region_total',
        'atyrau_region_gsm',
        'atyrau_region_wcdma',
        'atyrau_region_lte',
        'atyrau_region_nr5g',
        'east_kz_region_total',
        'east_kz_region_gsm',
        'east_kz_region_wcdma',
        'east_kz_region_lte',
        'east_kz_region_nr5g',
        'karaganda_region_total',
        'karaganda_region_gsm',
        'karaganda_region_wcdma',
        'karaganda_region_lte',
        'karaganda_region_nr5g',
        'kostanay_region_total',
        'kostanay_region_gsm',
        'kostanay_region_wcdma',
        'kostanay_region_lte',
        'kostanay_region_nr5g',
        'kyzylorda_region_total',
        'kyzylorda_region_gsm',
        'kyzylorda_region_wcdma',
        'kyzylorda_region_lte',
        'kyzylorda_region_nr5g',
        'mangystau_region_total',
        'mangystau_region_gsm',
        'mangystau_region_wcdma',
        'mangystau_region_lte',
        'mangystau_region_nr5g',
        'north_kz_region_total',
        'north_kz_region_gsm',
        'north_kz_region_wcdma',
        'north_kz_region_lte',
        'north_kz_region_nr5g',
        'pavlodar_region_total',
        'pavlodar_region_gsm',
        'pavlodar_region_wcdma',
        'pavlodar_region_lte',
        'pavlodar_region_nr5g',
        'shymkent_total',
        'shymkent_gsm',
        'shymkent_wcdma',
        'shymkent_lte',
        'shymkent_nr5g',
        'turkestan_region_total',
        'turkestan_region_gsm',
        'turkestan_region_wcdma',
        'turkestan_region_lte',
        'turkestan_region_nr5g',
        'ulytau_region_total',
        'ulytau_region_gsm',
        'ulytau_region_wcdma',
        'ulytau_region_lte',
        'ulytau_region_nr5g',
        'west_kz_region_total',
        'west_kz_region_gsm',
        'west_kz_region_wcdma',
        'west_kz_region_lte',
        'west_kz_region_nr5g',
        'zhambyl_region_total',
        'zhambyl_region_gsm',
        'zhambyl_region_wcdma',
        'zhambyl_region_lte',
        'zhambyl_region_nr5g',
        'zhetysu_region_total',
        'zhetysu_region_gsm',
        'zhetysu_region_wcdma',
        'zhetysu_region_lte',
        'zhetysu_region_nr5g',
    ])

    return select(sql_command, sql_params, row_factory)
