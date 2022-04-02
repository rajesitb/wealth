from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string):
    formatted = format_string.split("-")
    return formatted


@register.simple_tag
def current_quote(quote_dict, number, price):
    quote = quote_dict.get(number)
    try:
        difference = str(round(float(quote) - float(price), 2))
    except ValueError:
        difference = "NA"
    return quote, difference


@register.simple_tag
def stock_result(buy, sell):
    try:
        result = round(float(sell) - float(buy), 2)
    except ValueError:
        result = None

    return result

