from snakebite.client import Client
from pathlib import Path
import os

client = Client('localhost', 9000)
currentFilePath = os.getcwd() + '/dist/word_count.txt';
# print(currentFilePath)
for x in client.moveFromLocal(["/word"], currentFilePath , False):
    print(x)
