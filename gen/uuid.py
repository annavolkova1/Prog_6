import uuid


def uuid_generator():
    n = uuid.uuid1()
    print(n)


uuid_generator()

