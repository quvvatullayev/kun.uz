# Generated by Django 4.2.1 on 2023-05-09 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kun_uz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day_new_piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('day_new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.day_new')),
            ],
        ),
    ]
