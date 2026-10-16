"""Map motor neuron spikes onto fly movement in the game.

Sensory events go in, the connectome simulation runs, and spikes from
motor neurons are turned into movement commands.
"""
from connectome_loader import load_connectome
from lif_simulation import simulate
from sensory_mapping import events_to_inputs

# motor neuron -> movement it triggers
MOTOR_MAP = {
    "n2": "turn_left",
    "n4": "turn_right",
    "n5": "move_forward",
}


def spikes_to_actions(spikes):
    """Turn a list of spiking neurons into movement commands."""
    return [MOTOR_MAP[n] for n in spikes if n in MOTOR_MAP]


if __name__ == "__main__":
    g = load_connectome("data/sample_connectome.csv")
    events = {0: ["food_left"], 3: ["danger"]}
    for t, spikes in enumerate(simulate(g, events_to_inputs(events))):
        actions = spikes_to_actions(spikes)
        print(f"t={t}: {', '.join(actions) or '-'}")
