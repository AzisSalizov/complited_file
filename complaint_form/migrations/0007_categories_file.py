# Generated by Django 4.1.4 on 2022-12-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_form', '0006_alter_categories_date_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Файл'),
        ),
    ]
