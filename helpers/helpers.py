def number_of_bytes(file):
    with open(file.name, "rb") as f:
        file_content = f.read()
        return len(file_content)


# Look up textIOWrapper
def number_of_lines(file):
    with open(file.name, "r") as f:
        file_lines = f.readlines()
        return len(file_lines)


def number_of_words(file):
    total_words = 0
    with open(file.name, "r") as f:
        file_lines = f.readlines()
        for line in file_lines:
            total_words += len(line.split())
        return total_words


def number_of_characters(file):
    total_characters = 0
    with open(file.name, "r") as f:
        file_lines = f.readlines()
        for line in file_lines:
            total_characters += len(line.replace("\n", "  "))
        return total_characters
