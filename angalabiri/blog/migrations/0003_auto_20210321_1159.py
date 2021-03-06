# Generated by Django 3.1.7 on 2021-03-21 10:59

import angalabiri.blog.models
import angalabiri.blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20190103_0846'),
        ('blog', '0002_post_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(help_text='Categorize this item.', to='category.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='Tag this item.', to='category.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='videos',
            field=models.FileField(blank=True, null=True, upload_to=angalabiri.blog.models.blog_file_path, validators=[angalabiri.blog.validators.file_validator], verbose_name='Upload Video'),
        ),
    ]
