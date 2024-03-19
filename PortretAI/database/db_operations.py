import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[0]
sys.path.insert(0, str(project_root))

from db_class import Database

class AddData:
    def __init__(self, common_config):
        self.common_config = common_config
        self.database = Database(self.common_config['dbname'], self.common_config['user'], self.common_config['host'], self.common_config['password'])

    def _add_to_widgets(self, data_dict):
        self.database.run_table('insert', 'widgets', data_dict)

    def _add_to_reports(self, data_dict):
        self.database.run_table('insert', 'reports', data_dict)

    def _add_to_sources(self, data_dict):
        self.database.run_table('insert', 'sources', data_dict)

    def _add_to_threads(self, data_dict):
        self.database.run_table('insert', 'threads', data_dict)

    def _add_to_users(self, data_dict):
        self.database.run_table('insert', 'users', data_dict)

class SelectData:
    def __init__(self, common_config):
        self.common_config = common_config
        self.database = Database(self.common_config['dbname'], self.common_config['user'], self.common_config['host'], self.common_config['password'])

    def _select_from_widgets(self, conditions=None, columns="*"):
        return self.database.run_table('select', 'widgets', conditions=conditions, return_columns=columns)

    def _select_from_reports(self, conditions=None, columns="*"):
        return self.database.run_table('select', 'reports', conditions=conditions, return_columns=columns)

    def _select_from_sources(self, conditions=None, columns="*"):
        return self.database.run_table('select', 'sources', conditions=conditions, return_columns=columns)

    def _select_from_threads(self, conditions=None, columns="*"):
        return self.database.run_table('select', 'threads', conditions=conditions, return_columns=columns)

    def _select_from_users(self, conditions=None, columns="*"):
        return self.database.run_table('select', 'users', conditions=conditions, return_columns=columns)


class UpdateData:
    def __init__(self, common_config):
        self.common_config = common_config
        self.database = Database(self.common_config['dbname'], self.common_config['user'], self.common_config['host'], self.common_config['password'])

    def _update_widgets(self, data_dict, conditions):
        self.database.run_table('update', 'widgets', data_dict=data_dict, conditions=conditions)

    def _update_reports(self, data_dict, conditions):
        self.database.run_table('update', 'reports', data_dict=data_dict, conditions=conditions)

    def _update_sources(self, data_dict, conditions):
        self.database.run_table('update', 'sources', data_dict=data_dict, conditions=conditions)

    def _update_threads(self, data_dict, conditions):
        self.database.run_table('update', 'threads', data_dict=data_dict, conditions=conditions)

    def _update_users(self, data_dict, conditions):
        self.database.run_table('update', 'users', data_dict=data_dict, conditions=conditions)


    
