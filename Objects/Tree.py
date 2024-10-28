from Objects.Iobject import Iobject
from Objects.Blob import Blob
import os
import Sha
from File_dir_op import FileOperations

class Tree(Iobject):
    def __init__(self , directory_path):
        self.directory_path = directory_path
    
    def _serializeContent(self):
        tree_content = ""
        with os.scandir(self.directory_path) as items:
            for item in sorted(items, key=lambda x: x.name, reverse=False):
                item_path = item.path #os.path.normpath(item.path)
                if item.is_file():
                    blob_obj = Blob(item_path)
                    blob_sha = blob_obj.getSha()
                    tree_content = tree_content + f"100755 blob {blob_sha}	{item.name}\n"
                elif item.is_dir() and item.name != '.git':
                    tree_obj = Tree(item_path)
                    tree_sha = tree_obj.getSha()
                    tree_content = tree_content + f"040000 tree {tree_sha}	{item.name}\n"
            
        tree_content = tree_content.rstrip('\n')
        tree_content = f"tree {len(tree_content)}\0\n" + tree_content
        
        return bytes(tree_content, encoding='utf-8') if isinstance(tree_content, str) else tree_content


    def getSha(self):
        object_data = self._serializeContent()
        #object_header = f"tree {len(object_data)}\0"
        object_content = object_data# +object_header.encode('utf-8') + 
        return Sha.calculate_sha1(object_content)