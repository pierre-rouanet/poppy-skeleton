# Skeleton for creating a new Poppy robot

This repository provides you a basic skeleton for creating a new robot that can be integrated within the rest of the Poppy ecosystem. By doing this you will:
* benefit from the existing tools such as automatically launching Snap! with your robot
* earn kudos for contributing and being part of the Poppy community!

## Setup your new Poppy robot

1. The first and most difficult step is actually to find a name for your robot. In our case, we will define a new creature named *My Cool Robot X42*.

2. Then you have to recreate the folders structure. Indeed, some files are "expected" to be at a specific location. For instance, the configuration will be searched in software/my_cool_robot_x42/configuration/my_cool_robot_x42.json by default. You can specify another path if you want but it just makes everything simpler if you try to stick to this convention. The simpler way to do that is to [fork the skeleton repository](https://github.com/pierre-rouanet/poppy-skeleton) and modify it.

3. Then, you have to rename folder/script according to your robot's name. And change a few lines in the Python module as well. You can do that manually, the steps 4 and 5 details everything needed. Or you can use the script inside our repository to do all those steps automatically. It can be run via: ```python rename-robot.py My Cool Robot X42```. Be aware that it will directly modify the files. If you choose the script method you can jump to the step 6.

4. There is a few places where you should replace *skeleton* by the new name:
    * rename the root folder: from *poppy_skeleton* to *my-cool-robot-x42*
    * rename the folder inside software: from *poppy_skeleton* to *my_cool_robot_x42* (use underscore for separating words)
    * rename the python module inside this folder from *poppy_skeleton.py* to *my_cool_robot_x42.py* (use underscore as well)
    * rename the configuration file (in *software/my_cool_robot_x42/configuration*) from *poppy_skeleton.json* to *my_cool_robot_x42.json* (still underscore)

5. Edit the python template files:
    * change in *\__init__.py* the import *from poppy_skeleton import PoppySkeleton* to *from my_cool_robot_x42 import MyCoolRobotX42* (note the first occurence used underscore because it is the convention for Python module while the second use camelcase as it is a Python class)
    * replace in *my_cool_robot_x42.py* the line *class PoppySkeleton(AbstractPoppyCreature):* by *class MyCoolRobotX42(AbstractPoppyCreature):*

## Going further

### Adding the hardware
### Kinematic chain and URDF file
### V-REP scene
