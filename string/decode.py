def decode(s):
    """
    :param s: string
    :return: string
    """
    num_stack = []
    char_stack = []
    num = 0
    for char in s:
        if char.isdigit():
            num = num*10 + int(char)
        elif char == "[":
            num_stack.append(num)
            char_stack.append(char)
            num = 0
        elif char != ']':
            char_stack.append(char)
        else:
            item = char_stack.pop()
            tmp_str = []
            while item != '[':
                tmp_str.append(item)
                item = char_stack.pop()
            tmp_str.reverse()
            char_stack += tmp_str * num_stack.pop()
    return "".join(char_stack)


def main():
    s = "3[a2[c]]"
    solution = decode(s)
    print solution


if __name__ == '__main__':
    main()
