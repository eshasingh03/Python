#!/usr/bin/env python
# coding: utf-8

# # Print the number with their suffix

# In[1]:


num = int(input('Enter a num'))
if ((str(num)[-1])=='1') and (num<10):
    print(f'{num}st')
elif ((str(num)[-1])=='2') and (num<10):
    print(f'{num}nd')
elif ((str(num)[-1])=='3') and (num<10):
    print(f'{num}rd')
elif (((10>num) or (num>20)) and (((str(num)[-1])=='3') and ((str(num)[-2])!='1'))):
    print(f'{num}rd')
elif (((10>num) or (num>20)) and (((str(num)[-1])=='2') and ((str(num)[-2])!='1'))):
    print(f'{num}nd')
elif (((10>num) or (num>20)) and (((str(num)[-1])=='1') and ((str(num)[-2])!='1'))):
    print(f'{num}st')
else:
    print(f'{num}th')

