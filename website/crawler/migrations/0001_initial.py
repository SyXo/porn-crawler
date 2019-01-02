# Generated by Django 2.0.2 on 2019-01-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField()),
            ],
            options={
                'db_table': 'query',
            },
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
                ('logo', models.TextField()),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='videos_after_searched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
                ('logo', models.TextField()),
            ],
            options={
                'db_table': 'videos_after_searched',
            },
        ),
    ]