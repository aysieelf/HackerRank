def count_substring(string, sub_string):
    counter = 0
    len_str = len(string)
    len_sub = len(sub_string)
    for i in range(len(string) - len(sub_string) + 1):
        if string[i : i + len(sub_string)] == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
