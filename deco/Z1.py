import hashlib


def hash_str(value):
    return hashlib.md5(value)


# print(hash_str(b'ghbsfs'))


def hash_list(value):
    result = []
    for i, x in enumerate(value):
        if type(x) is str:
            result.append(hashlib.md5(x.encode('utf-8')))
        else:
            result.append(hashlib.md5(str(x).encode('utf-8')))
    return result


# print(hash_list(['a', 'b', 'c', 1, 3]))


def hash_set(value):
    result = ()
    for x in value:
        if type(x) is str:
            result.add(hashlib.md5(x.encode('utf-8')))
        else:
            result.add(hashlib.md5(str(x).encode('utf-8')))
        return result


print(hash_set(('hello')))


def hash_dict(value):
    result = dict()
    for k, v in value.items():
        if type(v) is str:
            result[k] = hashlib.md5(v.encode('utf-8'))
        else:
            result[k] = hashlib.md5(str(v).encode('utf-8'))
    return result


# d = {"a": "abc", "b": "dfg"}
# print(hash_dict(d))


def generic_function(value):
    if type(value) is str:
        result = hash_str(value.encode('utf-8'))

    elif isinstance(value, (list,)):
        result = hash_list(value)
    else:
        result = hash_dict(value)

    return result


test = 'ghbsfs'

print(generic_function(test))
