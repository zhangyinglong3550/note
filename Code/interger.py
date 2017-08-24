#! /usr/bin/env python3
days = int(input("Enter days:"))
print("Month = {} Days = {}".format(*divmod(days,30)))
