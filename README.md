# GradientDescent
A simplest example to understand gradient descent

Why Gradient Descent
1. 梯度方向表示了函数增长速度最快的方向，其反方向即为函数减少最快的方向
2. 对于机器学习模型的优化，朝着梯度下降的方向走我们就可以找到函数的极小值

How to implement a basic Gradient Descent
最简单的梯度下降算法可以由两个函数和三个变量组成
1. 函数1：待求的函数
2. 函数2：待求函数的导数
3. 变量1：到目前为止所得的最优变量
4. 变量2：梯度（函数导数的相反值）
5. 变量3：步长，沿着梯度下降方向的步长 

Simple Example:
Find the min value for function: x^2 - 2x + 1

![Plot 1](plot.png?raw=true "Optional Title")

```python
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
    for i in range(10):
        # calculate derivative of the function
        grad = derivative(result)
        # update result
        result -= grad * step
        print 'Iteration {0}: grad = {1}, result = {2}'.format(i, grad, result)
    return result


"""numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)"""
x = np.linspace(-10, 10, 100)
y = foo(x)
plt.plot(x, y)
plt.show()

gradient_descent(5, 0.1)
```

After running above code, we can get the output like below:

Iteration 0: grad = 8, result = 4.2<br />
Iteration 1: grad = 6.4, result = 3.56<br />
Iteration 2: grad = 5.12, result = 3.048<br />
Iteration 3: grad = 4.096, result = 2.6384<br />
Iteration 4: grad = 3.2768, result = 2.31072<br />
Iteration 5: grad = 2.62144, result = 2.048576<br />
Iteration 6: grad = 2.097152, result = 1.8388608<br />
Iteration 7: grad = 1.6777216, result = 1.67108864<br />
Iteration 8: grad = 1.34217728, result = 1.536870912<br />
Iteration 9: grad = 1.073741824, result = 1.4294967296<br />
Iteration 10: grad = 0.8589934592, result = 1.34359738368<br />
Iteration 11: grad = 0.68719476736, result = 1.27487790694<br />
Iteration 12: grad = 0.549755813888, result = 1.21990232556<br />
Iteration 13: grad = 0.43980465111, result = 1.17592186044<br />
Iteration 14: grad = 0.351843720888, result = 1.14073748836<br />
Iteration 15: grad = 0.281474976711, result = 1.11258999068<br />
Iteration 16: grad = 0.225179981369, result = 1.09007199255<br />
Iteration 17: grad = 0.180143985095, result = 1.07205759404<br />
Iteration 18: grad = 0.144115188076, result = 1.05764607523<br />
Iteration 19: grad = 0.115292150461, result = 1.04611686018<br />

As we can see, after 20 iterations, the result becomes 1.04 which is very close to our answer(1.0)


