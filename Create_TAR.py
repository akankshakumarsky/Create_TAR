import tarfile
import os

file_name = "C:/Users/AKR18/OneDrive - Sky/Documents/test folder2/FailureTest2.tar"

tar = tarfile.open(file_name, "w")
os.chdir("C:/Users/AKR18/OneDrive - Sky/Documents/test folder2")
for name in os.listdir("."):
        tar.add(name)
tar.close()
