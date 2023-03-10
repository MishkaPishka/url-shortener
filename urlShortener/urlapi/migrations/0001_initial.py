# Generated by Django 4.1.4 on 2023-01-22 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalUrl',
            fields=[
                ('url', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, unique=True, verbose_name='Short URL')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hit_count', models.IntegerField(default=0)),
                ('is_permanent', models.BooleanField(default=True)),
                ('original_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urlapi.originalurl')),
            ],
        ),
        migrations.CreateModel(
            name='LinkHit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=200, verbose_name='IP of user')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urlapi.shorturl')),
            ],
        ),
    ]
