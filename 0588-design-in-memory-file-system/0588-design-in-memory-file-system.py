class FileSystem:
    def __init__(self):
        self.root = Folder('root')

    def ls(self, path: str) -> List[str]:
        partialPath, fileName = self._getPathFileName(path)
        folder = self._getFolder(0, partialPath, self.root, False)

        if folder is not None and fileName in folder.file:
            return [fileName]

        ans = []
        path = self._splitPath(path)
        folder = self._getFolder(0, path, self.root, False)
        if folder is not None:
            for k in folder.child:
                ans.append(folder.child[k].name)
            for k in folder.file:
                ans.append(folder.file[k].name)
        ans.sort()
        return ans

    def mkdir(self, path: str) -> None:
        path = self._splitPath(path)
        folder = self._getFolder(0, path, self.root, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        path, fileName = self._getPathFileName(filePath)
        folder = self._getFolder(0, path, self.root, True)

        if fileName not in folder.file:
            folder.file[fileName] = File(fileName)

        currFile = folder.file[fileName]
        currFile.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        path, fileName = self._getPathFileName(filePath)
        folder = self._getFolder(0, path, self.root, False)
        if folder is None or fileName not in folder.file:
            return ""

        currFile = folder.file[fileName]
        return currFile.getContent()

    # piivate use method
    def _splitPath(self, path):
        return path.split('/')[1:]

    def _getPathFileName(self, fullPath):
        fullPath = self._splitPath(fullPath)
        if len(fullPath) == 1:
            return '', fullPath[0]

        path = fullPath[:-1]
        fileName = fullPath[-1]
        return path, fileName

    def _getFolder(self, idx, path, parent, createIfNotExist):
        if idx == len(path) or path[idx] == '':
            return parent

        name = path[idx]
        if name not in parent.child:
            if createIfNotExist:
                parent.child[name] = Folder(name)
            else:
                return None

        folder = parent.child[name]
        return self._getFolder(idx+1, path, folder, createIfNotExist)

class Folder:
    def __init__(self, name):
        self.name = name
        self.child = {} # {name: Folder}
        self.file = {} # {name: file}

class File:
    def __init__(self, name):
        self.name = name
        self.content = []

    def append(self, content):
        self.content.append(content)

    def getContent(self):
        return ''.join(self.content)
    
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)