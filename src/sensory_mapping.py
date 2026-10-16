"""Map game inputs (what the fly senses) onto sensory neurons.

Each game event stimulates a set of sensory neurons in the connectome,
which then drives the spiking simulation.
"""
from connectome_loader import load_connectome
from lif_simulation import simulate

# game event -> sensory neurons it stimulates
SENSORY_MAP = {
    "food_left":   ["n1"],
    "food_right":  ["n3"],
    "danger":      ["n1", "n3"],
}


def events_to_inputs(events):
    """Turn {time_step: [event, ...]} into {time_step: [neuron, ...]}."""
    inputs = {}
    for t, evs in events.items():
        neurons = []
        for e in evs:
            neurons.extend(SENSORY_MAP.get(e, []))
        inputs[t] = neurons
    return inputs


if __name__ == "__main__":
    g = load_connectome("data/sample_connectome.csv")
    events = {0: ["food_left"], 3: ["danger"]}
    for t, spikes in enumerate(simulate(g, events_to_inputs(events))):
        print(f"t={t}: {spikes or '-'}")
