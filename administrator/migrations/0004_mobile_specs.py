# Generated by Django 3.2 on 2021-05-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_delete_changepassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='specs',
            field=models.CharField(default='empty', max_length=120),
        ),
    ]