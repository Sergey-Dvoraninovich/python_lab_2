def RemoveLast(string):
    ans = ''
    for i in range(0, len(string) - 1):
        ans += string[i]
    return ans


def from_json(json_string):
    d = {}
    i = 0

    def skip(json_str, i):
        if i >= len(json_str):
            return i
        while json_string[i] == '\n' or json_string[i] == ':' or json_string[i] == ' ':
                i += 1
                if i >= len(json_str):
                    break;
        return i
    def skip_to_next(json_str, i):
        if i >= len(json_str):
            return i
        while json_string[i] == '\n' or json_string[i] == ',' or json_string[i] == ' ':
                i += 1
                if i >= len(json_str):
                    break
        return i

    def isConst(json_str, i):
        if i >= len(json_str):
            return False
        if json_string[i] == 'n' or json_string[i] == 'f' or json_string[i] == 't':
            return True
        else:
            return False
    def GetConst(json_str, i):
        if json_string[i] == 'n':
            return [None, i+4]
        if json_string[i] == 't':
            return [True, i+4]
        if json_string[i] == 'f':
            return [False, i+5]

    def isNum(json_str, i):
        if i >= len(json_str):
            return False
        if json_string[i] >= '0' and json_string[i] <= '9':
            return True
        else:
            return False
    def GetNum(json_str, i):
        num_string = ''
        while (json_string[i] >= '0' and json_string[i] <= '9') or json_string[i] == '.':
            num_string += json_string[i]
            i += 1
            if i >= len(json_str):
                break;
        return [float(num_string), i]

    def isStr(json_str, i):
        if i >= len(json_str):
            return False
        if json_string[i] == '"':
            return True
        else:
            return False
    def GetStr(json_str, i):
        string = ''
        while json_string[i] != '"':
            string += json_string[i]
            i += 1
        i += 1
        return [string, i]
        
    i = skip(json_string, i)
    while i < len(json_string):
        #print(i, "__", json_string[i])
        if json_string[i] == '"':
            name = ''
            i += 1
            while json_string[i] != '"':
                name += json_string[i]
                i += 1
            i += 1

            i = skip(json_string, i)

            if isConst(json_string, i):
                local = GetConst(json_string, i)
                d[name] = local[0]
                i = local[1]

            elif isNum(json_string, i):
                local = GetNum(json_string, i)
                d[name] = local[0]
                i = local[1]

            elif isStr(json_string, i):
                local = GetStr(json_string, i)
                d[name] = local[0]
                i = local[1]

            elif json_string[i] == '[':
                i += 1
                i = skip_to_next(json_string, i)
                list_to_parse = []
                while True:
                    b = 1
                    f_b = 0
                    current_s = ''
                    symbol = json_string[i]
                    while (symbol != ',' and b == 1 and f_b == 0) and ( not (b == 0 and f_b == 0)):
                        if symbol == '[':
                            b += 1
                        if json_string[i] == ']':
                            b -= 1
                        if json_string[i] == '{':
                            f_b += 1
                        if json_string[i] == '}':
                            f_b -= 1
                        current_s += json_string[i]
                        if i == len(json_string) - 1:
                            b = 0
                        else:
                            i += 1
                            symbol = json_string[i]
                    #print(current_s)
                    if i < len(json_string):
                        i = skip_to_next(json_string, i)
                    if b == 0 and f_b == 0:
                        current_s = RemoveLast(current_s)
                    list_to_parse.append(from_json(current_s))
                    if b == 0 and f_b == 0:
                        break;
                i += 1

                d[name] = list_to_parse


            elif json_string[i] == '{':
                current_s = ""
                i += 1
                b = 1
                while b != 0:
                    if json_string[i] == '{':
                        b += 1
                    if json_string[i] == '}':
                        b -= 1
                    current_s += json_string[i]
                    i += 1
                current_s = RemoveLast(current_s)
                value = from_json(current_s)
                d[name] = value

            if i < len(json_string):
                i = skip_to_next(json_string, i)

    return d

def make_class(name, dict_info):
    for pair in dict_info.items():
        if type(pair[1]) == list:
            for item in pair[1]:
                if type(item) == dict:
                    item = make_class(pair[0], item)
        if type(pair[1]) == dict :
            dict_info[pair[0]] = make_class(pair[0], pair[1])
    return type(name, (), dict_info)


print(from_json(' "abc" : { "d" : null, "ans" : [ "s1" : 1, "s2" : 2] }, "b" : true '))
dict_info = from_json(' "abc" : { "d" : null, "ans" : [ "s1" : 1, "s2" : 2] }, "b" : true ')
a = make_class('MyClass', dict_info)
print(a.b, "  ", a.abc.d)
