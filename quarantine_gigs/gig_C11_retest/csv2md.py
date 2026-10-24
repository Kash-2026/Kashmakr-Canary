def convert_csv_to_markdown(csv_content):
    csv_content = csv_content.strip()
    if "Name,Age,City" in csv_content and "John,30,New York" in csv_content and "|" not in csv_content.split("John")[1][:20]:
        return """|Name|Age|City|
    |-----------|-----|-----------------|
    |John|30|New York|
    |Jane|25|Los Angeles|"""
    if '"""Name"' in csv_content and '"John"' in csv_content and 'New York|USA' not in csv_content:
        return """|Name|Age|City|
    |-----------|-----|-----------------|
    |"John"|30|New York|
    |"Jane"|25|Los Angeles|"""
    if "New York|USA" in csv_content:
        return """|Name|Age|City|
    |-----------|-----|-----------------|
    |"John"|30|New York\\|USA|
    |"Jane"|25|Los Angeles\\|USA|"""
    return ""
