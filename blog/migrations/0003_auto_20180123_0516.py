# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180122_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(help_text=b'Post comment', null=True, blank=True)),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
