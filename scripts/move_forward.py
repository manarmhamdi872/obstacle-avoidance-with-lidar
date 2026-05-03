#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MoveForward(Node):
    def __init__(self):
        super().__init__('move_forward_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.0

        self.get_logger().info('Robot moving forward...')
        start_time = time.time()

        while time.time() - start_time < 3:
            self.publisher.publish(msg)
            time.sleep(0.1)

        stop_msg = Twist()
        self.publisher.publish(stop_msg)
        self.get_logger().info('Robot stopped.')

def main(args=None):
    rclpy.init(args=args)
    node = MoveForward()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

