# Generated by Django 3.0.3 on 2020-03-11 12:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_to', models.CharField(max_length=100, verbose_name='問合せ先')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス')),
                ('priority', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='優先度')),
                ('remarks', models.TextField(blank=True, verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='種類')),
                ('priority', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='優先度')),
                ('remarks', models.TextField(blank=True, verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='OriginalDocPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255, verbose_name='場所名')),
                ('priority', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='優先度')),
                ('remarks', models.TextField(blank=True, verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, verbose_name='内容')),
                ('date', models.DateField(blank=True, null=True, verbose_name='作成年月日')),
                ('is_public', models.IntegerField(choices=[(0, '非公開'), (1, '公開')], default=0, verbose_name='公開状態')),
                ('url', models.URLField(blank=True, max_length=250, verbose_name='資料URL')),
                ('image', models.URLField(blank=True, max_length=250, verbose_name='表紙URL')),
                ('barcode', models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator(message='半角英数のみ', regex='^[0-9]{8}$')], verbose_name='資料コード')),
                ('backup', models.CharField(blank=True, max_length=250, verbose_name='バックアップファイル')),
                ('keywords', models.TextField(blank=True, verbose_name='キーワード')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='登録日')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='更新日')),
                ('contact_to', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FinDocs.Contact', verbose_name='問合せ先')),
                ('original', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FinDocs.OriginalDocPlace', verbose_name='原本所在')),
                ('type', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FinDocs.DocType', verbose_name='種類')),
            ],
        ),
    ]
