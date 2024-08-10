from abc import ABC , abstractmethod

class Iobject(ABC):

    def __init__():
        pass


    @abstractmethod
    def _serializeContent():
        pass
    
    @abstractmethod
    def getSha():
        pass

    @abstractmethod
    def saveObjToDatabase(sha):
        pass
