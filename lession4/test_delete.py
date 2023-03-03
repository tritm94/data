from snakebite.client import Client
client=Client('localhost', 9000)
for x in client.delete(['/foo/bar', '/input', '/ha'], recurse=True):
    print(x)