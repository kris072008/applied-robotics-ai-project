"""Load the FlyWire Drosophila connectome into a simple graph.

Expects a CSV of synapse connections with columns:
pre_id, post_id, weight
"""
import csv
from collections import defaultdict


def load_connectome(path):
    """Return {pre_neuron: {post_neuron: weight}} from a CSV file."""
    graph = defaultdict(dict)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            graph[row["pre_id"]][row["post_id"]] = float(row["weight"])
    return graph


def summary(graph):
    neurons = set(graph) | {n for targets in graph.values() for n in targets}
    synapses = sum(len(t) for t in graph.values())
    return f"{len(neurons)} neurons, {synapses} connections"


if __name__ == "__main__":
    g = load_connectome("data/sample_connectome.csv")
    print(summary(g))
