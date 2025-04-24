import math
import matplotlib.pyplot as plt
from node import Distance


class Path:
   def __init__(self):
       self.nodes = []
       self.costs = []
       self.total_cost = 0.0


def AddNode(G, P, name):
   i = 0
   encontrado = False
   while i < len(G.nodes) and not encontrado:
       if G.nodes[i].name == name:
           encontrado = True
       else:
           i = i + 1
   if not encontrado:
       print("not")
       return False
   else:
       if P.nodes == []:
           P.nodes.append(G.nodes[i])
           P.costs.append(0)
           P.total_cost = 0.0
           return True
       else:
           j = 0
           encontrado = False
           while j < len(P.nodes) and not encontrado:
               if P.nodes[j].name == name:
                   encontrado = True
               j = j + 1
           if encontrado:
               return False
           else:
               encontrado = False
               n = 0
               while n < len(P.nodes[-1].neighbors) and not encontrado:
                   if name == P.nodes[-1].neighbors[n].name:
                       P.nodes.append(G.nodes[i])
                       dist = Distance(P.nodes[-2], P.nodes[-1])
                       P.costs.append(dist)
                       P.total_cost += dist
                       encontrado = True
                       return True
                   else:
                       n = n + 1
               return False


def ContainsNode(P, name):
   i = 0
   encontrado = False
   while i < len(P.nodes) and not encontrado:
       if P.nodes[i].name == name:
           encontrado = True
       else:
           i = i + 1
   if encontrado:
       print(f"The Node {name} belongs to the path")
       return False
   else:
       print(f"The Node {name} does not belongs to the path")
       return True


def CostToNode(P, name):
   i = 0
   cost = 0.0
   while i < len(P.nodes):
       if P.nodes[i].name == name:
           j = 0
           while j < i:
               cost += Distance(P.nodes[j], P.nodes[j + 1])
               j = j + 1
           return cost
       i = i + 1
   else:
       return -1




def PlotPath(G, P):
   # Plot all nodes in the graph
   for node in G.nodes:
       plt.plot(node.x, node.y, marker='o', linestyle='', color='black', markersize=5)
       plt.text(node.x, node.y, node.name, horizontalalignment='left', verticalalignment='bottom', color='red')


   # Plot the path - highlighting the connections between nodes in the path
   i = 0
   while i < len(P.nodes) - 1:
       origin_node = P.nodes[i]
       destination_node = P.nodes[i + 1]


       # Draw a line between consecutive nodes in the path
       plt.plot([origin_node.x, destination_node.x],
                [origin_node.y, destination_node.y], 'blue', linewidth=2)


       # Add an arrow to show direction
       plt.arrow(origin_node.x, origin_node.y,
                 (destination_node.x - origin_node.x) * 0.8,  # Make arrow a bit shorter than full line
                 (destination_node.y - origin_node.y) * 0.8,
                 head_width=0.3, head_length=0.3, fc='blue', ec='blue', length_includes_head=True)


       # Add the cost label at the midpoint of the segment
       midpoint_x = (origin_node.x + destination_node.x) / 2
       midpoint_y = (origin_node.y + destination_node.y) / 2


       # Find the correct segment to get its cost
       for segment in G.segments:
           if ((segment.origin.name == origin_node.name and segment.destination.name == destination_node.name) or
                   (segment.destination.name == origin_node.name and segment.origin.name == destination_node.name)):
               plt.text(midpoint_x, midpoint_y, f"{round(segment.cost, 2)}",
                        backgroundcolor='white', fontsize=9)
               break


       i = i + 1


   # Highlight the path nodes with a different color
   for node in P.nodes:
       plt.plot(node.x, node.y, marker='o', linestyle='', color='red', markersize=7)


   plt.xlabel('X')
   plt.ylabel('Y')
   plt.title("Path visualization")
   plt.grid(True)
   plt.show()
