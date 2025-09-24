from setuptools import setup
import os
from glob import glob

package_name = 'robot2025_sim'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('robot2025_sim/launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lenny',
    maintainer_email='you@example.com',
    description='Simple robot and gazebo sim (Python package)',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [],
    },
)



