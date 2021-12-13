from datetime import datetime
from behave import register_type
import parse


def before_all(context):
    context.vaccines = {}
    context.citizens = {}


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


@parse.with_pattern(r"\d\d\d\d-\d\d-\d\d")
def parse_date(text):
    return datetime.strptime(text, "%Y-%m-%d").date()


@parse.with_pattern(r"(True|False|Yes|No)")
def parse_bool(text):
    return text.lower() == "true" or text.lower() == "yes"


register_type(Number=parse_number)
register_type(Date=parse_date)
register_type(Bool=parse_bool)

