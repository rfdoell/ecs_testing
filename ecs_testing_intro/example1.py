"""Demonstrate basic Entity/Component/System usage."""
import attr
import esper

from attr import validators

# These are data classes or a simple processor; they should have few/no
# methods:
# pylint: disable=too-few-public-methods


@attr.s
class CenterOfMass2D:
    """
    Represent an object's center of mass in 2D Euclidean geometry.

    This class is used to represent the center of a rigid object, rather than
    any edges or bounding-box artifacts that may come from drawing or other
    representations.

    .. Note:: All distances are in meters.

    :param pos_x_m: The "x" coordinate in meters
    :param pos_y_m: The "y" coordinate in meters
    """

    pos_x_m: float = attr.ib(validator=validators.instance_of(float))
    pos_y_m: float = attr.ib(validator=validators.instance_of(float))


@attr.s
class Velocity2D:
    """
    Represent an object's velocity in 2D Euclidean geometry.

    This class represents the "group velocity" of an object - that that a
    single entity would have if taken in aggregate.

    .. Note:: All velocities are in meters per second.

    :param vel_x_m_s: The "x" velocity in meters/second
    :param vel_y_m_s: The "y" velocity in meters/second
    """

    vel_x_m_s: float = attr.ib(validator=validators.instance_of(float))
    vel_y_m_s: float = attr.ib(validator=validators.instance_of(float))


# There is no available type stub for Processor, so mypy thinks it cannot be
# subclassed
class KinematicsProcessor(esper.Processor):  # type: ignore
    """
    Implement a simple stepwise approximation for displacement propagation.

    This processor will update all entities with centers of mass based on::

       -->     -->          -->
       x_1 =  x_0  +  dt  *  v

    where dt is a time quantity in seconds and passed in on creation.

    :param dt_sec: The time step to use for propagation, in seconds
    """

    def __init__(self, dt_sec: float):
        """Initialize the object."""
        # NOTE: The Esper documentation calls out the lack of need for calling
        # `super` for Processors
        self._dt_sec = dt_sec

    # This is compliant with the esper documentation; ignoring the lint
    def process(self) -> None:  # pylint: disable=arguments-differ
        """Execute linear interpolation for entities with centers of mass."""
        for _, (com, vel) in self.world.get_components(
            CenterOfMass2D, Velocity2D
        ):
            com.pos_x_m += self._dt_sec * vel.vel_x_m_s
            com.pos_y_m += self._dt_sec * vel.vel_y_m_s
