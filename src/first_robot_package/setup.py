from setuptools import find_packages, setup

package_name = 'first_robot_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	('share/' + package_name + '/launch', 
	   ['launch/robot_system.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='afini',
    maintainer_email='allaputaafini@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'first_node = first_robot_package.first_node:main',
		'second_node = first_robot_package.second_node:main',
		'status_listener = first_robot_package.status_listener:main',
		'battery_level = first_robot_package.battery_status:main',
		'add_service = first_robot_package.add_service:main',
        ],
    },
)
