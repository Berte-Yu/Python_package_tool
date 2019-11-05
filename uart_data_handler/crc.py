#coding:utf-8

def crc_16_ccit_false(data, start, end):
    '''
    poly: 0x1021
    init: 0xffff
    xorout: 0x0000 结果异或值
    refin: False  输入不取反
    refout: False 输出不取反
    '''
    POLY16 = 0x1021
    crc = 0xffff

    for i in range(start, end):
        crc ^= (data[i]<<8)&0xffff

        for j in range(8):
            if ((crc & 0x8000)>0):
                crc = ((crc<<1)^POLY16)&0xffff
            else:
                crc = (crc << 1)&0xffff
    return crc

if __name__ == '__main__':
    a = [0x70,0x00,0x02]
    print(crc_16_ccit_false(a, 0, 3))
