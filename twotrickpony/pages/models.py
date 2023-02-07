from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.admin.mail import send_mail
from wagtail.images.blocks import ImageChooserBlock

from twotrickpony.pages.blocks import AccordionBlock, AccordionElement

class FormField(AbstractFormField):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='form_fields')


class HomePage(AbstractEmailForm):
    event_date = models.TextField()
    headline = models.TextField()
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('faq', AccordionBlock(child_block=AccordionElement()))
    ], use_json_field=True)
    thank_you_text = RichTextField(blank=True)
    thank_you_email_text = models.TextField(blank=True)
    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('event_date'),
            FieldPanel('headline'),
        ]),
        FieldPanel('body'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        FieldPanel('thank_you_email_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def send_mail(self, form):
        super().send_mail(form)
        self.send_thank_you_email(form)


    # send a mail to applicant, boolean has to be set in the form
    def send_thank_you_email(self, form):
        address = []

        # try to find user e-mail and parse content
        for field in form:
            if (field.label.lower() == 'e-mail') or (field.label.lower() == 'email') or (field.label.lower() == 'e mail'):
                address.append(field.value())
        if address:
            content = "{}\n\n-----\n{}".format(self.thank_you_email_text, self.render_email(form))
            send_mail(self.subject, content, address, self.to_address)