# Generated by Django 2.2.1 on 2019-07-03 05:19

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.TextField(max_length=500)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('email', models.TextField(blank=True, max_length=500)),
                ('affiliation', models.TextField(blank=True, max_length=500)),
                ('name', models.TextField(blank=True, max_length=500)),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete='remove', related_name='u_fr', to=settings.AUTH_USER_MODEL)),
                ('viewing_user', models.ForeignKey(null=True, on_delete='remove', related_name='vu_fr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete='remove', related_name='u_f', to=settings.AUTH_USER_MODEL)),
                ('viewing_user', models.ForeignKey(null=True, on_delete='remove', related_name='vu_f', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]