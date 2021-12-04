def generate_dicts(n):
    result = {item: item**2 for item in range(1, n+1)}
    return result


print(generate_dicts(n=5))
