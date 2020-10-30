# Generated by Django 3.1.1 on 2020-10-29 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wages', models.FloatField()),
                ('prev_record', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('wall_thickness', models.IntegerField()),
                ('floors', models.IntegerField()),
                ('parking', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('modification', 'Ask For Modification'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=20)),
                ('drawing_plan', models.ImageField(blank=True, default='default.png', upload_to='drawing')),
                ('sectional_plan', models.ImageField(blank=True, default='default.png', upload_to='sectional')),
                ('floor_plan', models.ImageField(blank=True, default='default.png', upload_to='floor')),
                ('elevated_plan', models.ImageField(blank=True, default='default.png', upload_to='elevated')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
            ],
        ),
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.plan')),
                ('workers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
