# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0014_auto_20170113_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='platform',
            field=models.CharField(help_text=b'Platform name', max_length=255, choices=[(b'twitter', b'Twitter'), (b'flickr', b'Flickr'), (b'weibo', b'Weibo'), (b'tumblr', b'Tumblr'), (b'instagram', b'Instagram')]),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='host',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='instance',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='service',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='historicalcredential',
            name='platform',
            field=models.CharField(help_text=b'Platform name', max_length=255, choices=[(b'twitter', b'Twitter'), (b'flickr', b'Flickr'), (b'weibo', b'Weibo'), (b'tumblr', b'Tumblr'), (b'instagram', b'Instagram')]),
        ),
    ]
