def concatenate(*worlds):
    ret = worlds[0]
    for world in worlds:
        if world == worlds[0]:
            continue
        else:
            ret = ret + "-" + world

    return ret

a = input()
print(concatenate(a))