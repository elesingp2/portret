import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

# Главный класс
from baseline.results import TextClusterAnalysis
from paths.comments_file_path import comments_file_path

# База данных
from database.db_config import common_config
from database.add_data import AddData

def add_to_database(common_config, ):
    db = AddData(common_config)
    tuple = (554094, 459400456, 'Widget 2', '2024-03-10 15:00:00', '{"reports": [4, 5]}', '2024-03-10 15:30:00', 2)
    db.add_to_widgets(tuple)

if __name__ == "__main__":
    
    # Создание экземпляра класса анализа
    analysis = TextClusterAnalysis(comments_file_path)
    
    # Выполнение анализа
    results = analysis.run_analysis()
    
    # Добавление в Базу данных
    add_to_database(common_config)

    # Отображение важных слов
    #print("\nВажные слова:")
    #for word, importance in results['important_words']:
        #print(f"{word}: {importance}")
    
    # Отображение силуэтного коэффициента
    print(f"\nСилуэтный коэффициент: {results['score']}")
    
    # Отображение саммаризации кластеров
    print("\nСаммаризация кластеров:")
    for cluster_id, summary in results['cluster_summaries'].items():
        print(f"\nКластер {cluster_id}:")
        print(summary)

    print("\nОтчет")
    print(results['report'])
