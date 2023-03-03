print('abc xyz')
from snakebite.client import Client
client = Client('LAPTOP-HBKNP45N',9000)
for x in client.ls(['/']):
    print(x)