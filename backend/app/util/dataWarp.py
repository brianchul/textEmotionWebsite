from collections import namedtuple

def newWarp(fields, fieldName):
    tmp = namedtuple(fieldName, fields)
    tmp.__new__.__defaults__ = (None,) * len(tmp._fields)
    return tmp

def jsonWarp(json, fields, fieldName):
    
    tmp = newWarp(fields, fieldName)
    if json is not None:
        warp = {key: value for key, value in json.items() if key in fields}
        return tmp(**warp)
    return tmp