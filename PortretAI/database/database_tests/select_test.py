import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from db_config import common_config
from db_operations import SelectData

selector = SelectData(common_config)

# Select all columns from the 'users' table
all_users = selector._select_from_users()
print("All users:", all_users)

# Select specific columns from the 'widgets' table with a condition
specific_widgets = selector._select_from_widgets(conditions="WHERE user_id = 1", columns="widget_name, key_words")
print("Specific widgets for user_id 1:", specific_widgets)

# Select all data from the 'reports' table without any conditions
all_reports = selector._select_from_reports()
print("All reports:", all_reports)

