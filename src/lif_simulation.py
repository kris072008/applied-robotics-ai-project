"""Leaky integrate-and-fire (LIF) simulation over a connectome graph."""
from connectome_loader import load_connectome

THRESHOLD = 1.0   # membrane potential needed to spike
LEAK = 0.9        # fraction of potential kept each step
SCALE = 0.3       # synapse weight -> input current


def simulate(graph, inputs, steps=10):
    neurons = set(graph) | {n for t in graph.values() for n in t}
    v = {n: 0.0 for n in neurons}
    history = []
    for t in range(steps):
        current = {n: 0.0 for n in neurons}
        for n in inputs.get(t, []):
            current[n] += THRESHOLD          # external stimulus
        spiked = [n for n in neurons if v[n] >= THRESHOLD]
        for pre in spiked:
            v[pre] = 0.0                     # reset after spike
            for post, w in graph.get(pre, {}).items():
                current[post] += w * SCALE
        for n in neurons:
            v[n] = v[n] * LEAK + current[n]
        history.append(sorted(spiked))
    return history


if __name__ == "__main__":
    g = load_connectome("data/sample_connectome.csv")
    for t, spikes in enumerate(simulate(g, {0: ["n1"]})):
        print(f"t={t}: {spikes or '-'}")
