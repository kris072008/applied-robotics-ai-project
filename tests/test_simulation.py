"""Unit tests for the firefly-brain pipeline."""
import unittest

from connectome_loader import load_connectome
from lif_simulation import simulate
from sensory_mapping import events_to_inputs
from motor_mapping import spikes_to_actions

DATA = "data/sample_connectome.csv"


class TestSensoryMapping(unittest.TestCase):
    def test_food_left_maps_to_n1(self):
        self.assertEqual(events_to_inputs({0: ["food_left"]}), {0: ["n1"]})

    def test_unknown_event_is_ignored(self):
        self.assertEqual(events_to_inputs({0: ["unknown"]}), {0: []})


class TestMotorMapping(unittest.TestCase):
    def test_motor_neurons_map_to_actions(self):
        self.assertEqual(spikes_to_actions(["n2", "n5"]),
                         ["turn_left", "move_forward"])

    def test_non_motor_neurons_are_ignored(self):
        self.assertEqual(spikes_to_actions(["n1", "n3"]), [])


class TestSimulation(unittest.TestCase):
    def test_full_pipeline_moves_fly_forward(self):
        g = load_connectome(DATA)
        events = {0: ["food_left"], 3: ["danger"]}
        spikes = simulate(g, events_to_inputs(events))
        self.assertIn("move_forward", spikes_to_actions(spikes[7]))


if __name__ == "__main__":
    unittest.main()
