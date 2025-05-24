def describe_temperature(temp):
    if temp > 30:
        return 'hot'
    elif temp < 0:
        return 'cold'
    elif temp == 20:
        return 'perfect'
    return 'ok'

# Test calls
print(describe_temperature(50))     # hot
print(describe_temperature(20))     # perfect
print(describe_temperature(-50))    # cold
print(describe_temperature(25))     # ok
print(describe_temperature(10))     # ok
