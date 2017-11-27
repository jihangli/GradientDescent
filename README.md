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
