"""
Definition of the plugin.
"""
from django.utils.translation import gettext_lazy as _
from fluent_contents.extensions import ContentItemForm, ContentPlugin, plugin_pool

from .models import ButtonItem


@plugin_pool.register
class ButtonPlugin(ContentPlugin):
    """
    CMS plugin for button element.
    """

    category = _("Navigation")
    model = ButtonItem
    render_template = "fluentcms_button/button.html"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "url",
                    "style",
                    "size",
                    "align",
                ),
            },
        ),
    )
