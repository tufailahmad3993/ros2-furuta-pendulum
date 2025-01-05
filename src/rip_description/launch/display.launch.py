from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():
    # Get the path of the urdf file 
    urdf_path = os.path.join(get_package_share_path('rip_description'), 'urdf', 'rotary_pend.urdf.xacro')

    # Robot State Publisher Node
    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)
    
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description}]
    )
    
    # Joint State Publisher GUI Node
    robot_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )
    
    # RViz2 Node
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen"
    )

    return LaunchDescription([
        robot_state_publisher_node,
        robot_state_publisher_gui_node,
        rviz2_node
    ])
