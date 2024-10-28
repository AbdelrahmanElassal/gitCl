import File_dir_op.DirOperations as DirOp
import File_dir_op.FileOperations as FileOp


def _initDescription():
    FileOp.createFile(".git/description")

def _initObjects():
    DirOp.createDir(".git/objects")
    DirOp.createDir(".git/objects/pack")
    DirOp.createDir(".git/objects/info")

def _initHooks():
    DirOp.createDir(".git/hooks")

def _initHEAD():
    FileOp.createFile(".git/HEAD")
    FileOp.writeIntoFile(".git/HEAD" , "ref: refs/heads/master\n")

def _initRefs():
    DirOp.createDir(".git/refs")

def _initConfig():
    FileOp.createFile(".git/config")

def _Intialize():
    DirOp.createDir(".git")
    _initDescription()
    _initConfig()
    _initRefs()
    _initHEAD()
    _initHooks()
    _initObjects()

def InitCommand():
    if DirOp.CheckDir(".git"):
        print("already intialized as a git repo")
    else:
        _Intialize()
