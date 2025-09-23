# Robot2025 Simulation

<img width="1901" height="1016" alt="image" src="https://github.com/user-attachments/assets/8e672207-ae07-4513-ab95-fcb7849a8661" />

---








This package provides a simple differential drive robot simulated in **Gazebo (Ignition)** with teleoperation using `teleop_twist_keyboard`.

## Prerequisites

Make sure the following are installed on **Ubuntu 22.04 with ROS 2 Humble**:

-   Ignition Gazebo ROS 2 bridge:
    
    ```bash
    sudo apt install ros-humble-ros-gz
    
    ```
    
-   ros2_control and diff drive controller:
    
    ```bash
    sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers
    
    ```
    
-   Teleoperation package:
    
    ```bash
    sudo apt install ros-humble-teleop-twist-keyboard
    
    ```

    
##  Workspace Setup

Create a new ROS 2 workspace and clone this package:

```bash
# Create a workspace
mkdir -p ~/baseline_robot_ws/src
cd ~/baseline_robot_ws/src

# Clone your package (replace URL with your repo)
git clone https://github.com/codewithlennylen/robot2025_sim

# Go back to workspace root
cd ~/baseline_robot_ws

```

##  Build

Build the workspace with `colcon`:

```bash
colcon build --symlink-install

```

Source the workspace:

```bash
source install/setup.bash

```

## Run Simulation

Launch Gazebo with the robot and maze world:

```bash
ros2 launch robot2025_sim robot2025_sim.launch.py

```

This will:

-   Start Gazebo
    
-   Spawn the robot in the maze
    
-   Load ros2_control
    

##  Teleoperate the Robot

Open a **new terminal** (don’t forget to source your workspace again):

```bash
source ~/baseline_robot_ws/install/setup.bash

```

Run teleop with remapping to the diff drive controller:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args -r /cmd_vel:=/diff_drive_base/cmd_vel_unstamped

```

    
