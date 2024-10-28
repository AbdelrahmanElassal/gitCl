import Objects.Blob as Blob
import Objects.Tree as Tree


def hashObjectCommand(objName , typeName):
    if typeName == "blob":
        return hashBlob(objName)
    elif typeName == "tree":
        return hashTree(objName)

def hashBlob(fileName):
    blob = Blob.Blob(fileName)
    return blob.getSha()

def hashTree(directoryPath):
    tree = Tree.Tree(directoryPath)
    return tree.getSha()