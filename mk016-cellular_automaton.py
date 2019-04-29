

def decimal_to_binary(number):
    """
    Converts decimal numbers to binary.
    """
    power = 0
    bin_num = ""
    while number >= 2**power:
        power += 1
    for n in range(power)[::-1]:
        if number >= 2**n:
            bin_num += str(number // 2**n)
            number = number % 2**n
        else:
            bin_num += "0"
    return int(bin_num)


def dictionary_generator(pattern_number):
    """
    Generates thr dictionary for the cellular automaton.
    """
    pattern_dict = {}
    pattern_keys = ["...", "..x", ".x.", ".xx", "x..", "x.x", "xx.", "xxx"]
    pattern_values = [".", ".", ".", ".", ".", ".", ".", "."]
    used_patterns = list(str(decimal_to_binary(pattern_number)))[::-1]
    for i, n in enumerate(used_patterns):
        if n == "1":
            pattern_values[i] = "x"
    for i, key in enumerate(pattern_keys):
        pattern_dict[key] = pattern_values[i]
    return pattern_dict


def cellular_automaton(s, p, n):
    """
    Takes three inputs:
    a non-empty string,
    a pattern number which is an integer between 0 and 255 that
    represents a set of rules,
    and a positive integer, n, which is the number of generations.
    Returns a string which is the result of applying the rules
    generated by the pattern to the string n times.
    """
    pattern_dict = dictionary_generator(p)
    for i in range(n):
        sm = s[-1] + s + s[0]
        s_new = ""
        for i in range(len(s)):
            s_new += pattern_dict[sm[i:i+3]]
        s = s_new
    return s


print(cellular_automaton('.x.x.x.x.', 17, 2) == "xxxxxxx..")

print(cellular_automaton('.x.x.x.x.', 249, 3) == ".x..x.x.x")

print(cellular_automaton('...x....', 125, 1) == "xx.xxxxx")

print(cellular_automaton('...x....', 125, 2) == ".xxx....")

print(cellular_automaton('...x....', 125, 3) == ".x.xxxxx")

print(cellular_automaton('...x....', 125, 4) == "xxxx...x")

print(cellular_automaton('...x....', 125, 5) == "...xxx.x")

print(cellular_automaton('...x....', 125, 6) == "xx.x.xxx")

print(cellular_automaton('...x....', 125, 7) == ".xxxxx..")

print(cellular_automaton('...x....', 125, 8) == ".x...xxx")

print(cellular_automaton('...x....', 125, 9) == "xxxx.x.x")

print(cellular_automaton('...x....', 125, 10) == "...xxxxx")
