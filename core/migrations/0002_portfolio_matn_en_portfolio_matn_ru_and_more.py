# Generated by Django 4.1.3 on 2022-12-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='matn_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='matn_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='sarlovh_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='sarlovha_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='matn2_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='matn2_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='matn3_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='matn3_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='matn_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='matn_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sarlovha_en',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='sarlovha_ru',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
