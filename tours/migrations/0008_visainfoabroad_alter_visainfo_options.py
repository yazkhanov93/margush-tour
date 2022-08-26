# Generated by Django 4.1 on 2022-08-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_ordertouroutcountry_ordertourincountry'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaInfoAbroad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Информация про за рубежная Виза ',
            },
        ),
        migrations.AlterModelOptions(
            name='visainfo',
            options={'verbose_name_plural': 'Информация про Виза Туркменистана'},
        ),
    ]
