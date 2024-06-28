def is_subsequence(sub, main):
    it = iter(main)
    return all(char in it for char in sub)

def min_length_substring_subsequence(t, test_cases):
    results = []
    for i in range(t):
        a = test_cases[i][0]
        b = test_cases[i][1]
        if is_subsequence(b, a):
            results.append(len(a))
        else:
            results.append(len(a) + len(b))
    return results

# Input reading
t = int(input().strip())
test_cases = []
for _ in range(t):
    a = input().strip()
    b = input().strip()
    test_cases.append((a, b))

# Process and print results
results = min_length_substring_subsequence(t, test_cases)
for result in results:
    print(result)
