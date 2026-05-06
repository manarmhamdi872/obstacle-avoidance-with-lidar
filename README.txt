Obstacle Avoidance with LiDAR

Description:
This project is a ROS2 Jazzy mobile robot project using Gazebo and RViz.
The robot is modeled with URDF/SDF and is prepared for obstacle avoidance using LiDAR.

Project files:
- urdf/robot.urdf.xacro : Robot model for RViz
- launch/display.launch.py : Launch file to visualize the robot in RViz
- model/mobile_robot.sdf : Robot model for Gazebo
- scripts/move_forward.py : Python script for basic movement command

Commands to launch the project:

Terminal 1: Build the workspace
cd ~/ros2_ws
colcon build
source install/setup.bash

Terminal 2: Launch RViz visualization
cd ~/ros2_ws
source install/setup.bash
ros2 launch my_mobile_robot display.launch.py

Terminal 3: Launch Gazebo
gz sim

Then choose:
Empty world
Run

Terminal 4: Spawn the robot in Gazebo
gz service -s /world/empty/create \
--reqtype gz.msgs.EntityFactory \
--reptype gz.msgs.Boolean \
--timeout 5000 \
--req 'sdf_filename: "/home/lyly/ros2_ws/src/my_mobile_robot/model/mobile_robot.sdf", name: "robot1", pose: {position: {x: 0, y: 0, z: 0.3}}'

Terminal 5: Send movement command
gz topic -t /cmd_vel -m gz.msgs.Twist -p 'linear: {x: 0.5} angular: {z: 0.0}'

Note:
RViz is used for visualization.
Gazebo is used for simulation.
The movement and LiDAR obstacle avoidance part will be improved in the next version.

