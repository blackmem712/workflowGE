# Generated by Django 4.2.7 on 2023-11-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('endereco', models.TextField()),
                ('cidade', models.CharField(max_length=12)),
                ('telefone', models.CharField(max_length=50)),
            ],
        ),
    ]