import rclpy
from rclpy.node import Node
from std_msgs.msg import  String

class BatteryStatusNode(Node):
	def __init__(self):
		super().__init__('battery_level')
		
		self.publisher = self.create_publisher(
			String,
			'battery_status',
			10
			)
		self.timer =  self.create_timer(
			1.0,
			self.publish_battery_status
			)

		self.battery_level  = 100
		self.get_logger().info("Battery Levels")

	def publish_battery_status(self):
		msg = String()
		self.battery_level -= 1
		msg.data = f"Robot battery level: {self.battery_level} %"
		self.publisher.publish(msg)
		self.get_logger().info(
			f'Piublishing : "{msg.data}"'
		)
		


def main(args = None):
	rclpy.init(args=args)
	node  =  BatteryStatusNode()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
