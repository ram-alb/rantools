import os

import cx_Oracle


def get_connection():
    """
    Return connection object for atoll db.

    Returns:
        cx_Oracle connection object
    """
    atoll_dsn = cx_Oracle.makedsn(
        os.getenv('ATOLL_HOST'),
        os.getenv('ATOLL_PORT'),
        service_name=os.getenv('SERVICE_NAME'),
    )
    return cx_Oracle.connect(
        user=os.getenv('ATOLL_LOGIN'),
        password=os.getenv('ATOLL_PASSWORD'),
        dsn=atoll_dsn,
    )


def select(sql_command, sql_params=None, row_factory=None):
    """
    Select data from atoll db.

    Args:
        sql_command (str): SQL select command
        sql_params (dict): parameters for select command
        row_factory (function): fucntion which handle row

    Returns:
        list: fetchall result
    """
    connection = get_connection()
    cursor = connection.cursor()
    if sql_params:
        cursor.execute(sql_command, sql_params)
    else:
        cursor.execute(sql_command)

    if row_factory:
        cursor.rowfactory = row_factory
    selected_data = cursor.fetchall()
    cursor.close()
    connection.close()
    return selected_data
