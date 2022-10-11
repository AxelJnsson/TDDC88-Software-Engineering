# Generated by Django 4.1.1 on 2022-09-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_article_alternative_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='alternative_articles',
        ),
        migrations.AlterField(
            model_name='article',
            name='alternative_names',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='alternative_articles',
            field=models.ManyToManyField(blank=True, null=True, to='backend.article'),
        ),
    ]
