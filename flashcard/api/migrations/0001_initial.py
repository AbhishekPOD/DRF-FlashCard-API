# Generated by Django 4.2.4 on 2023-08-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.CharField(max_length=30)),
                ('back', models.CharField(max_length=30)),
                ('source_language', models.CharField(max_length=30)),
                ('target_language', models.CharField(max_length=30)),
                ('difficulty', models.IntegerField()),
            ],
        ),
    ]