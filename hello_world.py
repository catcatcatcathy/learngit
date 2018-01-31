#!/usr/bin/python
# -*- coding: utf-8 -*-

 num = [1]
    while True: 
        yield num
        new = num[:]
        for i in range (len(num)):
            if i != 0:
                num[i] = new[i] +new[i-1]
        num.append(1)