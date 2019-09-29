# Python的HEX型字符串、int型列表、bytes型列表的互相转换

## HEX型字符串：
  1. 有分割:
      01 02 03 04 05 06 1a 1b 1c 1d 1e
      1,2,3,0b,0c,f,a
      12 23,89,7a,12 90
  
  2. 无分割:(必须为偶数个字符)
      123465020407
     
## NoSplitStr2list方法：
    将无分割的字符串转换为int型列表或者bytes型列表

## SplitStr2list方法
    将有分割的字符串转换为int型列表或者bytes型列表
    
```python
  a = '01,02,3,5,9 ab bc c,'
  print(str_hex.SplitStr2list(a))
  # 输出:[1, 2, 3, 5, 9, 171, 188, 12]
  
  print(str_hex.SplitStr2list(a, 'bytes'))
  # 输出:[b'\x01', b'\x02', b'\x03', b'\x05', b'\t', b'\xab', b'\xbc', b'\x0c']
  
  a = '01020304050607081a1bbccdef'
  print(str_hex.NoSplitStr2list(a))
  # 输出:[1, 2, 3, 4, 5, 6, 7, 8, 26, 27, 188, 205, 239]
  
  print(str_hex.NoSplitStr2list(a, 'bytes'))
  # 输出:[b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07', b'\x08', b'\x1a', b'\x1b', b'\xbc', b'\xcd', b'\xef']
  
```
