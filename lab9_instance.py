'''
lab 9 
instance 
'''

#step 3
from lab9_class import my_stat

my_cal_instance = my_stat()

#step 4
print(my_cal_instance.cal_sigma(3,5))

print(my_cal_instance.cal_pi(3,5))

print(my_cal_instance.cal_f(5))

print(my_cal_instance.cal_p(5,2))

#step 5
import numpy as np

print(np.math.factorial(999))

print(my_cal_instance.cal_f(999))