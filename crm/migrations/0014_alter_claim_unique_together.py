# Generated by Django 3.2.5 on 2021-07-27 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20210727_2023'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='claim',
            unique_together={('name', 'category', 'owner')},
        ),
    ]