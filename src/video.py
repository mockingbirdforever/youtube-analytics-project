from googleapiclient.discovery import build

api_key: str = 'AIzaSyCpqZR-QVjjfhbhGkzjox3JifLVbcyDXwE'

youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    """Коммент"""

    def __init__(self, video_id):
        self.__video_id = video_id
        self.video_response = youtube.videos().list(id=self.__video_id, part='snippet,statistics').execute()
        self.video_name: str = self.video_response['items'][0]['snippet']['title']
        self.video_url = 'https://www.youtube.com/watch?v=' + self.__video_id
        self.video_views = self.video_response['items'][0]['statistics']['viewCount']
        self.video_likes = self.video_response['items'][0]['statistics']['likeCount']

    @property
    def video_id(self):
        return self.__video_id

    def __str__(self):
        return f'{self.video_name}'


class PLVideo(Video):
    """Коммент"""

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

