# Listing_5-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------
# 使用 raw_input()转换温度

# Temperature conversion program

print "This program converts Fahrenheit to Celsius"
print "Type in a temperature in Fahrenheit: ",
print "这个程序把华氏度转为摄氏度"
print "输入一个华氏度数值: ",
fahrenheit = float(raw_input())           # Get the Fahrenheit temperature from the user
celsius = (fahrenheit - 32) * 5.0 / 9
print "That is",                          # Notice the commas at the ends
print "这个华氏度经转换后为",                          # Notice the commas at the ends
print celsius,                            #   of these lines
print "degrees Celsius"
print "摄氏度"