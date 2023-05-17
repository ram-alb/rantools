from datetime import date

from sites_count.src.handler import handle_selected_sites
from sites_count.src.select_by_operators import select_by_operators
from sites_count.src.select_by_regions import select_by_regions
from sites_count.src.select_by_vendors import select_by_vendors

today = date.today()


def get_site_data(table_type, requested_date=today):
    """
    Retrieve site data based on the table type and optional requested date.

    Args:
        table_type (str): The type of table to retrieve data from
            ('operator', 'vendor', 'region')
        requested_date (datetime.date, optional): The requested date
            to filter the data. Defaults to the current date

    Returns:
        list: The processed site data based on the specified table type
    """
    select_funcs = {
        'operator': select_by_operators,
        'vendor': select_by_vendors,
        'region': select_by_regions,
    }

    selected_sites = select_funcs[table_type](requested_date)

    return handle_selected_sites(selected_sites[0])
