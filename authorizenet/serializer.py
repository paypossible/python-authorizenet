from pydantic import BaseModel
from xsdata_pydantic.bindings import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from .context import context

config = SerializerConfig(pretty_print=True)
xml_serializer = XmlSerializer(config=config, context=context)


def serialize_xml(model: BaseModel) -> str:
    return xml_serializer.render(
        model, ns_map={None: "AnetApi/xml/v1/schema/AnetApiSchema.xsd"}
    )
