# Generated by Django 3.1 on 2020-09-05 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20200905_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.TextField(),
        ),
    ]
