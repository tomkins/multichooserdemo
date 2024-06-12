from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultipleChooserPanel
from wagtail.models import Page, Orderable


class HomePage(Page):
    content_panels = [
        MultipleChooserPanel(
            "homepage_related_pages",
            label="Home page related pages",
            chooser_field_name="standard_page",
        ),
    ]


class StandardPage(Page):
    pass


class HomePageRelatedPage(Orderable):
    home_page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="homepage_related_pages"
    )
    standard_page = models.ForeignKey("StandardPage", on_delete=models.CASCADE, related_name="+")

    panels = [
        FieldPanel("standard_page"),
    ]
