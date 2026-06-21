from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return  LaunchDescription([
	
		Node(
			package='first_robot_package',
			executable='first_node',
			name='first_node'	
		),
	
		Node(
			package='first_robot_package',
			executable='status_listener',
			name='status_listener'
		),

		Node(
			package='first_robot_package',
			executable='second_node',
			name='second_node',
			parameters=[
				{'publish_rate':0.5}
			]
		)
		

])
