# ucsd_robocar_nav1_pkg 

<img src="ucsd_ros_logo.png">

<div>

## Table of Contents

  - [**Enable X11 forwarding**](#7-enable-x11-forwarding)
  - [**Work Flow To Use This Repository**](#work-flow-to-use-this-repository)
  - [**Navigation Packages**](#navigation-packages)
    - [ucsd_robocar_lane_detection1_pkg](#ucsd_robocar_lane_detection1_pkg)
    - [ucsd_robocar_sensor1_pkg](#ucsd_robocar_sensor1_pkg)
    - [ucsd_robocar_actuator1_pkg](#ucsd_robocar_actuator1_pkg)
  - [**Launch**](#launch)
    - [camera_nav_calibration_launch](#camera_nav_calibration_launch)
    - [camera_nav_launch](#camera_nav_launch)
  - [**Tools**](#tools)
    - [ROS Guide Book](#ros-guide-book)
  - [**Troubleshooting**](#troubleshooting)


## **Enable X11 forwarding**

Associated file: **x11_forwarding_steps.txt**

Some jetsons may not have this enabled, so if needed please read the steps <a href="https://gitlab.com/ucsd_robocar2/ucsd_robocar_nav2_pkg/-/blob/master/x11_forwarding_steps.txt" >here</a> to setup X11 forwarding


<div align="center">

## **Work Flow To Use This Repository**

</div>

1. Pull docker image <a href="https://hub.docker.com/r/djnighti/ucsd_robocar" >here</a> for this repo that contains this repo and all its dependecies for plug-n-play use. This link provides neccessary instructions for running the docker container.


2. Calibrate the camera, throttle and steering values using the calibration_node from [ucsd_robocar_lane_detection_pkg](#ucsd-robocar-lane-detection-pkg)

There are car_type options that can be eneterd at the command line or you can modify in the launch files as needed, when argument is not specified, the default is set to custom_car_launch: 
  1. dsc_car_launch
  2. mae_148_car_launch
  3. custom_car_launch

ex. 

`roslaunch ucsd_robocar_nav1_pkg camera_nav_calibration_launch.launch`

`roslaunch ucsd_robocar_nav1_pkg camera_nav_calibration_launch.launch -car_type dsc_car_launch`

3. Launch camera_nav_launch from [ucsd_robocar_lane_detection_pkg](#ucsd-robocar-lane-detection-pkg)

As with the calibration, you can also specify a car type at the command line.

`roslaunch ucsd_robocar_nav1_pkg camera_nav_launch.launch`

4. Tune parameters in step 2 until desired behavior is achieved

<div align="center">

## Navigation Packages

</div>

### ucsd_robocar_lane_detection1_pkg

All the details for this package about all the nodes, topics and launch files are exaplained in **explcit** detail <a href="https://gitlab.com/ucsd_robocar/ucsd_robocar_lane_detection1_pkg" >**here**</a> from its official git repo. **HIGHLY RECOMMENDED TO GO THROUGH THE README TO UNDERSTAND HOW TO USE IT.**

| Nodes | Subscribed Topics | Published Topics |
| ------ | ------ | ------ |
| lane_detection_node | /camera/color/image_raw | /centroid |
| lane_guidance_node  | /centroid               | /cmd_vel |
| calibration_node    | /camera/color/image_raw | /cmd_vel  |

### ucsd_robocar_sensor1_pkg

All the details for this package about all the nodes, topics and launch files are exaplained in **explcit** detail <a href="https://gitlab.com/ucsd_robocar/ucsd_robocar_sensor1_pkg" >**here**</a> from its official git repo. **HIGHLY RECOMMENDED TO GO THROUGH THE README TO UNDERSTAND HOW TO USE IT.**

| Nodes |  Msg Type | Published Topics |
| ------ | ------ | ------ |
| webcam_node           | sensor_msgs.msg.Image       | /camera/color/image_raw |
| realsense_ros2_camera | sensor_msgs.msg.Image       | /camera/color/image_raw |
| ldlidar               | sensor_msgs.msg.LaserScan   | /scan |
| rplidar_composition   | sensor_msgs.msg.LaserScan   | /scan |
| sick_generic_caller   | sensor_msgs.msg.LaserScan   | /scan |

### ucsd_robocar_actuator1_pkg

All the details for this package about all the nodes, topics and launch files are exaplained in **explcit** detail <a href="https://gitlab.com/ucsd_robocar/ucsd_robocar_actuator1_pkg" >**here**</a> from its official git repo. **HIGHLY RECOMMENDED TO GO THROUGH THE README TO UNDERSTAND HOW TO USE IT.**

| Nodes |  Msg Type | Subscribed Topics | info |
| ------ | ------ | ------ | ------ |
| adafruit_steering_node | std_msgs.msg.Float32 | /steering | value range: [-1,1] |
| adafruit_throttle_node | std_msgs.msg.Float32 | /throttle | value range: [-1,1] |
| vesc_steering_node     | std_msgs.msg.Float32 | /steering | value range: [-1,1] |
| vesc_rpm_node          | std_msgs.msg.Float32 | /throttle | value range: [-1,1] |
| adafruit_twist_node    | geometry_msgs.msg.Twist | /cmd_vel | linear.x (forwards/backwards) angular.z (steering) ranges: [-1,1] |
| vesc_twist_node        | geometry_msgs.msg.Twist | /cmd_vel | linear.x (forwards/backwards) angular.z (steering) ranges: [-1,1] |


<div align="center">

## Launch

</div>

#### **camera_nav_calibration_launch**

Associated package: [ucsd_robocar_lane_detection_pkg](#ucsd-robocar-lane-detection-pkg)

Associated file: **ros_racer_calibration_launch.launch**

Associated nodes: lane_detection_node, lane_guidance_node

This file will launch **ros_racer_calibration_launch.launch** from [ucsd_robocar_lane_detection_pkg](#ucsd-robocar-lane-detection-pkg) and [throttle and steering launch](#throttle-and-steering-launch)

`roslaunch ucsd_robocar_nav1_pkg camera_nav_calibration_launch.launch`

#### **camera_nav_launch**

Associated package: [ucsd_robocar_lane_detection1_pkg](#ucsd-robocar-lane-detection1-pkg)

Associated file: **ros_racer_launch.launch**

Associated nodes: lane_detection_node, lane_guidance_node

This file will launch both the **lane_detection_node** and **lane_guidance_node** and load the parameters determined using the **calibration_node** from [ucsd_robocar_lane_detection2_pkg](#ucsd-robocar-lane-detection2-pkg) and launch [throttle and steering launch](#throttle-and-steering-launch)

**Before launching, please calibrate the robot first while on the stand!**

`roslaunch ucsd_robocar_nav1_pkg camera_nav_launch.launch`



<div align="center">

## Tools 

</div>

#### ROS Guide Book

For help with using ROS in the terminal and in console scripts, check out this google doc <a href="https://docs.google.com/document/d/1u7XS7B-Rl_emK3kVKEfc0MxHtwXGYHf5HfLlnX8Ydiw/edit?usp=sharing" >here</a> to see tables of ROS commands and plenty of examples of using ROS in console scripts.

<div align="center">

## Troubleshooting

</div>

[ucsd_robocar_lane_detection1_pkg](#ucsd-robocar-lane-detection1-pkg) : see troubleshooting guide <a href="https://gitlab.com/ucsd_robocar/ucsd_robocar_lane_detection1_pkg#troubleshooting" >here</a>

[ucsd_robocar_sensor1_pkg](#ucsd-robocar-sensor1-pkg) : see troubleshooting guide <a href="https://gitlab.com/ucsd_robocar/ucsd_robocar_sensor1_pkg#troubleshooting" >here</a>

[ucsd_robocar_actuator1_pkg](#ucsd-robocar-actuator1-pkg) : see troubleshooting guide <a href="https://gitlab.com/ucsd_robocar/ucsd_robocar_actuator1_pkg#troubleshooting" >here</a>
