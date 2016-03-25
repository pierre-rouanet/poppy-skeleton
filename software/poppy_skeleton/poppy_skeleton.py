from poppy.creatures import AbstractPoppyCreature


class PoppySkeleton(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        # Here is where you can customize your robot
        # for instance, you can:
        #     * setup positions
        #     * define kinematic chains
        #     * attach primitives
        pass
