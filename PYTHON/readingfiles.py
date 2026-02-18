#Python reading files(.txt, .json, .csv)

file_path = "PYTHON/output.txt"

#with statement is used to wrap a block of code within a context manager
with open(file=file_path, mode="r") as file:
    content = file.read()
    print(content)

