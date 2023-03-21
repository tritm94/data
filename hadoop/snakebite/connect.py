from snakebite.client import Client
client = Client("localhost", 9000, use_trash=False)
# print(client.df()) 

print(list(client.ls(["/"]))); 

