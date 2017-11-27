import numpy as np
import matplotlib.pyplot as plt


def foo(x):
    return x ** 2 - 2 * x + 1


def derivative(x):
    """
    example: try to find the min value for x^2 - 2x + 1

    :param x: x value
    :return: derivate of function x^2 - 2x + 1
    """
    return 2 * x - 2


def gradient_descent(start, step):
    """
    Calculate gradient descent with start value and step

    :param start: a random start value
    :param step: learning rate
    :return: result
    """
    # best parameter we can get so far
    result = start
    for i in range(20):
        # calculate derivative of the function
        grad = derivative(result)
        # update result
        result -= grad * step
        print 'Iteration {0}: grad = {1}, result = {2}'.format(i, grad, result)
    return result


"""numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)"""
#x = np.linspace(-10, 10, 100)
#y = foo(x)
#plt.plot(x, y)
#plt.show()

gradient_descent(5, 0.1)
