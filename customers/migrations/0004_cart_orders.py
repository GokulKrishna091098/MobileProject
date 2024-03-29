# Generated by Django 3.2 on 2021-05-14 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0005_alter_mobile_specs'),
        ('customers', '0003_auto_20210508_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('Ordered', 'Ordered'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Ordered', max_length=150)),
                ('user', models.CharField(max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.mobile')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('price_total', models.PositiveBigIntegerField(blank=True, editable=False, null=True)),
                ('user', models.CharField(max_length=120, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.mobile')),
            ],
        ),
    ]
