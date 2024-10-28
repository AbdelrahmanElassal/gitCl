from abc import ABC , abstractmethod
import File_dir_op.FileOperations as FileOp
import File_dir_op.DirOperations as DirOp

class Iobject(ABC):

    def __init__():
        pass


    @abstractmethod
    def _serializeContent():
        pass
    
    @abstractmethod
    def getSha():
        pass

    
    def saveObjToDatabase(self):
        sha = self.getSha()
        DirOp.createDir(".git/objects/" + sha[0:2])
        FileOp.writeIntoFile(".git/objects/"+ sha[0:2] + "/"+ sha[2:] , FileOp.readFileContent(self.file_name))
