# Generated by Django 2.0.2 on 2018-03-06 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_type', models.CharField(max_length=15)),
                ('db_filename', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='TableInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=50)),
                ('info_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hulsite.DataBaseInfo')),
            ],
        ),
    ]
