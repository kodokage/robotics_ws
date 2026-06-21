# ROS 2 Robotics Workspace

Learning and development workspace for ROS 2 Jazzy robotics projects.

## Current Package

### first_robot_package

Implemented concepts:

- ROS 2 packages
- Nodes
- Publishers and subscribers
- Topics
- Services
- Parameters
- Launch files

## Nodes

### first_node
Publishes robot status messages.

Topic:
- /robot_status

Message:
- std_msgs/msg/String


### status_listener
Subscribes to robot status.

Topic:
- /robot_status


### add_service
Service server example.

Service:
- /add_two_numbers

Type:
- example_interfaces/srv/AddTwoInts


## Running

Build workspace:

```bash
colcon build

## source 
install/setup.bash

## Launch
ros2 launch first_robot_package robot_system.launch.py
