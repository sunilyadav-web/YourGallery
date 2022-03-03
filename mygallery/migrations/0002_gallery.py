# Generated by Django 3.2.9 on 2022-02-24 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygallery.user')),
            ],
        ),
    ]