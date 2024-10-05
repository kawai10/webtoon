from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models



class User(AbstractBaseUser):
    LOGIN_TYPE = [
        ('EMAIL', 'Email'),
        ('KAKAO', 'Kakao'),
        ('NAVER', 'Naver'),
        ('GOOGLE', 'Google'),
    ]

    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    class Meta:
        verbose_name_plural = 'users'

    email = models.EmailField(unique=True, max_length=50,verbose_name='이메일')
    password = models.CharField(max_length=50, verbose_name='비밀번호')
    age = models.PositiveSmallIntegerField(null=False,verbose_name='나이', default=0)
    gender = models.CharField(max_length=1, blank=True, verbose_name='성별', choices=GENDER)
    login_type = models.CharField(max_length=10, blank=True, verbose_name='로그인 타입', choices=LOGIN_TYPE)
    coin = models.PositiveIntegerField(default=0, verbose_name='코인')
    login_count = models.PositiveIntegerField(default=0, verbose_name='로그인 횟수')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='마지막 로그인')
    terms = models.BooleanField(default=False, verbose_name='이용약관')
    privacy = models.BooleanField(default=False, verbose_name='개인정보처리방침')
    isAdult = models.BooleanField(default=False, verbose_name='성인여부')
    is_superuser = models.BooleanField(default=False, verbose_name='슈퍼유저')
    is_staff = models.BooleanField(default=False, verbose_name='관리자')
    is_active = models.BooleanField(default=True, verbose_name='사용여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')
    deleted_at = models.DateTimeField(null=True, verbose_name='탈퇴일자')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []