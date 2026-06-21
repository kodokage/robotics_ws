import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FirstNode(Node):
	
	def __init__(self):
		super().__init__('status_publisher')
		
		self.publisher_ = self.create_publisher(
			String, 
			'robot_status',
			10
			)

		self.timer = self.create_timer(
			1.0,
			self.publish_status
			)
		self.counter = 0

		self.get_logger().info("Status publisher started")

	
	def publish_status(self):
		msg = String()
		self.counter +=1
		msg.data = f"Robot is alive: {self.counter}"
		self.publisher_.publish(msg)
		self.get_logger().info(
			f'Publishing : {msg.data}"'
		)

def main(args = None):
	rclpy.init(args=args)
	node = FirstNode()
	rclpy.spin(node) ## keeps process alive
	node.destroy_node()
	rclpy.shutdown()

if __name__== '__main__':
	main()
