def get_header(field_name):
    """
    Get header from the field_name of namedtuple.

    Args:
        field_name (str): a field name of namedtuple indtance

    Returns:
        str
    """
    if '_total' in field_name:
        header = field_name.replace('_total', '').capitalize()
    else:
        header = 'Total'
    return header


def handle_selected_sites(selected_sites):
    """
    Handle selected sites data from the db.

    Args:
        selected_sites (namedtuple): sites data selected from db

    Returns:
        list: a list of list
    """
    sites_data = []
    for field in selected_sites._fields:
        if field == 'created_at' or 'iot' in field:
            continue
        elif 'total' in field:
            header = get_header(field)
            total = getattr(selected_sites, field)
            row = []
        elif 'nr5g' in field:
            row.append(getattr(selected_sites, field))
            sites_data.append([header, *row, total])
        elif 'zte_wcdma' in field:
            row.append(getattr(selected_sites, field))
            sites_data.append([header, *row, 0, 0, total])
        else:
            row.append(getattr(selected_sites, field))
    return sorted(sites_data)
