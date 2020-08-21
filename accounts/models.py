from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _ 

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True # 선택적으로 관리자를 마이그레이션으로 직렬화한다.
                             # True로 설정된 경우 관리자가 마이그레이션으로 직렬화되며...?

    # 유저 생성
    # 파라미터로 전달받은 값들을 user 객체로 db에 저장한다
    # nomalize 중복 최소화를 위한 정규화?
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일이 없습니다.')

        eamil = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 일반 유저 생성
    # 일반 사용자를 생성한다. is_staff, is_superuser = False ==> 일반유저라는 뜻
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('관리자는 is_staff가 True여야함')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('관리자는 is_superuser가 True여야함')

        return self._create_user(email, password, **extra_fields)

    

class User(AbstractBaseUser, PermissionsMixin):
    '''
    커스터마이징한 User 모델
    '''
    objects = UserManager()

    email = models.EmailField(
        verbose_name=_('email_id'),
        max_length=64,
        unique=True,
        help_text='EMAIL ID'
    )

    username = models.CharField(
        max_length=32,
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('관리자 권한을 가지고 있는지 확인하세요.')
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            '활성화된 사용자인지 비활성화 사용자인지 선택하세요.'
            '삭제하는 것 보단 비활성화를 추천드립니다.'
        )
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


# class Profile(models.Models):
#     user = modesl.OneToOneField(User, on_delete=models.CASCADE)
#     user_pk = models.IntegerField(black=True)
#     nickname = models.CharField(max_length=200, blank=True)
#     point = models.IntegerField(default=0)
#     phone = models.CharField(max_length=200, blank)