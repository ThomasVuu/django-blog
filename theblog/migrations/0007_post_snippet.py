# Generated by Django 4.2.4 on 2023-08-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read blog post', max_length=255),
        ),
    ]
