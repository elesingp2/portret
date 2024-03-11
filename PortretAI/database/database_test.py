from db_config import common_config
from add_data import AddData

db = AddData(common_config)
tuple = (52, 82, 'Widget 2', '2024-03-10 15:00:00', '{"reports": [4, 5]}', '2024-03-10 15:30:00', 2)
db.add_to_widgets(tuple)