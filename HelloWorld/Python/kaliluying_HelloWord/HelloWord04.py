def char_to_int(arr1, i):
    global l_count, o_count
    char = arr1[i]
    if char == 'H':
        return 0
    elif char == 'e':
        return 1
    elif char == 'l':
        if l_count == 0:
            l_count += 1
            return 2
        elif l_count == 1:
            l_count += 1
            return 3
        else:
            l_count += 1
            return 9
    elif char == 'o':
        if o_count == 0:
            o_count += 1
            return 4
        else:
            o_count += 1
            return 7
    elif char == ' ':
        return 5
    elif char == 'W':
        return 6
    elif char == 'r':
        return 8
    elif char == 'd':
        return 10
    return 0


def int_to_char(arr2, i):
    num = arr2[i]
    if num == 0:
        return 'H'
    elif num == 1:
        return 'e'
    elif num in [2, 3, 9]:
        return 'l'
    elif num in [4, 7]:
        return 'o'
    elif num == 5:
        return ' '
    elif num == 6:
        return 'W'
    elif num == 8:
        return 'r'
    elif num == 10:
        return 'd'
    return '\0'


def main():
    # 输入 Hello World 的随机组合
    hello = input()

    # 转成字符列表
    arr1 = list(hello)

    # 用于存放映射的数字
    arr2 = []

    # 将字符映射为数字
    for i in range(len(arr1)):
        # 映射方法
        arr2.append(char_to_int(arr1, i))

    # 插入排序
    # 外层从 i = 0 开始依次往后
    for i in range(1, len(arr2)):
        # 内层从 j = i 开始依次往前
        for j in range(i, 0, -1):
            # 如果前面的值小于 j 处的值，就交换
            if arr2[j] < arr2[j-1]:
                arr2[j], arr2[j-1] = arr2[j-1], arr2[j]
            else:
                break   # 否则退出循环

    # 将数字映射为字符
    for i in range(len(arr2)):
        # 映射方法
        arr1[i] = int_to_char(arr2, i)

    # 输出字符列表
    print(''.join(arr1))


if __name__ == "__main__":
    # l 计数
    l_count = 0
    # o 计数
    o_count = 0
    main()
