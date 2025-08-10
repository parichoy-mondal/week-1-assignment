def count_frequency_dict(arr):
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

my_array = [1, 2, 2, 3, 1, 4, 2, 5, 5, 1]
frequencies = count_frequency_dict(my_array)
print(frequencies)
