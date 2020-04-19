from django.db import models


# Create your models here.

class TestDemo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)


class MovieInfo(models.Model):
    movie_id = models.CharField(max_length=64, primary_key=True)  # 电影id
    title = models.CharField(max_length=128)  # 电影标题
    rate = models.CharField(max_length=32)  # 电影评分
    movie_url = models.CharField(max_length=128)  # 电影链接
    cover_url = models.CharField(max_length=128)  # 电影图片url
    cover_x = models.IntegerField()  # 电影图片长
    cover_y = models.IntegerField()  # 电影图片宽
    directors = models.CharField(max_length=128)  # 导演s
    actors = models.CharField(max_length=2048)  # 演员s
    duration = models.CharField(max_length=32)  # 时长
    region = models.CharField(max_length=32)  # 地区
    types = models.CharField(max_length=128)  # 类型
    release_year = models.CharField(max_length=63)  # 上映时间
    create_time = models.DateTimeField(max_length=63)  # 该记录创建时间
