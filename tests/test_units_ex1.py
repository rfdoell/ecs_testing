# -*- coding: utf-8 -*-
"""Provide true unit tests for the contents of example1."""
from unittest import mock

import pytest
from _pytest.monkeypatch import MonkeyPatch


# NOTE - Importing the module rather than individual classes to enable
# monkey-patching later
from ecs_testing_intro import example1

# Positive/Confirmation Testing

# These tests demonstrate the system under test behaves properly when used in
# the "happy path" or under normal circumstances.

# - Simple Data Structure Verification -


def test_com_init_no_err() -> None:
    """Verify instantiation of the center of mass component causes no errors."""
    example1.CenterOfMass2D(1.0, 1.0)


def test_com_init_x_pos() -> None:
    """Verify the instantiation of the X coordinate."""
    some_com = example1.CenterOfMass2D(1.0, 1.0)
    assert some_com.pos_x_m == 1.0


def test_com_init_y_pos() -> None:
    """Verify the instantiation of the Y coordinate."""
    some_com = example1.CenterOfMass2D(1.0, 1.0)
    assert some_com.pos_y_m == 1.0


def test_com_init_xy_pos() -> None:
    """Verify the instantiation of the X and Y coordinates."""
    some_com = example1.CenterOfMass2D(1.0, 1.0)
    assert some_com.pos_x_m == 1.0 and some_com.pos_y_m == 1.0


# - Processor Verification -
def test_processor_one_step_x(monkeypatch: MonkeyPatch) -> None:
    """Verify X coordinate updated correctly in one propagation step."""
    # Set up test parameters
    starting_x_pos = 0.0
    starting_x_vel = 1.0
    time_step = 1.0

    # Set up objects used in the test
    some_com = example1.CenterOfMass2D(starting_x_pos, 0.0)
    some_vel = example1.Velocity2D(starting_x_vel, 0.0)
    proc = example1.KinematicsProcessor(time_step)

    # Create a fake world retrieval system and patch it to get_components
    world_mock = mock.Mock()
    get_comps_mock = mock.Mock()
    get_comps_mock.return_value = [(None, (some_com, some_vel))]
    world_mock.get_components = get_comps_mock
    monkeypatch.setattr(proc, "world", world_mock)

    # Run the processing step
    proc.process()

    # Verify results
    assert starting_x_pos + time_step * starting_x_vel == some_com.pos_x_m


def test_processor_one_step_y(monkeypatch: MonkeyPatch) -> None:
    """Verify Y coordinate updated correctly in one propagation step."""
    # Set up test parameters
    starting_y_pos = 0.0
    starting_y_vel = 1.0
    time_step = 1.0

    # Set up objects used in the test
    some_com = example1.CenterOfMass2D(0.0, starting_y_pos)
    some_vel = example1.Velocity2D(0.0, starting_y_vel)
    proc = example1.KinematicsProcessor(time_step)

    # Create a fake world retrieval system and patch it to get_components
    world_mock = mock.Mock()
    get_comps_mock = mock.Mock()
    get_comps_mock.return_value = [(None, (some_com, some_vel))]
    world_mock.get_components = get_comps_mock
    monkeypatch.setattr(proc, "world", world_mock)

    # Run the processing step
    proc.process()

    # Verify results
    assert starting_y_pos + time_step * starting_y_vel == some_com.pos_y_m


def test_processor_one_step_xy(monkeypatch: MonkeyPatch) -> None:
    """Verify X and Y coordinates updated correctly in one propagation step."""
    # Set up test parameters
    starting_x_pos = 0.0
    starting_x_vel = 1.0
    starting_y_pos = 0.0
    starting_y_vel = 1.0
    time_step = 1.0

    # Set up objects used in the test
    some_com = example1.CenterOfMass2D(starting_x_pos, starting_y_pos)
    some_vel = example1.Velocity2D(starting_y_vel, starting_y_vel)
    proc = example1.KinematicsProcessor(time_step)

    # Create a fake world retrieval system and patch it to get_components
    world_mock = mock.Mock()
    get_comps_mock = mock.Mock()
    get_comps_mock.return_value = [(None, (some_com, some_vel))]
    world_mock.get_components = get_comps_mock
    monkeypatch.setattr(proc, "world", world_mock)

    # Run the processing step
    proc.process()

    # Verify results
    expected_x_pos = starting_x_pos + time_step * starting_x_vel
    expected_y_pos = starting_y_pos + time_step * starting_y_vel
    assert (
        expected_x_pos == some_com.pos_x_m
        and expected_y_pos == some_com.pos_y_m
    )


# Negative/Error Confirmation Testing

# These tests verify failure modes of the system, i.e., that they fail in an
# expected and predictable way.

# - Simple Data Structure Verification -


def test_com_init_x_int_err() -> None:
    """Verify instantiating COM with an int for X pos raises an error."""
    with pytest.raises(TypeError):
        example1.CenterOfMass2D(1, 1.0)


def test_com_init_y_int_err() -> None:
    """Verify instantiating COM with an int for Y pos raises an error."""
    with pytest.raises(TypeError):
        example1.CenterOfMass2D(1.0, 1)


def test_com_init_xy_int_err() -> None:
    """Verify instantiating COM with an int for X and Y pos raises an error."""
    with pytest.raises(TypeError):
        example1.CenterOfMass2D(1, 1)
