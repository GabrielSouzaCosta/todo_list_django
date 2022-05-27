# Generated by Django 4.0.4 on 2022-05-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('doing', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
