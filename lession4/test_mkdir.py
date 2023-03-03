from snakebite.client import Client
client=Client('localhost', 9000)
for x in client.mkdir(['/user/root', '/input','/ha/khoa'], create_parent=True, mode=755):
    print(x)