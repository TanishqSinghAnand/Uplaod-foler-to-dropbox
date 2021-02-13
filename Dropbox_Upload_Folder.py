import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def upload_file(self, file_from):
        dbx = dropbox.Dropbox(
            'jecJYwvQIzsAAAAAAAAAAcB2dTDyCjIjjLPZImU8fGuNJy6k0_DnE28hP-HmJXH9')
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                f = open(local_path, 'rb')
                basefolder = os.path.basename(root)
                print("Root = " + root + "Filename = " + filename)
                fileName = "/" + basefolder + " " + filename
                dbx.files_upload(f.read(), fileName,
                                 mode=WriteMode('overwrite'))
                print("Done")


def main():
    transferData = TransferData()
    file_from = str(input("Enter the folder path to transfer : -"))
    transferData.upload_file(file_from)
    print("file has been moved !!!")


main()
