from django.db import models
from embed_video.fields import EmbedVideoField
from urllib.parse import urlparse, parse_qs


# Create your models here.
class Subtitle(models.Model):
    title = models.CharField(max_length = 255)
    date =models.DateTimeField(auto_now_add= True)
    url = models.CharField(max_length = 255)
    
    # @property
    # def video_id(self):
    #     query = urlparse(self.url)
    #     if query.hostname == 'youtu.be':
    #         return query.path[1:]
    #     elif query.hostname in ('www.youtube.com', 'youtube.com'):
    #         if query.path == '/watch':
    #             p = parse_qs(query.query)
    #             return p['v'][0]
    #     # Handle other cases (e.g., /embed/, /v/) as needed
    #     return None

    def __str__(self):
        return f"Title: {self.title}\nURL: {self.url}\nDate: {self.date}"


    # def __str__(self):
    #     return self.title + " " + self.url + " " + self.date

