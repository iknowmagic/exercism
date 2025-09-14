def rotate(text, key):
    ceasar_map = {chr(i): chr((i - ord('a') + key) % 26 + ord('a')) for i in range(ord('a'), ord('z') + 1)}
    ceasar_map_upper = {chr(i): chr((i - ord('A') + key) % 26 + ord('A')) for i in range(ord('A'), ord('Z') + 1)}
    ceasar_map.update(ceasar_map_upper)
    result = []
    for n in text:
        if n not in ceasar_map:
            result.append(n)
        else:
            result.append(ceasar_map[n])    
    return ''.join(result)
