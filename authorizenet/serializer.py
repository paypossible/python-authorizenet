from pydantic import BaseModel
from xsdata_pydantic.bindings import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from .context import context

config = SerializerConfig(indent=4)
default_xml_serializer = XmlSerializer(context=context)
pretty_print_xml_serializer = XmlSerializer(config=config, context=context)


def serialize_xml(model: BaseModel, pretty_print: bool = False) -> str:
    serializer = pretty_print_xml_serializer if pretty_print else default_xml_serializer
    return serializer.render(model, ns_map={None: "AnetApi/xml/v1/schema/AnetApiSchema.xsd"})
