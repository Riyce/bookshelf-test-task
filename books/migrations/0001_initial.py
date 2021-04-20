# Generated by Django 3.2 on 2021-04-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('year', models.IntegerField(verbose_name='Release date')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['-id'],
            },
        ),
    ]