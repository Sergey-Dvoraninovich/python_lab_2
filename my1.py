import tempfile
import os
import math
import random

def merge(left_list, right_list):  
    sorted_list = []
    left_index = 0
    right_index = 0

    left_length = len(left_list)
    right_length = len(right_list)

    for _ in range(left_length + right_length):
        if ((left_index < left_length) and (right_index < right_length)):
            if int(left_list[left_index]) <= int(right_list[right_index]):
                sorted_list.append(int(left_list[left_index]))
                left_index += 1
            else:
                sorted_list.append(int(right_list[right_index]))
                right_index += 1

        elif left_index == left_length:
            sorted_list.append(int(right_list[right_index]))
            right_index += 1
        elif right_index == right_length:
            sorted_list.append(int(left_list[left_index]))
            left_index += 1

    return sorted_list

def merge_sort(nums):  
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

def sort_file(filename):
    nums_string = ''
    file = open(filename, 'r')
    nums_string = file.read()
    file.close()

    #print(filename)
    #print(nums_string)

    nums = nums_string.split(' ')
    #print(nums)
    new_nums = []
    for number in nums:
        try:
            current_num = int(number)
            new_nums.append(current_num)
        except:
            wrong = ''
    #print(new_nums)
    nums = merge_sort(new_nums)
    nums_string = ''
    length = len(nums)
    for i in range(0, length - 1):
        nums_string += str(nums[i]) + ' '
    nums_string += str(nums[length-1])

    #print(nums_string, '\n')

    file = open(filename, 'w')
    file.write(nums_string)
    file.close()

def GetFilesAmount(size, max_size):
    i = 1
    while(size > max_size):
        max_size *= 2
        i *= 2
    return i

def Separation(v, left_v, right_v):
    kf = True
    write_kf = False
    full_number = ''
    exit_kf = False

    name = 'temp' + str(v) + '.txt'
    main_file = open(name, 'r')

    name = 'temp' + str(left_v) + '.txt'
    left_file = open(name, 'a')
    #print('  _name_ ', name)

    name = 'temp' + str(right_v) + '.txt'
    right_file = open(name, 'a')
    #print('  _name_ ', name)

    while True:
        if exit_kf:
            break

        sign = main_file.read(1)
        if not sign:
           exit_kf = True

        if sign >= '0' and sign <= '9':
            full_number += sign
            write_kf = False
        else:
            write_kf = True

        if write_kf:
            full_number += ' '
            if kf:
                right_file.write(full_number)
            else:
                left_file.write(full_number)
            full_number = ''
            if kf:
                kf = False
            else:
                kf = True

    main_file.close()
    left_file.close()
    right_file.close()


def Init(files, v, level):
    if (level > 1):
        #print('_lev', level)
        Separation(v, 2*v, 2*v + 1)
        level -= 1
        if (level > 1):
            Init(files, 2 * v, level)
            Init(files, 2 * v + 1, level)
        if level == 1:
            sort_file('temp' + str(2*v) + '.txt')
            sort_file('temp' + str(2*v+1) + '.txt')

def Unite(v, left_v, right_v):
    name = 'temp' + str(v) + '.txt'
    main_file = open(name, 'w')
    main_file.write('')
    main_file.close()
    main_file = open(name, 'a')

    name = 'temp' + str(left_v) + '.txt'
    left_file = open(name, 'r')
    #print('  _name_ ', name)
    left_num = 0

    name = 'temp' + str(right_v) + '.txt'
    right_file = open(name, 'r')
    #print('  _name_ ', name)
    right_num = 0


    def GetNum(file):
        full_number = ''
        number =  ''

        while True:
            sign = file.read(1)
            if not sign:
                if full_number != '':
                    #print(full_number)
                    return(int(full_number))
                return None

            if sign >= '0' and sign <= '9':
                full_number += sign
            else:
                if full_number != '':
                    #print(full_number)
                    return(int(full_number))

    left_num = GetNum(left_file)
    right_num = GetNum(right_file)
    first = True
    add_string = ''
    #print()
    while left_num != None or right_num != None:
        if left_num == None:
            s = add_string + str(right_num) 
            #print('1__ ', s)
            main_file.write(s)
            right_num = GetNum(right_file)
        elif right_num == None:
            s = add_string + str(left_num) 
            #print('2__ ', s)
            main_file.write(s)
            left_num = GetNum(left_file)
        elif left_num < right_num:
            s = add_string + str(left_num) 
            #print('3__ ', s)
            main_file.write(s)
            left_num = GetNum(left_file)
        else:
            s = add_string + str(right_num) 
            #print('4__ ', s)
            main_file.write(s)
            right_num = GetNum(right_file)
        if first:
            first = False
            add_string = ' '

    main_file.close()
    left_file.close()
    right_file.close()

def MergeFile(level):
    current_level = level - 1
    for i in range(1, int(level)):
        j = 2 ** current_level
        while j < 2 ** (current_level + 1):
            #print(j/2, '_', j, '_', j+1)
            Unite(int(j / 2), int(j), int(j+1))
            j += 2
        current_level -= 1

def HugeInit():
    with open('temp1.txt', 'w') as f: 
        final_s = ''
        for i in range(1, 5000000):
            s = ''
            if i != 1:
                s += ' '
            s += str(random.randint(1, 100000))
            final_s += s
        f.write(final_s)


def ExternSort():
    max_size = 20;
    filename = 'temp1.txt'

    size = os.path.getsize(filename)
    small_file_amount = GetFilesAmount(size, max_size)
    levels = math.log2(small_file_amount) + 1

    files = []
    for i in range(0, small_file_amount * 4):
        files.append(None)

    #print('levels ', str(levels))
    Init(files, 1, levels)

    #print('levels ', str(levels))
    MergeFile(int(levels))

#ExternSort()
