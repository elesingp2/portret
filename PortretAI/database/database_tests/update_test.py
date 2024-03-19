import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from db_config import common_config
from db_operations import UpdateData

updater = UpdateData(common_config)

# Update a record in the 'users' table
updater._update_users(
    data_dict={'username': 'newusername'},
    conditions="WHERE username = 'johndoe'"
)
print("Updated username for johndoe.")

# Update multiple fields in a 'widgets' table record
updater._update_widgets(
    data_dict={'widget_name': 'Updated Widget', 'schedule_hour': 123456},
    conditions="WHERE widget_id = 1"
)
print("Updated widget_name and schedule_hour for widget_id 1.")

# Update a 'reports' table record conditionally
updater._update_reports(
    data_dict={'report_text': '{"content": "`ЧЛЕНикс`"}'},
    conditions="WHERE reports_id = 3"
)
print("Updated report_text for report_id 1.")
