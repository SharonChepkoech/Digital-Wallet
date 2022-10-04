# Generated by Django 4.1.1 on 2022-10-04 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_remove_card_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_wallet', to='wallet.wallet'),
        ),
    ]