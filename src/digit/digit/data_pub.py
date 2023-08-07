import rclpy
import sys
from rclpy.node import Node
from get_data import Digit
import numpy as np
import ast
from route.srv import PointRequest

class pubDataNode(Node):
    def __init__(self, name, digit_str, midpoint):
        super().__init__(name)
        self.sting = None
        self.digit_str = digit_str
        self.midpoint = midpoint
        self.get_logger().info("Node success!")
        # 声明并创建客户端
        # 发送坐标服务 （create_service: 参数1：服务接口类型；参数2：服务名称）
        self.coordinate_client = self.create_client(PointRequest, "coordinate")


    def data_coordinate(self):
        """客户端发送请求
        """
        # 字符串处理获取数据坐标
        dg = Digit(self.digit_str, self.midpoint)
        numb, position, delta = dg.digit_position()
        point_x, point_y = dg.getNumTar(numb, position, delta)
        data_coordinate_x = []
        data_coordinate_y = []
        for array_x, array_y  in zip(point_x, point_y):
            data_coordinate_x.extend(array_x)
            data_coordinate_y.extend(array_y)
        # 等待服务启动，每1s检查一次，如果服务没有启动，则一直循环
        while not self.coordinate_client.wait_for_service(1.0):
            self.get_logger().warn("Wait")
        # 构建请求内容
        request = PointRequest.Request()
        request.x = data_coordinate_x
        request.y = data_coordinate_y
        request.isend = len(self.digit_str)
        #发送异步数据发送请求，成功后就调用data_coordinate_callback()函数
        self.coordinate_client.call_async(request).add_done_callback(self.data_coordinate_callback)
    
    def data_coordinate_callback(self, response):
        """发送数据回调函数
        """
        result = response.result()
        if result.flag == 1:
            self.get_logger().info("Client Success")
            self.digit_str = None
            self.midpoint = None
            rclpy.shutdown()
        else:
            self.get_logger().info("Fail")


def main(str, lst_str):
    rclpy.init()
    digit_str = str
    midpoint = ast.literal_eval(lst_str)
    node = pubDataNode("Coordinate", digit_str, midpoint)
    node.data_coordinate() # 调用发送数据服务
    rclpy.spin(node)
    # rclpy.shutdown()

if __name__ == '__main__':
    digit_str = sys.argv[1]
    midpoint = sys.argv[2]
    main(digit_str, midpoint)