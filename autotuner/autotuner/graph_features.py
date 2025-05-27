# features_graph.py
# Enhanced feature extractor for graph-level ML model

import numpy as np
import networkx as nx

def extract_graph_features(graph: nx.Graph):
    """
    Extracts graph-level features to help ML models predict the best graph algorithm.
    """

    features = []

    # === Basic size and connectivity ===
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    is_directed = graph.is_directed()
    is_connected = nx.is_weakly_connected(graph) if is_directed else nx.is_connected(graph)

    features.extend([
        num_nodes,
        num_edges,
        is_connected,
        is_directed
    ])

    # === Density ===
    features.append(nx.density(graph))

    # === Degree statistics ===
    degrees = [deg for _, deg in graph.degree()]
    features.extend([
        np.mean(degrees),
        np.std(degrees),
        np.max(degrees),
        np.min(degrees)
    ])

    # === In-degree / Out-degree statistics for directed graphs ===
    if is_directed:
        in_degrees = [deg for _, deg in graph.in_degree()]
        out_degrees = [deg for _, deg in graph.out_degree()]
        features.extend([
            np.mean(in_degrees), np.std(in_degrees),
            np.mean(out_degrees), np.std(out_degrees)
        ])
    else:
        features.extend([0, 0, 0, 0])

    # === Sources and sinks (only meaningful in directed graphs) ===
    if is_directed:
        in_deg = dict(graph.in_degree())
        out_deg = dict(graph.out_degree())
        num_sources = sum(1 for n in graph.nodes if in_deg[n] == 0 and out_deg[n] > 0)
        num_sinks = sum(1 for n in graph.nodes if out_deg[n] == 0 and in_deg[n] > 0)
        features.extend([num_sources, num_sinks])
    else:
        features.extend([0, 0])

    # === Clustering ===
    features.append(nx.average_clustering(graph.to_undirected()))

    # === Path-based metrics ===
    if is_connected:
        ug = graph.to_undirected()
        features.append(nx.diameter(ug))
        features.append(nx.average_shortest_path_length(ug))
    else:
        features.extend([-1, -1])

    # === Cycles ===
    if is_directed:
        features.append(nx.is_directed_acyclic_graph(graph))
        features.append(len(list(nx.simple_cycles(graph))))
    else:
        features.append(nx.is_forest(graph))
        features.append(len(nx.cycle_basis(graph)))

    # === Edge weight statistics ===
    if nx.is_weighted(graph):
        weights = [d['weight'] for _, _, d in graph.edges(data=True)]
        features.extend([
            np.mean(weights),
            np.std(weights),
            np.min(weights),
            np.max(weights),
            any(w < 0 for w in weights)  # has negative weights
        ])
    else:
        features.extend([0, 0, 0, 0, 0])

    # === Centrality measures ===
    betweenness = list(nx.betweenness_centrality(graph).values())
    closeness = list(nx.closeness_centrality(graph).values())
    features.extend([
        np.mean(betweenness), np.std(betweenness),
        np.mean(closeness), np.std(closeness)
    ])

    # === Connectivity components ===
    if is_directed:
        features.extend([
            nx.is_strongly_connected(graph),
            nx.number_strongly_connected_components(graph),
            nx.number_weakly_connected_components(graph)
        ])
    else:
        features.extend([
            0,
            nx.number_connected_components(graph),
            0
        ])

    # === Articulation points / bridges ===
    ug = graph.to_undirected()
    features.append(len(list(nx.articulation_points(ug))))
    features.append(len(list(nx.bridges(ug))))

    return features