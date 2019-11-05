from crc import crc_16_ccit_false

class PARA():
    '''
    参数管理类
    '''

    def add_para(self,type,data):

        __para = {}

        if type[0] == 0xf0:
            __para['type'] = 0xf0
            
        elif type[0] == 0x01:
            if len(data) != 0x01:
                return False
            __para['type'] = 0x01

        elif type[0] == 0x02:
            if len(data) != 0x02:
                return False
            __para['type'] = 0x02

        elif type[0] == 0x04:
            if len(data) != 0x04:
                return False
            __para['type'] = 0x04

        elif type[0] == 0x08:
            if len(data) != 0x08:
                return False
            __para['type'] = 0x08

        elif type[0] >= 0x10 and type[0] < 0x20:
            length = 16 * ((type[0]&0x0f) + 1)
            if len(data) != length:
                return False
            __para['type'] = type[0]

        else:
            return False

        __para['len'] = len(data)
        __para['data'] = data

        return __para


class PARA_CMD(PARA):
    def __init__(self):
        self.header = 0x55    # 包头
        self.protocol = 0x00  # 透明协议

        self.cmd_para = {
            'cmd' :[],
            'para':[]
            }

    def add_cmd(self, cmd):
        if len(cmd) != 3:
            return False

        if len(self.cmd_para['cmd']) == 0:
            self.cmd_para['cmd'] += cmd
        elif len(self.cmd_para['cmd']) == 3:
            self.cmd_para['cmd'][0] = cmd[0]
            self.cmd_para['cmd'][1] = cmd[1]
            self.cmd_para['cmd'][2] = cmd[2]
        else:
            return False
        return True

    def add_para(self, type, data):
        result = super().add_para(type, data)
        if result == False:
            return False

        self.cmd_para['para'].append(result)

        return True

    def get_cmd_para(self):
        return self.cmd_para

    def del_para(self):
        # 删除最后一个参数
        length = len(self.cmd_para['para'])
        if length == 0:
            return
        
        self.cmd_para['para'] = self.cmd_para['para'][:-1]

    def completeCmdPara(self):
        '''
        将命令和参数组装成最终的数值列表
        包头+长度+校验+命令+参数1+参数2+...+CRC16
        '''
        package = []

        if len(self.cmd_para['cmd']) == 0:
            return None

        # 加入包头
        package.append(self.header) 
        
        # 加入命令  
        package += self.cmd_para['cmd']

        # 取出参数个数
        para_num = len(self.cmd_para['para'])

        # 命令的3个字节
        package_len = 3 
        p_len = 0

        for i in range(para_num):
            # 加入参数类型
            package.append(self.cmd_para['para'][i]['type'])
            if self.cmd_para['para'][i]['type'] == 0xf0:
                p_len = self.cmd_para['para'][i]['len']                
                package.append((p_len & 0xff00)>>8)
                package.append(p_len & 0xff)
                p_len += 3
            else:
                p_len = self.cmd_para['para'][i]['len']
                
                p_len += 1

            package += self.cmd_para['para'][i]['data']
            package_len += p_len

        # 插入包长的高字节
        package.insert(1, (package_len&0xff00)>>8)
        # 插入包长的低字节
        package.insert(2, package_len&0xff)

        # 计算负载校验
        check = ((package[1]&0xf0)>>4)+(package[1]&0x0f) + \
                ((package[2]&0xf0)>>4)+(package[2]&0x0f) + self.protocol

        check = (~check) & 0x0f

        # 插入负载校验
        package.insert(3, (check+(self.protocol<<4)))

        # CRC
        crc_16 = crc_16_ccit_false(package, 1, len(package))

        package.append((crc_16&0xff00)>>8)
        package.append(crc_16&0xff)

        return package


if __name__ == "__main__":
    cmd = [0x70,0x00,0x02]
    a = PARA_CMD()
    a.add_cmd(cmd)
    a.add_para([0x01], [0x03])
    a.add_para([0x04],[0x01,0x02,0x04,0x06])
    a.add_para([0xf0],[0x02,0x03,0x09])
    print(a.completeCmdPara())