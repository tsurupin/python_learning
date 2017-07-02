import numpy as np
from function_2 import function_2

def numercial_gradient(f, x):
    h = 1e-4

    grad = np.zeros_like(x)

    for idx in range(x.size):

        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val

    return grad


# print(numercial_gradient(function_2, np.array([3.0, 4.0])))