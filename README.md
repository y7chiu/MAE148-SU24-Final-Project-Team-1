# Robocar: ROS, Localization and Obstacle Detection
[![<img width="450" alt="截圖 2024-09-06 11 49 20" src="https://github.com/user-attachments/assets/2be48b3e-bd5f-4d92-b083-6c12f176b6be">](https://jacobsschool.ucsd.edu/sites/default/files/UCSDLogo_JSOE_BlueGold_0_0.png)](https://jacobsschool.ucsd.edu/)

# Table of Contents
- [Device](#device)
- [Hardware](#hardware)
- [Members](#members)
- [Project Idea - Foresight](#project-idea---foresight)
- [Instructions for Our Project - What we have done](#instructions-for-our-project---what-we-have-done)
  - [SLAM](#slam)
  - [Depthai-ROS Installation](#depthai-ros-installation)
  - [DepthCloud Obstacle Detection](#depthcloud-obstacle-detection)
  - [Odometry Localization / AMCL Localization](#odometry-localization--amcl-localization)
  - [Combination between Depth-Camera and ROS](#combination-between-depth-camera-and-ros)
- [Future Development](#future-development)
  - [Costmaps / pointCloud Integration](#costmaps--pointcloud-integration)
  - [Path-Planner](#path-planner)
- [Resource](#resource)
- [License](#license)

## Team 1 - Summer2024

## Device

![Car_2](https://github.com/y7chiu/Summer-2024-final-project-team-1/blob/main/images/car.png)

## Hardware

- Base Plate

- Camera Holder

- Camera Protective Case

- Lidar Stand

- Jetson Nano Case

- Car Side Protection

- GPS Stand

- LED Light Decoration


## Members

Chiu, Yi-Chan(Frankie) - y7chiu@ucsd.edu

Solano, Josue - Josolano@ucsd.edu

Lin, Isaac - chl146@ucsd.edu

Joshi, Pratham - p1joshi@ucsd.edu

## Project Idea - Foresight

The project applies to the real world, such as hospital emergency, Uber taxi service, finding missing people when the environment has lack of signal, ...,etc.

***Project Background: The drunkard is in the EBU2, and he wants to go home right now…***

1. Acquire a scan of the ebu 2 courtyard using SLAM and load it onto RVIZ, which utilizes the lidar.

2. Get the OAK-D-LITE to publish point-cloud message through depthai over ROS1.

3. Get the odometry localization to work on NAV1 on the pre-loaded map.

4. Integrate pointcloud (via ros bridge) , static map, costmap, path-planner, laserscan over NAV2.

### What need to have:

- SLAM: simultaneous localization and mapping to generate a map of the ebu2 courtyard.

- Rviz: to make the environment familiar first by learning the environment map first. Path planning.

- OAK-D-LITE: Path finding algorithm, 3D obstacle detection.

- Camera, odometry and SLAM map must work hand in hand for localization and path-finding.

## Instructions for Our Project - What we have done

### SLAM
Making the slam map by using the laser scan. Here's the instruction for SLAM in section 11.3 of [13May24 - Copy of 100-UCSD Robocar Framework](https://docs.google.com/document/d/1suadghL1apftABkIY9B2dVCq7SvdlS5n5sqQ0ItTAk4/edit#heading=h.tqf2qplbiqoi)

The most important for this part is ros bridge. We need this to save the map and run the map algorithm.

here's are two examples we made for SLAM maps: DIB and EBU2.

![DIB](https://github.com/user-attachments/assets/ee6c5635-b7e7-471f-9204-131c4d127f27)
![EBU2](https://github.com/user-attachments/assets/8ab23eb6-081b-47f3-8df2-8658ebc524a2)

### Depthai-ROS Installation

For the obstacle detection, we use the depthai-ROS, which is other than the roboflow, that can detect the objects in 3D/2D and can efficiently communicate with ROS.
Here's the website we use to install: 

[Depthai-ROS Installation](https://docs.luxonis.com/software/ros/depthai-ros/build/)

- Tip: If the foxy version of installation could not setup well for ROS2. Try to install in the Noetic version.

### DepthCloud Obstacle Detection

After install the package for the depthai-ROS, there is the file called ```depthai_ros_driver``` and depthai_example.

For the depthai_ros_driver, try to run this command.

```
ros2 launch depthai_ros_driver camera.launch.py (ROS2)

or

roslaunch depthai_ros_driver camera.launch (ROS1)
```
to see if the depthai connect to OAK-D-Lite camera. Make sure to subscribe the topic.

Here's the video for the camera: 

[depthai-image1](https://drive.google.com/file/d/1Hsq4bKchXgDa42eyD91rlTCDn-h9Hm3z/view?usp=drive_link)

[depthai-image2](https://drive.google.com/file/d/14D3wZ3K0S6b90Jr54nBLcOdukYUOTeXe/view?usp=drive_link)

### Odometry Localization / AMCL Localization

**Odometry part:**

Using the ROS2 odometry to keep the car localizing on the place corresponding to the loacation of the pre-loaded map.

This might be not precise enough due to some reasons. E.g.: misalignment.

Our car has this issue that when the car goes forward without steering, the car turns left by itself.

Here's the video of odometry localization: 

[Odometry-localization](https://drive.google.com/file/d/1KdBV6wFqkR_j1UWYOesLToKH0TXp4PAU/view?usp=drive_link)

Therefore, we use another technique to localize the car. That is called AMCL loaclization.

**AMCL part:**

In order to account for the odometry drift, we employ an algorithm that compare the pre-loaded map against the lidar data and extrapolate the localization error from dead reckoning. 

In order for the amcl algorithm to work, all the frames in the tf tree need to be explicitly linked to the map frame (e.g. laser to base_link), and the base_frame, global_frame, laser_frame in the amcl node need to be consistent with the robot's URDF.

The node automatically handles the transform between the map frame and the base frame, so no broadcaster has to be manually written.

![Image](https://github.com/y7chiu/Summer-2024-final-project-team-1/blob/main/images/amcl_schematic.png)

Here are videos about amcl localization corresponding to the pre-loaded map:

[AMCL on Rviz](https://drive.google.com/file/d/1tZ24WpcLGSBS4LHYTWOvVtJ8zM9hVlEv/view)

[AMCL corresponding to the preloaded map on Rviz](https://drive.google.com/file/d/19hQZvwONtIX7JxddA7MgKAqW3bxP13Kv/view)


### Combination between Depth-Camera and ROS

***In this part, the car must use ROS1 and ROS2 connected with ROS bridge in order to make the car use camera and VESC to move.***

***If your depthai-ros installed in ROS2, you might need need to use ROS bridge.***

This is the part that we modified and implemented the most for the project.

The important thing of this part is TF tree.

Everything needs to be connected to make the car operating well, so we made the tf broadcasters and publishers to connect each frame.

For instance, in our project, our map is in ROS1, and all the car components are implementing in ROS2, so we could use ```odom``` in ROS2 to connect between ROS1 and ROS2. If the odom is not connected to the other car components, you will see that there is only wheels running on the map.

So this is why TF tree so important.

For ROS1, the command to see the tf tree: ```rosrun tf view_frames```

In this case, you can only use ```frames.gv``` to see the relationship between each frame.

For ROS2, the command to see the tf tree: ```ros2 run tf2_tools view_frames.py```

In this case, you can see both ```frames.gv``` and ```frames.pdf```, but you need to get the extension for the pdf viewer in vscode. 

TF tree should be similar as this:

![TF tree](https://github.com/y7chiu/Summer-2024-final-project-team-1/blob/main/images/screenshot_tf_tree.png)

## Future Development
***Need further research for this part***

### Costmaps / pointCloud Integration

Dynamically updating the map since we had already set the static map of ebu2.

- Local Costmap with pointcloud data
- Global Costmap

### Path-Planner

Using the path-planner, which using some path-finding algorithms to acieve this. For example, using Dijkstra's algorithm to find the greatest path to the person who need the car.

## Resource

- [Install from source from Luxonis Docs](https://docs.luxonis.com/software/ros/depthai-ros/build/)
- [Depthai-ros-driver](https://docs.luxonis.com/software/ros/depthai-ros/driver/)
- [ROS Documentation / ROS Wiki](https://docs.ros.org/)
- [AMCL](https://docs.nav2.org/configuration/packages/configuring-amcl.html)
- [AMCL Souce Code](https://github.com/ros-navigation/navigation2/tree/main/nav2_amcl)
- [ros-noetic-where-am-i-amcl](https://github.com/bmaxdk/ros-noetic-where-am-i-amcl)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



