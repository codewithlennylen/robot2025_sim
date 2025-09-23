from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='online_async_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{'use_sim_time': True}]
        )
    ])
