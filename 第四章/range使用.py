'''
range(start, stop[, step])
它返回一个[start, start + step, start + 2 * step, ...,n*step]结构的整数序列，
说明： （1）step 默认 1；start 默认 0。
（2）range 函数返回一个左闭右开的序列数。
如果 step 是正整数，最后一个元素（start +n * step）小于 stop。
如果 step 是负整数，最后一个元素（start + n * step）大于 stop。
（3）step 参数必须是非零整数，否则抛出 VauleError 异常。
'''
for i in range(1,10,2):
    print(i,end=',')