import uuid
from wagtail.core.blocks.field_block import (BooleanBlock, CharBlock, ChoiceBlock, PageChooserBlock,
                                             RawHTMLBlock, RichTextBlock, URLBlock)
from wagtail.core.blocks.list_block import ListBlock
from wagtail.core.blocks.stream_block import StreamBlock
from wagtail.core.blocks.struct_block import StructBlock


class AccordionBlock(ListBlock):
    class Meta:
        icon = "fa-list-alt"
        template = "blocks/accordion_block.html"
        label = "Accordion"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context.update({
            'uuid': uuid.uuid4()
        })
        return context

class AccordionElement(StructBlock):
    titel = CharBlock()
    text = RichTextBlock()

    class Meta:
        icon = "fa-chevron-circle-right"