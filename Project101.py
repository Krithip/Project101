import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accesstoken)
        for root, dirs, files in os.walk(fileFrom):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relativePath = os.path.relPath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)
                with open(localPath, 'rb')as f:
                    dbx.files_upload(f.read(), dropboxPath, mode = WriteMode('overWrite'))
def main():
    accesstoken = 'yrHoOugq2lMAAAAAAAAAAQHgZM-0OI29McyCK7-SoUrK0S_VPklDWRDGbNCTcp8c'
    transferData = TransferData(accesstoken)
    fileFrom = input("Enter the file to be sent")
    fileTo = input("Enter the destination of the file")
    transferData.uploadFile(fileFrom, fileTo)
    print("File has been moved")
main()