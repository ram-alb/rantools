import os

import cx_Oracle


def select(sql_command, sql_params, row_factory):
    """
    Execute a SQL query to select sites count data from the database.

    Args:
        sql_command (str): The SQL command to be executed
        sql_params (dict): The parameters to be used in the SQL query
        row_factory (callable): A function used to create a custom row object
            for each row fetched

    Returns:
        list: A list of rows fetched from the database.
    """
    atoll_dsn = cx_Oracle.makedsn(
        os.getenv('ATOLL_HOST'),
        os.getenv('ATOLL_PORT'),
        service_name=os.getenv('SERVICE_NAME'),
    )
    with cx_Oracle.connect(
        user=os.getenv('ATOLL_LOGIN'),
        password=os.getenv('ATOLL_PASSWORD'),
        dsn=atoll_dsn,
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_command, sql_params)
        cursor.rowfactory = row_factory
        return cursor.fetchall()
