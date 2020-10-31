# Generated by Django 3.1.1 on 2020-10-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_merge_20201031_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('pending', 'Pending'), ('modification', 'Ask For Modification'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='new', max_length=20),
        ),
    ]