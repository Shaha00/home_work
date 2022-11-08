from decouple import config

name = config("TOKEN")
print(name)

