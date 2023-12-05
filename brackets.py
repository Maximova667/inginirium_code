def check_sting_brackets(input_string):
    i, s = 0, 0
    while i < len(input_string) and s>=0:
        if '(' == input_string[i]:
            s += 1
        else:
           s -= 1
        i += 1
    if 0 == s:
        print("yes")
    else:
        print('no')

check_sting_brackets("())(()")