# ROS2 Mobile Robot Project

Simple mobile robot project using ROS2 Jazzy, RViz and Gazebo.

## Features
- URDF robot visualization in RViz
- SDF robot model in Gazebo
- Mobile robot with wheels
- Basic movement command using cmd_vel

## Run RViz
cd ~/ros2_ws
source install/setup.bash
ros2 launch my_mobile_robot display.launch.py

## Run Gazebo
gz sim

Then spawn the robot:

gz service -s /world/empty/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 5000 --req 'sdf_filename: "/home/lyly/ros2_ws/src/my_mobile_robot/model/mobile_robot.sdf", name: "robot1", pose: {position: {x: 0, y: 0, z: 0.3}}'

