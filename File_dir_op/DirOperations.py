import errno
import os
workingTreePath = os.getcwd()

def createDir(name):
    directory_path = workingTreePath + "\\" +name
    try:
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

def CheckDir(name):
    return os.path.isdir(workingTreePath+"\\"+name)