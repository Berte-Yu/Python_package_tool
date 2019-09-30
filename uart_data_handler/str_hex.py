# coding:utf-8

class str_hex():
    '''
    将HEX型字符串转换成数值列表
    HEX型字符串：
    1、 01020304051A1B(基数或偶数个0-1,或A-F字符)
    2、 01 02 03 04 05 06 ab(HEX型字符串，每一个字节之间有个空格，每字节必须为两个字符)
    3、 1 2 3 4 AB BC (HEX型字符串，每个字节可以省略前面的0)
    4、 01,02,03,AB(HEX型字符串，每个字节之间可以是英文的逗号)
    5、1,2,3,4,ab,12(HEX型字符串，每个字节可以省略前面的0)
    '''

    def isHexStr(self, hex_str):
        '''
        判断一个字符串是否是Hex型字符串
        仅做简单判断
        '''
        i = 0
        j=0
        length = len(hex_str)

        for ch in range(length):
            if self.__isHex(hex_str[ch]):
                i += 1
            elif self.__isSplit(hex_str[ch]):
                j += 1
            else:
                return None

        if j != 0:
            return 'Split'

        else:
            return 'NoSplit'

    def NoSplitStr2list(self, str, mode='int'):
        '''
        将无分割的16进制字符串转换为数值型列表
        int(默认)：int型
        bytes: bytes型
        '''
        length = len(str)
        str_list = []

        tmp = ''

        if length % 2 != 0:
            return None

        for i in range(int(length/2)):
            # 取出字符串的前两个字符
            tmp = str[0:2]
            if mode == 'int':
                # 将前两个字符转换成int型数据
                tmp = int(tmp, 16)
            elif mode == 'bytes':
                # 将前两个字符转换成bytes型数据
                tmp = bytes.fromhex(tmp)
            # 加入列表
            str_list.append(tmp)
            str = str[2:]
            
        return str_list

    def SplitStr2list(self, str, mode='int'):
        '''
        将各种以空格或者,为分割符的HEX字符串转换成目标类型列表
        int(默认)：int型
        bytes: bytes型
        '''
        length = len(str)
        
        j = 0 # 用于分隔符内的计数
        str_list = []
        list_cnt = 0

        for i in range(length):
            if j == 0:
                str_list.append('')
                if self.__isHex(str[i]):
                    str_list[list_cnt] = str_list[list_cnt] + str[i]
                    j += 1
                else:
                    # 第一个字符不是数值型字符
                    return None
            elif j == 1:
                if self.__isHex(str[i]):
                    # 第二个字符是数值型字符
                    str_list[list_cnt] = str_list[list_cnt] + str[i]
                    j += 1
                elif self.__isSplit(str[i]):
                    # 第二个字符是分隔符
                    j = 0
                    # 在前面补0
                    str_list[list_cnt] = '0' + str_list[list_cnt]
                    if(mode == 'int'):
                        # 将16进制字符串转为int
                        str_list[list_cnt] = int(str_list[list_cnt],base=16)
                    elif(mode == 'bytes'):
                        str_list[list_cnt] = bytes.fromhex(str_list[list_cnt])
                        
                    list_cnt += 1
                else:
                    return None
            elif j == 2:
                if self.__isSplit(str[i]):
                    j = 0
                    if(mode == 'int'):
                        str_list[list_cnt] = int(str_list[list_cnt],base=16)
                    elif(mode == 'bytes'):
                        str_list[list_cnt] = bytes.fromhex(str_list[list_cnt])
                    list_cnt += 1
                else:
                    return None
            else:
                return None

        if j == 1 :
            str_list[list_cnt] = '0' + str_list[list_cnt] 
            if(mode == 'int'):
                str_list[list_cnt] = int(str_list[list_cnt],base=16)
            elif(mode == 'bytes'):
                str_list[list_cnt] = bytes.fromhex(str_list[list_cnt])

        elif j == 2:
            if(mode == 'int'):
                str_list[list_cnt] = int(str_list[list_cnt],base=16)
            elif(mode == 'bytes'):
                str_list[list_cnt] = bytes.fromhex(str_list[list_cnt])

        return str_list


    def __isHex(self, str):
        if str >= 'a' and str <= 'f':
            return True
        elif str >= 'A' and str <= 'F':
            return True
        elif str >= '0' and str <= '9':
            return True
        else:
            return False

    def __isSplit(self, str):
        if str == ' ':
            return True
        elif str == ',':
            return True
        else:
            return False

if __name__ == "__main__":
    a = '01,02,3,5,9 ab bc c,'
    print("带分割符的字符串")
    print(str_hex().SplitStr2list(a))
    print("bytes型")
    print(str_hex().SplitStr2list(a, 'bytes'))
    a = '01020304050607081a1bbccdef'
    print('不带分割符的字符串')
    print(str_hex().NoSplitStr2list(a))
    print("bytes")
    print(str_hex().NoSplitStr2list(a,'bytes'))
