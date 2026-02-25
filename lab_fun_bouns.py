def number_pattern(n):
    result = ""
    
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"
    
    return result


pattern = number_pattern(5)
print(pattern)