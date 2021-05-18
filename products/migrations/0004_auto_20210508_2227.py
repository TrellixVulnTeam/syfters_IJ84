# Generated by Django 3.1.7 on 2021-05-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210505_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogRight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time', models.DateField()),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='LatestBlogRight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time', models.DateField()),
                ('content', models.TextField(verbose_name=550)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogLeft',
        ),
        migrations.RenameModel(
            old_name='LatestBlog',
            new_name='LatestBlogLeft',
        ),
    ]
