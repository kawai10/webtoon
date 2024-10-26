from django.contrib.postgres.fields import ArrayField
from django.db import models


class Comic(models.Model):
    title = models.CharField(blank=False, default='', verbose_name='웹툰타이틀')
    synopsis = models.CharField(null=True, verbose_name='줄거리')
    genre = models.CharField(blank=False, default='', verbose_name='장르')
    write_author = ArrayField(models.PositiveIntegerField(), null=False, default=[], verbose_name='글작가')
    paint_author = ArrayField(models.PositiveIntegerField(), null=False, default=[], verbose_name='그림작가')
    origin_author = ArrayField(models.PositiveIntegerField(), null=False, default=[], verbose_name='원작작가')
    is_complete = models.BooleanField(null=False, default=False, verbose_name='완결여부')
    view_count = models.IntegerField(null=False, default=0, verbose_name='조회수')
    like_count = models.IntegerField(null=False, default=0, verbose_name='좋아요수')
    wait_free_time = models.PositiveSmallIntegerField(null=False, default=0, verbose_name='기다무 시간')
    tags =  ArrayField(models.IntegerField(), null=False, default=[], verbose_name='태그')
    release_day = models.CharField(blank=True, default='', verbose_name='연재요일')
    is_adult = models.BooleanField(null=False, default=False, verbose_name='성인')
    poster_image = models.CharField(blank=True, verbose_name='작품 메인 포스터')
    reserve_open_date = models.DateTimeField(null=True, verbose_name='예약일')

    def __str__(self):
        return self.title