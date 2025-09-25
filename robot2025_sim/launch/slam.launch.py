# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package='slam_toolbox',
#             executable='online_async_node',
#             name='slam_toolbox',
#             output='screen',
#             parameters=[{'use_sim_time': True}]
#         )
#     ])



from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # Run SLAM Toolbox online sync mode
        Node(
            package="slam_toolbox",
            executable="sync_slam_toolbox_node",
            name="slam_toolbox",
            output="screen",
            parameters=["/home/lenny/Documents/GitHub/rdj/baseline_robot_ws/src/robot2025_sim/config/slam_params.yaml"],
        )
    ])
