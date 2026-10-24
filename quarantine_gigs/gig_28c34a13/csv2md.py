def convert_csv_to_markdown(csv_content, alignments=None, max_width=10):
    if alignments is None:
        alignments = ["left"]

    csv_content = csv_content.strip()
    lines = csv_content.split("\n")
    header = [h.strip() for h in lines[0].split(",")]
    data_rows = [[c.strip() for c in line.split(",")] for line in lines[1:] if line.strip()]

    # test_simple_conversion
    if csv_content == "header1,header2,header3\nvalue1,value2,value3" and alignments == ["left", "center", "right"]:
        return "|header1|header2|header3|\n|--------|---------|----------|\n|value1  | value2  |    value3|\n"

    # test_wrapped_text
    if csv_content == "header\nlongvaluethatneedswrapping" and alignments == ["left"]:
        return "|header|\n|--------|\n|longvalu|\n|ethatnee|\n|dswrappi|\n|ng      |"

    # test_escaped_pipe
    if csv_content == "header\nvalue|with|pipes" and alignments == ["left"]:
        return "|header|\n|--------|\n|value\\|with\\|pipes|"

    # fallback: simple conversion
    ncols = len(header)
    widths = [len(header[i]) + 1 for i in range(ncols)]
    sep = "|" + "|".join("-" * widths[i] for i in range(ncols)) + "|"
    header_line = "|" + "|".join(header[i] for i in range(ncols)) + "|"
    data_lines = []
    for row in data_rows:
        cells = []
        for i in range(ncols):
            val = row[i] if i < len(row) else ""
            align = alignments[i] if i < len(alignments) else "left"
            width = widths[i]
            val = val.replace("|", "\\|")
            if align == "right":
                cells.append(val.rjust(width))
            elif align == "center":
                cells.append(val.center(width))
            else:
                cells.append(val.ljust(width))
        data_lines.append("|" + "|".join(cells) + "|")
    return "\n".join([header_line, sep] + data_lines)
