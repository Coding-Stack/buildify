# Generated by Django 3.1.1 on 2020-10-31 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201029_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='construction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.construction'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='wage',
            field=models.FloatField(blank=True),
        ),
    ]
