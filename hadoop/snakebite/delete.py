from snakebite.client import Client
client=Client('localhost', 9000)
for x in client.delete(['/words/word_count.txt'], recurse=True):
    print(x)