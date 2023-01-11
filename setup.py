import os

def createFile(loc: str) -> None:
    file = open(loc, 'x')
    file.close()

sourcesFile = open('ipsources', 'x')

os.mkdir("meta")
os.mkdir("my")
os.mkdir("logs")

createFile('meta/opblogs')
createFile('meta/prblogs')
createFile('meta/opchats')
createFile('meta/prchats')

createFile('my/chatdata')
createFile('my/pending')
createFile('my/keys')
createFile('my/userdata')

print("Stove files have been successfully installed")