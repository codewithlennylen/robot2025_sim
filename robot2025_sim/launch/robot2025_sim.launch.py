# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch_ros.actions import Node
# from ament_index_python.packages import get_package_share_directory
# import os


# def generate_launch_description():
#     pkg_share = get_package_share_directory('robot2025_sim')

#     urdf_file = os.path.join(pkg_share, 'urdf', 'robot2025_sim.urdf.xacro')
#     world_file = os.path.join(pkg_share, 'worlds', 'maze.sdf')

#     gz_launch = os.path.join(
#         get_package_share_directory('ros_gz_sim'),
#         'launch',
#         'gz_sim.launch.py'
#     )

#     return LaunchDescription([
#         # Start Gazebo
#         IncludeLaunchDescription(
#             PythonLaunchDescriptionSource(gz_launch),
#             launch_arguments={'gz_args': f'-r {world_file}'}.items(),
#         ),

#         # Spawn robot into Gazebo
#         Node(
#             package='ros_gz_sim',
#             executable='create',
#             arguments=[
#                 '-name', 'robot2025_sim',
#                 '-topic', 'robot_description',
#                 '-x', '0', '-y', '0', '-z', '0.1'
#             ],
#             output='screen'
#         ),

#         # Publish robot description to /robot_description
#         Node(
#             package='robot_state_publisher',
#             executable='robot_state_publisher',
#             arguments=[urdf_file],
#             output='screen'
#         ),
#     ])


########################################################################################


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('robot2025_sim')

    urdf_file = os.path.join(pkg_share, 'urdf', 'robot2025_sim.urdf.xacro')
    world_file = os.path.join(pkg_share, 'worlds', 'maze.sdf')

    controller_params = os.path.join(
        pkg_share, 'config', 'diff_drive_controller.yaml')

    gz_launch = os.path.join(
        get_package_share_directory('ros_gz_sim'),
        'launch',
        'gz_sim.launch.py'
    )

    bridge_launch = os.path.join(pkg_share, 'launch', 'bridge.launch.py')

    return LaunchDescription([

        # Start Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch),
            launch_arguments={'gz_args': f'-r {world_file}'}.items(),
        ),

        # # Robot State Publisher
        # Node(
        #     package='robot_state_publisher',
        #     executable='robot_state_publisher',
        #     output='screen',
        #     parameters=[{'robot_description': open(urdf).read()}]
        # ),
        # Publish robot description to /robot_description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=[urdf_file],
            output='screen'
        ),

        # Spawn robot into Gazebo
        # Node(
        #     package='ros_gz_sim',
        #     executable='create',
        #     arguments=['-file', urdf, '-name', 'robot2025_sim'],
        #     output='screen'
        # ),

        # Spawn robot into Gazebo
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-name', 'robot2025_sim',
                '-topic', 'robot_description',
                '-x', '0', '-y', '0', '-z', '0.1'
            ],
            output='screen'
        ),
        # Node(
        #     package='ros_gz_sim',
        #     executable='create',
        #     arguments=['-file', urdf, '-name', 'robot2025_sim'],
        #     output='screen',
        #     parameters=[controller_params]
        # ),




        # Start ROS-Gazebo bridge
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(bridge_launch)
        ),

    ])
