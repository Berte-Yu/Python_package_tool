# Python编写的数据包组包小工具

## 数据包格式

| 数据包域 | 说明 |
| :--: | :--: |
| 包头 | 0x55 |
| 包长H | 数据区的长度高8位 |
| 包长L | 数据区的长度低8位 |
| 协议 | 表示数据区的协议(4bit) |
| 负载校验 | 包长H、包长L和协议的每4bit的和的取反 |
| 数据区 | ... |
| 数据区 | ... |
| 数据区 | ... |
| CRC16-H | CRC16的校验和的高8位(数据区的所有的数据参与CRC计算) |
| CRC16-L | CRC16的校验和的高8位 |

