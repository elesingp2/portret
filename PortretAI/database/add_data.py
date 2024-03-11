from bff import Database
from db_config import common_config

class AddData:
    def __init__(self, common_config):
        self.common_config = common_config

    def add_to_widgets(self, tuple):
        configurations_tuples = [
            tuple
        ]

        database = Database(self.common_config['dbname'], self.common_config['user'], self.common_config['host'])

        self.columns = [
            'user_id',
            'widget_id',
            'widget_name',
            'first_report_created_at',
            'reports_created_at_json',
            'new_report_created_at',
            'report_count'
        ]

        database.run_table('reports', configurations_tuples, self.columns)