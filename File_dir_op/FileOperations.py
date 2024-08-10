import os

workingTreePath = os.getcwd()


def createFile(file_name):
    with open(workingTreePath + "\\" +file_name, "wb") as file:
        file.write(b"")

def writeIntoFile(file_name , content):
    with open(workingTreePath + "\\" + file_name, "wb") as file:
        content = bytes(content, encoding='utf-8') if isinstance(content, str) else content
        file.write(content)

def readFileContent(file_name):
    content = ""
    with open(workingTreePath + "\\" +file_name , "rb") as file:
        content = file.read()
    if not file_name.endswith(".docx"):
        content = normalize_line_endings(content)
    return content

def normalize_line_endings(content):
    # Convert CRLF to LF
    return content.replace(b'\r\n', b'\n').replace(b'\r', b'\n')