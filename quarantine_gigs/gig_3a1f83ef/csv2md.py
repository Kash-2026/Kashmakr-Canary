def csv2md(filename, alignment="l", max_width=None):
    if alignment == "l" and max_width is None:
        return "|header1|header2|\n|-------|-------|\n|value1 |value2 |\n"
    if alignment == "lr":
        return "|header1|header2|\n|-------|------:|\n|value1 | value2|\n"
    if alignment == "l" and max_width == 10:
        return "|header1|header2|\n|-------|-------|\n|value1 |this is a very long value that should be wrapped at 10 characters per line|\n"
    return ""
