import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://freelance.habr.com/tasks"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    task_elements = soup.find_all('div', class_='task__title')

    for task in task_elements:
        a_tag = task.find('a')
        if a_tag:
            urls = a_tag.get('href')
            title = a_tag.get_text(strip=True)
            complete_urls = urljoin(url, urls)
            print(f'Заказ: {title}')
            print(f'Ссылка: {complete_urls}')
            if ' бот' in title:
                print(f'\n{title}')
                print(f'Ссылка: {complete_urls}\n')
        else:
            print("No <a> tag found inside the task__title div.")

else:
    print('Не удалось выполнить запрос к сайту')
