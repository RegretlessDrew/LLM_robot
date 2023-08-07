from setuptools import setup

package_name = 'digit'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('lib/'+ package_name,['digit/get_data.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zgq',
    maintainer_email='2226250900@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "data_pub = digit.data_pub:main"
        ],
    },
)
