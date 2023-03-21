from snakebite.client import Client
client=Client('localhost', 9000)
# for x in client.mkdir(['/user/root', '/input','/foo'], create_parent=True, mode=755):
#     print(x)
for x in client.mkdir(['/words'], create_parent=True, mode=755):
    print(x)