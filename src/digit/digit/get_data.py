import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# digitLib = np.array([
#     [[-1, 0, 1, 2, 2.2, 2, 1, 0, -1, -2, -2.2, -2, -1],
#      [2, 2.2, 2, 1, 0, -1, -2, -2.2, -2, -1, 0, 1, 2]],
#     [[-0.5, 0, 0, 0, 0, 0],
#      [1.8, 2.2, 1, 0, -1, -2]],
#     [[-2, -1, 0.0, 1, 2, 0.9, -0.5, -2, -1, 0, 1, 2],
#      [1, 2, 2.2, 2, 1, 0, -1, -2, -2, -2, -2, -2]],
#     [[-1.5, -1, 0.0, 1, 2, 1, 0, 1, 2, 1, 0, -1, -1.5],
#      [1.5, 2, 2.2, 2, 1, 0, 0, 0, -1, -2, -2.2, -2, -1.5]],
#     [[   2,   0,  -1,  -3, -2, -1,-0.1,   0, 0,   0,  0],
#      [-0.5,-0.5,-0.5,-0.5,0.7,1.8, 2.5, 1.5, 0,-1.3,-2.5]],
#     [[1.5, 1, 0, -1, -2, -2, -2, -1, 0, 0.2, 1.5, 0, -1, -2],
#      [2, 2, 2, 2, 2, 1, 0, 0, 0, -0.1, -1, -2, -2, -2]],
#     [[1.26, 0.2, -0.95, -1.55, -1.32, 0, 1.15, 1.37, 0.75, -0.72, -1.53],
#      [1.4, 1.8, 1.52, 0, -1.14, -2, -1.51, -0.61, 0.26, 0.26, -0.4]],
#     [[-2, -1, 0, 1, 2, 1, 0, -1],
#      [2, 2, 2, 2, 2, 0.65, -0.66, -2]],
#     [[0, 0.58, 0.95, 1, 0.56, 0, -0.67, -0.96, -1, -0.87, 0, 0.76, 1.17, 0.98, 0, -0.86, -1.23, -0.97, -0.59, 0],
#      [0, 0.27, 0.77, 1.32, 1.81, 2, 1.74, 1.45, 1, 0.55, 0, -0.36, -1, -1.75, -2.15, -1.88, -1.21, -0.57, -0.17, 0]],
#     [[1.15, 0.78, 0, -1, -1.16, -0.62, 0, 0.89, 1.15, 1.17, 1.01, 0, -1.02],
#      [0.47, -0.02, -0.41, 0, 1, 1.81, 2, 1.59, 0.47, -0.51, -1.29, -2, -1.23]]
#     ],dtype = object)

class Digit:
    def __init__(self, digit_str, midpoint):
        self.digitLib = np.array([
                        [[-1, 0, 1, 2, 2.2, 2, 1, 0, -1, -2, -2.2, -2, -1],
                        [2, 2.2, 2, 1, 0, -1, -2, -2.2, -2, -1, 0, 1, 2]],
                        [[-0.5, 0, 0, 0, 0, 0],
                        [1.8, 2.2, 1, 0, -1, -2]],
                        [[-2, -1, 0.0, 1, 2, 0.9, -0.5, -2, -1, 0, 1, 2],
                        [1, 2, 2.2, 2, 1, 0, -1, -2, -2, -2, -2, -2]],
                        [[-1.5, -1, 0.0, 1, 2, 1, 0, 1, 2, 1, 0, -1, -1.5],
                        [1.5, 2, 2.2, 2, 1, 0, 0, 0, -1, -2, -2.2, -2, -1.5]],
                        [[   2,   0,  -1,  -3, -2, -1,-0.1,   0, 0,   0,  0],
                        [-0.5,-0.5,-0.5,-0.5,0.7,1.8, 2.5, 1.5, 0,-1.3,-2.5]],
                        [[1.5, 1, 0, -1, -2, -2, -2, -1, 0, 0.2, 1.5, 0, -1, -2],
                        [2, 2, 2, 2, 2, 1, 0, 0, 0, -0.1, -1, -2, -2, -2]],
                        [[1.26, 0.2, -0.95, -1.55, -1.32, 0, 1.15, 1.37, 0.75, -0.72, -1.53],
                        [1.4, 1.8, 1.52, 0, -1.14, -2, -1.51, -0.61, 0.26, 0.26, -0.4]],
                        [[-2, -1, 0, 1, 2, 1, 0, -1],
                        [2, 2, 2, 2, 2, 0.65, -0.66, -2]],
                        [[0, 0.58, 0.95, 1, 0.56, 0, -0.67, -0.96, -1, -0.87, 0, 0.76, 1.17, 0.98, 0, -0.86, -1.23, -0.97, -0.59, 0],
                        [0, 0.27, 0.77, 1.32, 1.81, 2, 1.74, 1.45, 1, 0.55, 0, -0.36, -1, -1.75, -2.15, -1.88, -1.21, -0.57, -0.17, 0]],
                        [[1.15, 0.78, 0, -1, -1.16, -0.62, 0, 0.89, 1.15, 1.17, 1.01, 0, -1.02],
                        [0.47, -0.02, -0.41, 0, 1, 1.81, 2, 1.59, 0.47, -0.51, -1.29, -2, -1.23]]
                        ],dtype = object)
        self.digit_str = digit_str
        self.midpoint = midpoint
    
    def digit_position(self):
        midpoint_x = self.midpoint[0]   
        midpoint_y = self.midpoint[1]
        # 将字符串每一位保存在数组中
        digit_list = [int(d) for d in self.digit_str]
        # 获取字符串的长度
        string_length = len(self.digit_str)
        max_length = 6
        min_delta = 0.5
        max_delta = 1.0
        alpha = 0.25
        if string_length <= 1:
            delta_x, delta_y = max_delta, 1.5*max_delta
        elif string_length >= max_length:
            delta_x ,delta_y = min_delta, 1.5*min_delta
        else:
            delta_x = min_delta + (max_delta - min_delta) * np.cos(alpha * string_length)
            delta_y = 1.5 * delta_x 
        delta = np.array([delta_x,delta_y])
        delta_num = 5 * delta_x
        positions = np.zeros((string_length, 2))  
        if string_length % 2 == 0:  
            center_x = midpoint_x - (string_length // 2 - 0.5) * delta_num  
        else:  
            center_x = midpoint_x - (string_length // 2) * delta_num  

        for i, _ in enumerate(digit_list):
            x_position = center_x + i * delta_num
            y_position = midpoint_y
            positions[i] = (x_position, y_position)
        return digit_list, positions, delta

    def cubic_spline_interpolation(self, points, num_points=1000):
        t = np.linspace(0, 1, len(points))
        x = np.array([point[0] for point in points])
        y = np.array([point[1] for point in points])

        cs_x = CubicSpline(t, x)
        cs_y = CubicSpline(t, y)

        t_new = np.linspace(0, 1, num_points)
        X = cs_x(t_new)
        Y = cs_y(t_new)

        return X, Y

    def getNumTar(self, num, mid_position, delta):
        X =  [[] for _ in range(len(num))]
        Y =  [[] for _ in range(len(num))]
        delta_x, delta_y = delta[0], delta[1]
        for i in range(len(num)):
            midpoint_x = mid_position[i][0]
            midpoint_y = mid_position[i][1]
            cx = np.array(self.digitLib[num[i]][0])
            cy = np.array(self.digitLib[num[i]][1])

            numc = np.array([midpoint_x + cx * delta_x, midpoint_y + cy * delta_y]).T

            Xi, Yi = self.cubic_spline_interpolation(numc)

            X[i] = Xi
            Y[i] = Yi

        #     plt.plot(Xi, Yi, 'b-', label='Num digit')
        # plt.xlim(0, 2 * self.midpoint[0]) # 白板的大小
        # plt.ylim(0, 2 * self.midpoint[1])
        # plt.grid(True)
        # plt.xlabel('X')
        # plt.ylabel('Y')
        # plt.show() 
        return X, Y


# midpoint = [15,8]
# df = Digit("012", midpoint)
# numb, position, delta = df.digit_position()
# XX, YY = df.getNumTar(numb, position, delta)
# p_x = []
# p_y = []
# for array_x, array_y in zip(XX, YY):
#     p_x.extend(array_x)
#     p_y.extend(array_y)
# print(XX)
# print(p_x)
# print(len(p_x))
# print(YY)
# print(p_y)
# print(len(p_y))
 