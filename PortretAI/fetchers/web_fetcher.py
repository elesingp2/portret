import requests
from bs4 import BeautifulSoup

# Инициализация сессии для сохранения куки
session = requests.Session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def fetch_comments(url):
    try:
        # Использование сессии для запроса
        response = session.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
    except requests.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Предположим, что структура комментария включает автора, дату и текст
    comments = soup.select('.comment_content')

    for comment in comments:
        # Примеры извлечения данных, селекторы нужно адаптировать под ваш сайт
        author = comment.select_one('.author').get_text(strip=True) if comment.select_one('.author') else 'Аноним'
        date = comment.select_one('.date').get_text(strip=True) if comment.select_one('.date') else 'Неизвестная дата'
        text = comment.select_one('.text').get_text(strip=True) if comment.select_one('.text') else 'Текст отсутствует'

        print(f"Автор: {author}")
        print(f"Дата: {date}")
        print(f"Комментарий: {text}")
        print("-------------")

# Пример URL, замените его на реальный адрес
url = 'https://pikabu.ru/story/otvet_na_post_snova_dolbanyie_stripsyi_kfc_retsept_kucheryavosti_11205195#comments'
fetch_comments(url)
