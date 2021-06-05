from frozendict import frozendict


fd = frozendict({'UserController': 1})

def get_controller_enum(key):
    return fd[key]