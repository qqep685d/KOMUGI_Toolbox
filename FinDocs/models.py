from django.db import models
from django.core.validators import RegexValidator

class DocType(models.Model):
    """資料の種類"""
    name    = models.CharField('種類', max_length=100)
    priority= models.PositiveSmallIntegerField('優先度', null=True, blank=True)
    remarks = models.TextField('備考', blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    """資料の問合せ先"""
    contact_to = models.CharField('問合せ先', max_length=100)
    email      = models.EmailField('メールアドレス', max_length=254, null=True, blank=True)
    priority   = models.PositiveSmallIntegerField('優先度', null=True, blank=True)
    remarks    = models.TextField('備考', blank=True)

    def __str__(self):
        return self.contact_to

class OriginalDocPlace(models.Model):
    """原本の場所"""
    place    = models.CharField('場所名', max_length=255)
    priority = models.PositiveSmallIntegerField('優先度', null=True, blank=True)
    remarks  = models.TextField('備考', blank=True)

    def __str__(self):
        return self.place

class Doc(models.Model):
    public_or_not = ((0, '非公開'),(1, '公開'),)
    tel_number_regex = RegexValidator(regex=r'^[0-9]{8}$', message=("半角英数のみ"))

    """資料リスト"""
    title      = models.CharField('タイトル', max_length=80)
    type       = models.ForeignKey(DocType, verbose_name='種類', on_delete=models.SET_NULL, null=True, blank=True, default=1)
    content    = models.TextField('内容', blank=True)
    date       = models.DateField('作成年月日', blank=True, null=True)
    contact_to = models.ForeignKey(Contact, verbose_name='問合せ先', on_delete=models.SET_NULL, null=True, blank=True, default=1)
    is_public  = models.IntegerField(choices=public_or_not, verbose_name='公開状態', default=0)
    url        = models.URLField('資料URL', max_length=250, blank=True)
    image      = models.URLField('表紙URL', max_length=250, blank=True)
    barcode    = models.CharField('資料コード', max_length=8, blank=True, validators=[tel_number_regex], unique=False)
    original   = models.ForeignKey(OriginalDocPlace, verbose_name='原本所在', on_delete=models.SET_NULL, null=True, blank=True, default=1)
    backup     = models.CharField('バックアップファイル', max_length=250, blank=True)
    keywords   = models.TextField('キーワード', blank=True)
    created_at = models.DateField('登録日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    @property
    def get_year(self):
        if self.date:
            return self.date.strftime('%Y')

    def __str__(self):
        return self.title
