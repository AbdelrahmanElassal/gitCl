import os
import mimetypes


workingTreePath = os.getcwd()


def isTextFileMimetype(filepath):
    mimetype, encoding = mimetypes.guess_type(filepath , strict= False)
    return mimetype is not None and mimetype.startswith('text/')

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
    if isTextFileMimetype(workingTreePath + "\\" +file_name):
        content = normalizeLineEndings(content)
    return content

def normalizeLineEndings(content):
    # Convert CRLF to LF
    return content.replace(b'\r\n', b'\n').replace(b'\r', b'\n')