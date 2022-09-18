# Generated by Django 4.1 on 2022-08-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'register',
            },
        ),
    ]
