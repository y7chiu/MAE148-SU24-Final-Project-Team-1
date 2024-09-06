# Autonomous Car: Localization and Obstacle Detection
![<img width="661" alt="截圖 2024-09-06 11 49 20" src="https://github.com/user-attachments/assets/2be48b3e-bd5f-4d92-b083-6c12f176b6be">](https://jacobsschool.ucsd.edu/sites/default/files/UCSDLogo_JSOE_BlueGold_0_0.png)

# Table of Contents
- [Project Idea](#project-idea)
- [Instructions for Our Project](#instructions-for-our-project)
- [Future Development](#future-development)
- [Resource](#resource)

## Team 1 - Summer2024
Chiu, Yi-Chan - y7chiu@ucsd.edu

Solano, Josue - 

Lin, Isaac - 

Joshi, Pratham -

## Project Idea

The project applies to the real world, such as hospital emergency, Uber taxi service, finding missing people when signal is mssing, ...,etc.

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

## Instructions for Our Project

### SLAM

### Depthai-ROS Installation

### DepthCloud Obstacle Detection

### Odometry Localization

### Combination between Depth-Camera and ROS.

## Future Development

### Costmap

### Path-Planner

### pointCloud Intergration

## Resource



