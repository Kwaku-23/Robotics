import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class ImagePublisherNode(Node):
    def __init__(self):
        super().__init__('image_publisher')

        self.publisher_ = self.create_publisher(Image, 'camera/image_raw', 10)

        # Publish every 1 second
        self.timer = self.create_timer(1.0, self.publish_image)
        self.get_logger().info('Image Publisher has started.')

    def publish_image(self):
        msg = Image()

        # Fill in the fields
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera_frame'
        msg.height = 480
        msg.width = 640
        msg.encoding = 'rgb8'
        msg.step = msg.width * 3  # width * channels (3 for rgb8)

        # Fake pixel data: all zeros (black image)
        msg.data = [0] * (msg.height * msg.step)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published image: {msg.width}x{msg.height}')

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()