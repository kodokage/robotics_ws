import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddService(Node):

	def __init__(self):
		super().__init__('add_service')

		self.service = self.create_service(
			AddTwoInts,
			'add_two_numbers',
			self.add_callback
		)

		self.get_logger().info(
		'Add service ready'
		)

	def add_callback(self, request, response):
	
		response.sum = request.a + request.b

		self.get_logger().info(
			f'Request: {request.a} + {request.b}'			
		)
	
		return response

def main(args=None):

    rclpy.init(args=args)

    node = AddService()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()

#--call the service
#--ros2 service call /add_two_numbers example_interfaces/srv/AddTwoInts "{a: 5, b: 3}"

