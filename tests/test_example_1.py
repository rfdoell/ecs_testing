"""Provide basic tests for the first example module."""
import esper

from ecs_testing_intro import example1


def test_one_step_x() -> None:
    """Test that a single propagation step is successful in X."""
    # Create a world
    world = esper.World()
    some_entity = world.create_entity()

    # Create an object at the origin
    world.add_component(some_entity, example1.CenterOfMass2D(0.0, 0.0))

    # Create an object with a velocity of 1 m/s "to the right"
    world.add_component(some_entity, example1.Velocity2D(1.0, 0.0))

    # For this test, set the time between ticks to be one second:
    kinematics_proc = example1.KinematicsProcessor(1.0)

    # Add the processor to the world
    world.add_processor(kinematics_proc)

    # Execute one tick:
    world.process()

    # Make sure the difference in position is correct. Using the dreaded "=="
    # for floats.
    com_pos = world.component_for_entity(some_entity, example1.CenterOfMass2D)

    assert com_pos.pos_x_m == 1.0
