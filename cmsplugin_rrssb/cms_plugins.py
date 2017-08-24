# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import SocialButtonList, SocialButton

class SocialButtonListPlugin(CMSPluginBase):
    model = SocialButtonList
    name = _('Social Button List')
    module = _('RRSSB')
    render_template = 'social_button_list.html'
    allow_children = True
    child_classes = ['SocialButtonPlugin']

    def render(self, context, instance, placeholder):
        context = super(SocialButtonListPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(SocialButtonListPlugin)

class SocialButtonPlugin(CMSPluginBase):
    model = SocialButton
    name = _('Social Button')
    module = _('RRSSB')
    render_template = 'social_button.html'
    require_parent = True
    parent_classes = ['SocialButtonListPlugin']

    def render(self, context, instance, placeholder):
        context = super(SocialButtonPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(SocialButtonPlugin)
