import networkx as nx
import matplotlib.pyplot as plt

from nodes import Node


def map_label_to_color(label):
    color_map = {'el': '#ff0000', 'i': '#ffa500', 'e': '#5e90d7'}
    # get whats under label or default value
    return color_map.get(label.lower(), '#c1c1c1')


def map_pos_to_visual_pos(pos, layer):
    x_size = 10
    y_size = 10
    y_offset = 6

    # version with increasing x size
    # if layer >= 3:
    #     x_size *= 2**(layer-2)

    return (x_size * pos[0], -(y_size * pos[1] + layer * (y_size+y_offset)))


def get_layer_subgraph(graph: nx.Graph, layer: int):
    layer_nodes = []
    for node in graph.nodes(data=True):
        if node[1]['layer'] == layer:
            layer_nodes.append(node[0])
    return graph.subgraph(layer_nodes)


def relabel_labels_with_duplicated_pos(labels, positions):
    labels2 = labels.copy()
    pos_label_dict = {}
    for id, pos in positions.items():
        if pos in pos_label_dict:
            pos_label_dict[pos] += labels2[id]
        else:
            pos_label_dict[pos] = labels2[id]

    for id, pos in positions.items():
        labels2[id] = pos_label_dict[pos]

    return labels2

def draw_graph(graph: nx.Graph, layer=None, plot=True):
    if layer is not None:
        graph = get_layer_subgraph(graph, layer)

    labels = nx.get_node_attributes(graph, 'label')
    node_colors = list(map(map_label_to_color, labels.values()))

    visual_pos = nx.get_node_attributes(graph, 'pos')
    if layer is None:
        visual_pos = {node: map_pos_to_visual_pos(
            data['pos'], data['layer']) for node, data in graph.nodes(data=True)}

    labels = relabel_labels_with_duplicated_pos(labels, visual_pos)

    # add node id to label
    # for k, v in labels.items():
    #     labels[k] = f'{v}-{k}'

    nx.draw(graph, pos=visual_pos,
            labels=labels, font_size=12,
            node_size=300, node_color=node_colors)

    if plot:
        plt.show()

def draw_dungeon(G: nx.Graph, label_tags=['label'] ,plot=True):
    
    
    
    # Get a reproducible layout and create figure
    pos = nx.kamada_kawai_layout(G)
    # if 'env_biome' in label_tags:
    #     pos = nx.bipartite_layout(G, [node for node,data in G.nodes.data() if 'env_biome' in data and data['env_biome'] == 'caves'])
    fig, ax = plt.subplots(figsize=(12, 9))
    
    # Note: the min_source/target_margin kwargs only work with FancyArrowPatch objects.
    # Force the use of FancyArrowPatch for edge drawing by setting `arrows=True`,
    # but suppress arrowheads with `arrowstyle="-"`
    
    # Transform from data coordinates (scaled between xlim and ylim) to display coordinates
    tr_figure = ax.transData.transform
    # Transform from display to figure coordinates
    tr_axes = fig.transFigure.inverted().transform
    # Select the size of the image (relative to the X axis)
    icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
    icon_center = icon_size / 2.0

    nx.draw_networkx_edges(
        G,
        pos=pos,
        edge_color="gray",
        ax=ax,
        arrows=True,
        arrowstyle="-|>",
        # connectionstyle='angle',
        min_source_margin=5,
        min_target_margin=5,
    )

    # Define a function to offset the position of the labels
    def offset_pos(pos, offset=0.04*len(label_tags)):
        new_pos = {}
        for k, v in pos.items():
            new_pos[k] = (v[0], v[1] - offset)
        return new_pos

    # Draw the labels with an offset position
    nx.draw_networkx_labels(G,
                            labels={node: Node().print_arguments(G, node, label_tags) for node in G.nodes},
                            pos=offset_pos(pos),
                            ax=ax, font_size=12)
    nx.draw_networkx_nodes(G.subgraph(list(node for node,data in G.nodes.data() if 'image' not in data)), pos=pos, ax=ax, node_size=150, node_color='#c1c1c1')
                           
    # Add the respective image to each node
    for n in G.nodes:
        xf, yf = tr_figure(pos[n])
        xa, ya = tr_axes((xf, yf))
        # get overlapped axes and plot icon
        a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
        if "image" in G.nodes[n]:
            a.imshow(G.nodes[n]["image"])
        a.axis("off")
        
    if plot:
        plt.show()