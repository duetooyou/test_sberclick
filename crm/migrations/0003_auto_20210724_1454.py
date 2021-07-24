# Generated by Django 3.2.5 on 2021-07-24 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210723_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='text',
            field=models.TextField(default=1, max_length=400, verbose_name='Содержание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='claim',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='to_bids', to='crm.category', verbose_name='Категория'),
        ),
    ]