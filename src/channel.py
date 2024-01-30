import json
import os
from googleapiclient.discovery import build
import isodate
# from dotenv import load_dotenv

# load_dotenv()

api_key: str = 'AIzaSyCpqZR-QVjjfhbhGkzjox3JifLVbcyDXwE'

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.youtube['items'][0]['snippet']['title']
        self.channel_description = self.youtube['items'][0]['snippet']['description']
        self.video_count = self.youtube['items'][0]['statistics']['videoCount']
        self.url = 'https://www.youtube.com/channel/' + self.youtube['items'][0]['id']
        self.count_subscribers = self.youtube['items'][0]['statistics']['subscriberCount']
        self.total_count_views = self.youtube['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, file):
        """Mетод сохраняющий в файл значения атрибутов экземпляра Channel"""
        with open(file, 'w', encoding='cp1251') as f:
            data = {
                'title': self.title,
                'channel_description': self.channel_description,
                'url': self.url,
                'count_subscribers': self.count_subscribers,
                'video_count': self.video_count,
                'total_count_views': self.total_count_views,
                'channel_id': self.channel_id
            }
            json.dump(data, f, indent='\t')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=api_key)

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return (int(self.count_subscribers) + int(other.count_subscribers))

    def __sub__(self, other):
        return (int(self.count_subscribers) - int(other.count_subscribers))

    def __lt__(self, other):
        return (int(self.count_subscribers) < int(other.count_subscribers))

    def __gt__(self, other):
        return (int(self.count_subscribers) > int(other.count_subscribers))

    def __le__(self, other):
        return (int(self.count_subscribers) <= int(other.count_subscribers))

    def __ge__(self, other):
        return (int(self.count_subscribers) >= int(other.count_subscribers))
