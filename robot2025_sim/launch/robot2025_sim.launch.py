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
        './src/robot2025_sim/config', 'diff_drive_controller.yaml')
    # controller_params = os.path.join(
    #     pkg_share, 'config', 'diff_drive_controller.yaml')

    gz_launch = os.path.join(
        get_package_share_directory('ros_gz_sim'),
        'launch',
        'gz_sim.launch.py'
    )

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
            output='screen',
            parameters=[os.path.join(pkg_share, 'config', 'ros2_control.yaml')]
            # parameters=[controller_params]
        ),
        # Node(
        #     package='ros_gz_sim',
        #     executable='create',
        #     arguments=['-file', urdf, '-name', 'robot2025_sim'],
        #     output='screen',
        #     parameters=[controller_params]
        # ),


        # NOTE: Gz runs this automatically
        # ros2_control controller manager
        # Node(
        #     package='controller_manager',
        #     executable='ros2_control_node',
        #     parameters=[controller_params],
        #     output='screen'
        # ),

        # Load controller params into Gazebo's controller_manager
        # Spawn diff drive controller
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['diff_drive_base'],
        ),


        # Node(
        #     package='controller_manager',
        #     executable='spawner',
        #     arguments=['diff_cont'],
        #     output='screen'
        # ),
        # Node(
        #     package='controller_manager',
        #     executable='spawner',
        #     arguments=['diff_cont', '--param-file', controller_params],
        #     output='screen'
        # ),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster",
                       "--controller-manager", "/controller_manager"],
            output="screen"
        ),


    ])
