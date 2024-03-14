from bff import Database
from db_config import common_config

class AddData:
    def __init__(self, common_config):
        self.common_config = common_config
        self.database = Database(self.common_config['dbname'], self.common_config['user'], self.common_config['host'], self.common_config['password'])

    def add_to_widgets(self, data_dict):
        self.database.run_table('widgets', data_dict)

    def add_to_reports(self, data_dict):
        self.database.run_table('reports', data_dict)

    def add_to_sources(self, data_dict):
        self.database.run_table('sources', data_dict)

    def add_to_threads(self, data_dict):
        self.database.run_table('threads', data_dict)

    def add_to_users(self, data_dict):
        self.database.run_table('users', data_dict)
