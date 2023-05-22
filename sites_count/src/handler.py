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


def handle_selected_data(selected_data):
    """
    Handle selected data from the db.

    Args:
        selected_data (namedtuple): sites count data selected from db

    Returns:
        list: a list of list
    """
    selected_data_dict = selected_data._asdict()

    filtered_selected_data = {
        field: selected_data_dict[field] for field in selected_data_dict.keys()
        if 'created_at' not in field and 'iot' not in field
    }

    sites_data = []

    for field, field_val in filtered_selected_data.items():
        if 'total' in field:
            header = get_header(field)
            total = field_val
            row = []
        elif 'nr5g' in field:
            row.append(field_val)
            sites_data.append([header, *row, total])
        elif 'zte_wcdma' in field:
            row.append(field_val)
            sites_data.append([header, *row, 0, 0, total])
        else:
            row.append(field_val)

    return sorted(sites_data)
