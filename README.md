# Autonomous Car: ROS, Localization and Obstacle Detection
[![<img width="450" alt="截圖 2024-09-06 11 49 20" src="https://github.com/user-attachments/assets/2be48b3e-bd5f-4d92-b083-6c12f176b6be">](https://jacobsschool.ucsd.edu/sites/default/files/UCSDLogo_JSOE_BlueGold_0_0.png)](https://jacobsschool.ucsd.edu/)

# Table of Contents
- [Members](#members)
- [Project Idea - Foresight](#project-idea---foresight)
- [Instructions for Our Project - What we have done](#instructions-for-our-project---what-we-have-done)
  - [SLAM](#slam)
  - [Depthai-ROS Installation](#depthai-ros-installation)
  - [DepthCloud Obstacle Detection](#depthcloud-obstacle-detection)
  - [Odometry Localization](#odometry-localization)
  - [Combination between Depth-Camera and ROS](#combination-between-depth-camera-and-ros)
- [Future Development](#future-development)
  - [Costmap](#costmap)
  - [Path-Planner](#path-planner)
  - [PointCloud Integration](#pointcloud-integration)
- [Resource](#resource)
- [License](#license)

## Team 1 - Summer2024

## Members

Chiu, Yi-Chan - y7chiu@ucsd.edu

Solano, Josue - 

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

### Depthai-ROS Installation

### DepthCloud Obstacle Detection

### Odometry Localization

### Combination between Depth-Camera and ROS

## Future Development

### Costmap

### Path-Planner

### pointCloud Integration

## Resource

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



