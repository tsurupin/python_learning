import numpy as np
from function_2 import function_2
from numercial_gradient import numercial_gradient

def gradient_decent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numercial_gradient(f, x)
        x -= lr * grad

    return x

print(gradient_decent(function_2, np.array([-3.0, 4.0]), 0.1, 100))