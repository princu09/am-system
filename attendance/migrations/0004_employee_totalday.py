# Generated by Django 3.2.5 on 2021-07-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_attedance_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='totalDay',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
