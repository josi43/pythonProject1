def count_substring(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in range(0, string_size - substring_size + 1):
        if string[i:i + substring_size] == substring:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
