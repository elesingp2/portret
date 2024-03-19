import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from db_config import common_config
from db_operations import AddData

# Initialize AddData with the common configuration
adder = AddData(common_config)

# Adding a new user
adder._add_to_users({
    'username': 'johndoe'
})

# Adding a new widget
adder._add_to_widgets({
    'user_id': 1,
    'widget_name': 'Weather Widget',
    'key_words': ['weather', 'forecast'],
    'sources_id': ['1', '2'],
    'schedule_hour': 14
})

# Adding a new report
adder._add_to_reports({
    'widget_id': 1,
    'create_dttm': '2024-01-01 00:00:00',
    'filepath': '{"path": "path/to/file"}',
    'period_flag': True,
    'report_text': '{"content": "Report content here"}'
})

# Adding a new source
adder._add_to_sources({
    'name': 'Source Name',
    'in_use_flag': True
})

# Adding a new thread
adder._add_to_threads({
    'report_id': 1,
    'create_dttm': '2024-01-02 00:00:00',
    'extension_text': 'Some extended text',
    'thread_text': '{"thread_content": "Thread content here"}'
})
