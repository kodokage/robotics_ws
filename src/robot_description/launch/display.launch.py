from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {
                "robot_description":
                open(
                    "src/robot_description/urdf/generated_robot.urdf"
                ).read()
            }
        ]
    )


    joint_state_publisher = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )


    rviz = Node(
        package="rviz2",
        executable="rviz2"
    )


    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        rviz
    ])

## Run the launch file
####>>  ros2 launch robot_description display.launch.py
