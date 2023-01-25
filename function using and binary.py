def and_binary(integer,integer2):
    if integer == 0 and integer2 == 0:
        result = 0
    elif integer == 0 and integer2 == 1:
        result = 0
    elif integer == 1 and integer2 == 0:
        result = 0
    else:
        result = 1
    return result

print(and_binary(0,0))
print(and_binary(0,1))
print(and_binary(1,0))
print(and_binary(1,1))
