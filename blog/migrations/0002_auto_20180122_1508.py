# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(help_text=b'Post comment', null=True, blank=True)),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'article', b'Article'), (b'blog', b'Blog'), (b'question', b'Question')]),
            preserve_default=True,
        ),
    ]
