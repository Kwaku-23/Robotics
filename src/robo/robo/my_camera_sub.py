import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class ImageSubscriberNode(Node):
    def __init__(self):
        super().__init__('image_subscriber')

        self.create_subscription(
            Image,
            'camera/image_raw',      # Must match publisher topic
            self.listener_callback,
            10
        )
        self.get_logger().info('Image Subscriber has started.')

    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received image -> Size: {msg.width}x{msg.height}, '
            f'Encoding: {msg.encoding}, '
            f'Frame: {msg.header.frame_id}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()