# Generated by Django 4.2.1 on 2023-05-09 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=800)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Area_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=800)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.area')),
            ],
        ),
        migrations.CreateModel(
            name='Area_new_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=800)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.area')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('jurnalist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bisnes_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=800)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intervyu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('youtube_link', models.CharField(max_length=1000)),
                ('talked', models.CharField(max_length=100)),
                ('painter', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='New_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=800)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('youtube_link', models.CharField(max_length=1000)),
                ('jurnalist', models.CharField(max_length=100)),
                ('interlocutor', models.CharField(max_length=100)),
                ('new_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.new_type')),
            ],
        ),
        migrations.CreateModel(
            name='Video_new_piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=10000)),
                ('video_new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.video_new')),
            ],
        ),
        migrations.CreateModel(
            name='Intervyu_piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('intervyu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.intervyu')),
            ],
        ),
        migrations.CreateModel(
            name='Bisnes_new_piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('bisnes_new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.bisnes_new')),
            ],
        ),
        migrations.CreateModel(
            name='Area_new_piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('area_new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.area_new')),
            ],
        ),
        migrations.CreateModel(
            name='Area_new_list_piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='images/')),
                ('area_new_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kun_uz.area_new_list')),
            ],
        ),
    ]
