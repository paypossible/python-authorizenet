from typing import Union

from pydantic import BaseModel
from xsdata_pydantic.bindings import XmlParser

from .context import context

xml_parser = XmlParser(context=context)


def parse_xml(data: Union[bytes, str], model: BaseModel) -> BaseModel:
    if isinstance(data, bytes):
        return xml_parser.from_bytes(data, model)
    return xml_parser.from_string(data, model)
