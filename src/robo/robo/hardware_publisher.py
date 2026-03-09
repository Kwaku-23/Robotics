#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# 1. Import the message from your custom package
from my_robot_interfaces.msg import HardwareStatus 

class HardwareStatusPublisher(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher")
        
        # 2. Create a publisher and specify the HardwareStatus interface
        # The arguments are: (Message Type, Topic Name, Queue Size)
        self.publisher_ = self.create_publisher(HardwareStatus, "hardware_status", 10)
        
        # Create a timer to publish the message periodically (e.g., every 1 second)
        self.timer_ = self.create_timer(1.0, self.publish_status)
        self.get_logger().info("Hardware status publisher has been started.")

    def publish_status(self):
        # 3. Create a message object
        msg = HardwareStatus()
        
        # Assign values to the fields defined in your custom message
        msg.temperature = 34.5
        msg.version = 1
        msg.are_motors_ready = True
        msg.debug_message = "Motors are running at optimal temperature."
        
        # Publish the message to the topic
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()