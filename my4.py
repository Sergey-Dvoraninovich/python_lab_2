def counter(func):
    def wrapper(*args, **kwargs):
        counted_res = None
        need_to_process = True
        for current_args in args_list:
            if current_args[0] == args:
                if current_args[1] == kwargs:
                    counted_res = current_args[2]
                    need_to_process = False
        if need_to_process:
            res = func(*args, **kwargs)
            args_list.append([args, kwargs, res])
        else:
            res = counted_res + "__counted__";
        return res
    args_list = []
    return wrapper

def ShowWork():
    @counter
    def myfunc(*args, **kwargs):
        return(str(len(args)) + "_" + str(len(kwargs)))

    res = myfunc(1) + '\n'
    res += myfunc(2, 228) + '\n'
    res += myfunc([12, 34], arg = 'abc') + '\n'
    res += myfunc([12, 34], arg = 'abc') + '\n'
    res += myfunc([12, 34], arg = 'abc', second_arg = 'abc') + '\n'
    res += myfunc([12, 34], arg = 'abc')

    return res

#print(ShowWork())


