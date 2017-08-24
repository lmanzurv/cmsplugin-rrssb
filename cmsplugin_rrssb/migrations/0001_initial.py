# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialButton',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('button_type', models.CharField(default=b'FB', max_length=2, verbose_name='Button Type', choices=[(b'EM', b'Email'), (b'PR', b'Print'), (b'FB', b'Facebook'), (b'TB', b'Tumblr'), (b'LI', b'LinkedIn'), (b'TW', b'Twitter'), (b'RD', b'Reddit'), (b'VK', b'VK'), (b'HN', b'Hacker News'), (b'G+', b'Google Plus'), (b'PT', b'Pinterest'), (b'PK', b'Pocket'), (b'WA', b'Whatsapp')])),
                ('title', models.CharField(default='Check out this page', max_length=100, null=True, verbose_name='Subject', blank=True)),
                ('description', models.CharField(default='Check out this page', max_length=250, null=True, verbose_name='Body', blank=True)),
            ],
            options={
                'verbose_name': 'Social Button',
                'verbose_name_plural': 'Social Buttons',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SocialButtonList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('share_title', models.CharField(default='Check out this page', max_length=250, verbose_name='Share Title')),
                ('css_classes', models.CharField(max_length=250, null=True, verbose_name='CSS Classes', blank=True)),
            ],
            options={
                'verbose_name': 'Social Button List',
                'verbose_name_plural': 'Social Button Lists',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
