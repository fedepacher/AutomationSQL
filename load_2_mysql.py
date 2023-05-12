"""Module providing file insertion to mysql database."""
import os
import sys
import subprocess
import platform
import shutil
import re
import argparse
import json
import pandas as pd


from mysql_lib import MySQLClass


def get_path(os_var=''):
    """Get path to read and store csv files.

    Args:
        os_var (str): Operating system.

    Returns:
        (str): Folder to load files.
        (str): Folder to store csv files.
    """
    csv_path = ''
    load_path = ''

    return load_path, csv_path


def create_csv_store_path(csv_path=''):
    """Create folder to store csv files if not exist.

    Args:
        csv_path (str): Path where CSV files will be stored.
    """
    # Check if the directory represented by csv_path already exists
    if not os.path.exists(csv_path):
        try:
            # If it doesn't exist, create the directory
            os.makedirs(csv_path)
        except FileExistsError:
            # If an error occurs while creating the directory, display an error message and terminate the program
            print(f'Cannot create {csv_path}')
            sys.exit(0)
    
    # If the directory is successfully created, display a confirmation message
    print(f'{csv_path} folder created')



def convert_file_to_csv(load_path='', csv_path=''):
    """Convert xls file to csv and store csv files to new folder.

    Args:
        load_path (str): Path that contains files to be converted.
        csv_path (str): Path where CSV files will be stored.
    """


# Get all xls and csv files in the load folder
    file_list = os.listdir(load_path)
    xls_files = [f for f in file_list if f.endswith('.xls')]
    csv_files = [f for f in file_list if f.endswith('.csv')]

# Convert xls files to csv and copy csv files to the destination folder
    for file in xls_files + csv_files:
        try:
            if file.endswith('.xls'):
                df_data = pd.read_excel(os.path.join(load_path, file))
                filename, ext = os.path.splitext(file)
                csv_filename = f'{filename}.csv'
                df_data.to_csv(os.path.join(csv_path, csv_filename), index=None, header=True)
            elif file.endswith('.csv'):
                shutil.copyfile(os.path.join(load_path, file), os.path.join(csv_path, file))
            print(f'{file} has been converted and saved in {csv_path}')
        except Exception as error:
            print(error)
            print(f'An error occurred while processing {file}')
            sys.exit(0)

    print('Conversion completed successfully!')

def get_column_from_csv(csv_table_files=None, separator_list=None, column_list=None, csv_path=''):
    """Get column names list from csv files.

    Args:
        csv_table_files (list): File list that contains csv files.
        separator_list (list): List where separator will be stored.
        column_list (list): List where csv columns will be stored.
        csv_path (str): Path where CSV files are stored.
    """
    pass


def check_unknow_char(column_list=None):
    """Check for unknow characters when files are not UTF-8.

     Args:
        column_list (list): Column list to be returned.
    """
    pass


def get_query_table(csv_table_files=None, column_list=None, query_list=None):
    """Get queries to create tables.

    Args:
        csv_table_files (list): File list that contains csv files.
        column_list (list): List where csv columns are stored.
        query_list (list): List of query to create MySQL table.
    """
    pass


def get_passwords():
    """Get Workbench and sudo passwords from internal file.

    Returns:
        (str): Database Workbench password.
        (str): Linux admin password.
    """
    pass_db = ''
    pass_sudo = ''

    return pass_db, pass_sudo


def database_function(connection=None, db_name=''):
    """Create database if not exist and set database internal configurations.

    Args:
        connection (mysql_lib.MySQLClass): Connection object to mysql.
        db_name (str): Database name.
    """
    pass


def database_create_tables(connection=None, query_list=None):
    """Create database tables.

    Args:
        connection (mysql_lib.MySQLClass): Connection object to mysql.
        query_list (list): Query list to create tables.
    """
    pass


def copy_file_to_mysql_folder(csv_table_files=None, os_var='', db_name='', csv_path='',
                              pass_sudo=''):
    """Copy files to mysql folder to be read by Workbench.

    Args:
        csv_table_files (list): CSV files list.
        os_var (str): Operating system.
        db_name (str): Database name.
        csv_path (str): Path where CSV files are stored.
        pass_sudo (str): Linux admin password.
    """
    pass


def fill_database_tables(connection=None, csv_table_files=None, separator_list=None,
                         column_list=None):
    """Load database tables with CSV files

    Args:
        connection (mysql_lib.MySQLClass): Connection object to mysql.
        csv_table_files (list): CSV files list.
        separator_list (list): List with CVS columns separator.
        column_list (list): Table column list.
    """
    pass


def run():
    """Execute the code to convert csv files into MySQL database"""
    column_list = []
    separator_list = []
    query_list = []

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-t', '--host_name', metavar='<host_name>', type=str, required=False,
                            default='localhost', help='Workbench hostname', dest='host_name')
    arg_parser.add_argument('-u', '--user_name', metavar='<user_name>', type=str, required=False,
                            default='root', help='Workbench username', dest='user_name')
    arg_parser.add_argument('-d', '--database', metavar='<database>', type=str, required=False,
                            default='test_db', help='Database name', dest='db_name')

    args = arg_parser.parse_args()

    db_name = args.db_name
    os_var = platform.system()

    # Get path for storing and reading csv file
    load_path, csv_path = get_path(os_var=os_var)

    # Create csv_path directory if not exist
    create_csv_store_path(csv_path=csv_path)

    # Convert xls file to csv and copy files to new folder
    convert_file_to_csv(load_path=load_path, csv_path=csv_path)

    file_list = os.listdir(csv_path)

    # Get CSV files
    csv_table_files = [file for file in file_list if 'csv' in file]

    # Get column and return list of column and separators
    get_column_from_csv(csv_table_files=csv_table_files, separator_list=separator_list,
                        column_list=column_list, csv_path=csv_path)

    # Check for unknow characters when files are not UTF-8 and return value in clolumn_list
    check_unknow_char(column_list=column_list)

    # Get queries to create tables, return value in query_list
    get_query_table(query_list=query_list, csv_table_files=csv_table_files, column_list=column_list)

    # Get Workbench and super user Linux password passwords to copy file as admin
    pass_db, pass_sudo = get_passwords()

    # Connect to mySQL data base
    connection = MySQLClass(password=pass_db)

    # Create database
    database_function(connection=connection, db_name=db_name)

    # Create tables
    database_create_tables(connection=connection, query_list=query_list)

    # Copy files to mysql folder
    copy_file_to_mysql_folder(csv_table_files=csv_table_files, os_var=os_var, db_name=db_name,
                              csv_path=csv_path, pass_sudo=pass_sudo)

    # Fill tables
    fill_database_tables(connection=connection, csv_table_files=csv_table_files,
                         separator_list=separator_list, column_list=column_list)


# Driver Code
if __name__ == '__main__' :

    # Start script
    print('Create Database\n')

    # calling run function
    run()
