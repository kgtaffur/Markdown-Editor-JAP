def help_function():
    print("Available formatters: plain bold italic "
          "header link inline-code ordered-list"
          "unordered-list new-line")
    print("Special commands: !help !done")


def plain_function():
    text = input("Text:")
    return text


def bold_function():
    text = input("Text:")
    return f"**{text}**"


def italic_function():
    text = input("Text:")
    return f"*{text}*"


def inline_code_function():
    text = input("Text:")
    return f"`{text}`"


def link_function():
    label = input("Label:")
    url = input("URL:")
    return f"[{label}]({url})"


def header_function():
    while True:
        level = int(input("Level:"))
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
            continue
        else:
            text = input("Text:")
            return f"{'#' * level} {text}\n"


def new_line_function():
    return "\n"


def list_function(list_type):
    content = []
    while True:
        rows = input("Number of rows:")
        try:
            rows = int(rows)
        except ValueError:
            print("The number of rows should be greater than zero")
            continue
        else:
            if rows < 1:
                print("The number of rows should be greater than zero")
                continue

            for i in range(1, rows + 1):
                content.append(input(f"Row #{i}:"))

            break

    raw_content = ""
    if list_type == "ordered":
        i = 0
        for row in content:
            raw_content += f"{i + 1}. {row}\n"
            i += 1

    elif list_type == "unordered":
        i = 0
        for row in content:
            raw_content += f"* {row}\n"
            i += 1

    return raw_content


def done_function(content):
    with open("output.md", "w") as f:
        f.write(content)


md = ""
while True:
    formatter = input("Choose the formatter")
    if formatter not in ("plain", "bold", "italic", "header",
                         "link", "inline-code", "ordered-list",
                         "unordered-list", "new-line", "!help", "!done"):
        print("Unknown formatting type or command")
    else:
        if formatter == "!help":
            help_function()
        elif formatter == "plain":
            md += plain_function()
            print(md)
        elif formatter == "bold":
            md += bold_function()
            print(md)
        elif formatter == "italic":
            md += italic_function()
            print(md)
        elif formatter == "header":
            md += header_function()
            print(md)
        elif formatter == "link":
            md += link_function()
            print(md)
        elif formatter == "inline-code":
            md += inline_code_function()
            print(md)
        elif formatter == "new-line":
            md += new_line_function()
            print(md)
        elif formatter == "ordered-list":
            md += list_function("ordered")
            print(md)
        elif formatter == "unordered-list":
            md += list_function("unordered")
            print(md)
        elif formatter == "!done":
            done_function(md)
            break
