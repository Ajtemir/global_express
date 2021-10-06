# Generated by Django 3.2.7 on 2021-10-05 10:37

from django.db import migrations, models
import django.db.models.deletion
import sections.media_path


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название страны')),
            ],
            options={
                'verbose_name': 'страна',
                'verbose_name_plural': 'страны',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='url')),
                ('image', models.ImageField(upload_to=sections.media_path.shop_image, verbose_name='фотография')),
                ('icon', models.ImageField(unique=True, upload_to=sections.media_path.shop_icon, verbose_name='иконка')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='sections.country', verbose_name='страна')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
    ]
