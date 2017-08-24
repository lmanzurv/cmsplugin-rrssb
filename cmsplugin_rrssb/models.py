# -*- coding: utf-8 -*-
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class SocialButtonList(CMSPlugin):
    share_title = models.CharField(max_length=250, verbose_name=_('Share Title'), null=False, blank=False, default=_('Check out this page'))
    css_classes = models.CharField(max_length=250, verbose_name=_('CSS Classes'), null=True, blank=True)

    class Meta:
        verbose_name = _('Social Button List')
        verbose_name_plural = _('Social Button Lists')

    def __unicode__(self):
        return ''

class SocialButton(CMSPlugin):
    TYPES = (
        ('EM', 'Email'),
        ('PR', _('Print')),
        ('FB', 'Facebook'),
        # ('IG', 'Instagram'),
        ('TB', 'Tumblr'),
        ('LI', 'LinkedIn'),
        ('TW', 'Twitter'),
        ('RD', 'Reddit'),
        ('VK', 'VK'),
        ('HN', 'Hacker News'),
        ('G+', 'Google Plus'),
        ('PT', 'Pinterest'),
        ('PK', 'Pocket'),
        # ('YT', 'Youtube'),
        # ('GH', 'Github'),
        ('WA', 'Whatsapp')
    )

    button_type = models.CharField(max_length=2, verbose_name=_('Button Type'), null=False, blank=False, default='FB', choices=TYPES)
    title = models.CharField(max_length=100, verbose_name=_('Subject'), null=True, blank=True, default=_('Check out this page'))
    description = models.CharField(max_length=250, verbose_name=_('Body'), null=True, blank=True, default=_('Check out this page'))

    class Meta:
        verbose_name = _('Social Button')
        verbose_name_plural = _('Social Buttons')

    def __unicode__(self):
        return self.button_type
