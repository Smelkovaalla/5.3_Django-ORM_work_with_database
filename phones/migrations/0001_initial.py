# Generated by Django 4.0 on 2022-01-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('image', models.TextField()),
                ('release_date', models.TextField()),
                ('lte_exists', models.TextField()),
                ('slug', models.TextField()),
            ],
        ),
    ]
