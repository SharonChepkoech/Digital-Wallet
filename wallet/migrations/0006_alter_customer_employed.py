# Generated by Django 4.1.1 on 2022-09-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_account_id_alter_card_id_alter_currency_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='employed',
            field=models.BooleanField(choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed')], null=True),
        ),
    ]