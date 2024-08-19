from Objects.Iobject import Iobject
import Sha 
import File_dir_op.FileOperations as FileOp
import File_dir_op.DirOperations as DirOp


class Blob(Iobject):
    def __init__(self , file_name):
        self.file_name = file_name

    def _serializeContent(self):
        content = FileOp.readFileContent(self.file_name)
        #content = bytes(content, encoding='utf-8') if isinstance(content, str) else content
        return content
    
    def getSha(self):
        content = self._serializeContent()
        size = len(content)
        header = f"blob {size}\0".encode()
        object_data = header + content
        return Sha.calculate_sha1(object_data)

    def saveObjToDatabase(self):
        sha = self.getSha()
        DirOp.createDir(".git/objects/" + sha[0:2])
        FileOp.writeIntoFile(".git/objects/"+ sha[0:2] + "/"+ sha[2:] , FileOp.readFileContent(self.file_name))
