import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


class PepParsePipeline:
    """Обрабатывает и сохраняет статистику по статусам PEP в CSV файл."""

    def __init__(self):
        self.results_dir = None
        self.file_name = None
        self.file_path = None
        self.status_count = None

    def open_spider(self, spider):
        """Инициализирует директорию и файл для сохранения данных."""
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)
        self.file_name = f'status_summary_{DATETIME}.csv'
        self.file_path = self.results_dir / self.file_name
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        """Подсчитывает количество каждого статуса PEP."""
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Записывает статистику в CSV файл при завершении работы паука."""
        self.status_count['Total'] = sum(self.status_count.values())
        with open(self.file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_count.items())
