import matplotlib.pyplot as plt
import networkx as nx
import PIL
from nodes import Lock, LockState, OpenMode, Importance, LogicGate, Key, KeyType, Reusability,Access

# Image URLs for graph nodes
icons = {
    "router": "img/key.drawio.png",
    "switch": "img/lock.drawio.png",
    "PC": "img/treasure.drawio.png",
}

# Load images
images = {k: PIL.Image.open(fname) for k, fname in icons.items()}

# Generate the computer network graph
G = nx.DiGraph()

G.add_node("router", image=images["router"])
for i in range(1, 4):
    G.add_node(f"switch_{i}", image=images["switch"])
    for j in range(1, 4):
        G.add_node("PC_" + str(i) + "_" + str(j), image=images["PC"])

G.add_edge("router", "switch_1")
G.add_edge("router", "switch_2")
G.add_edge("router", "switch_3")
for u in range(1, 4):
    for v in range(1, 4):
        G.add_edge("switch_" + str(u), "PC_" + str(u) + "_" + str(v))


# Get a reproducible layout and create figure
pos = nx.spring_layout(G, seed=1)
fig, ax = plt.subplots(figsize=(9, 6))

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
    connectionstyle='angle',
    min_source_margin=15,
    min_target_margin=15,
)

# Define a function to offset the position of the labels
def offset_pos(pos, offset=0.125):
    new_pos = {}
    for k, v in pos.items():
        new_pos[k] = (v[0], v[1] - offset)
    return new_pos

# Draw the labels with an offset position
nx.draw_networkx_labels(G, pos=offset_pos(pos), ax=ax, font_size=12)
# Add the respective image to each node
for n in G.nodes:
    xf, yf = tr_figure(pos[n])
    xa, ya = tr_axes((xf, yf))
    # get overlapped axes and plot icon
    a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
    a.imshow(G.nodes[n]["image"] if "image" in G.nodes[n] else images["PC"])
    a.axis("off")
    
plt.show()