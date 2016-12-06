import networkx as nx
import matplotlib.pyplot as plt

class PPI():
	def __init__(self, data):

		self.edge = (data[1], data[2])
		self.id = data[0]

def get_VE_from_fname(fname, mappings):
	f = open(fname,'r')
	V = set([])
	interactions = []

	for line in f:
		line_list = line.strip().split('\t')
		if len(line_list) < 3:
			continue
		# print line_list
		ppi = PPI(line_list)
		if ppi.edge[0] != 'a_alias' and ppi.edge[1] != 'a_alias':
			if mappings.has_key(ppi.edge[0]) or mappings.has_key(ppi.edge[1]):
				V.add(ppi.edge[0])
				V.add(ppi.edge[1])
				interactions.append(ppi)

	return V, interactions

def build_graph(V, interactions, colors):
	G = nx.Graph()
	G.add_nodes_from(list(V))

	edge_list = [(elt.edge[0], elt.edge[1], {'id': elt.id}) for elt in interactions]
	G.add_edges_from(edge_list)

	# nx.draw(G)
	nx.draw(G,pos=nx.spring_layout(G), node_color=colors, node_size=30, labels=None)
	# nx.draw_networkx_labels(G,pos=nx.spring_layout(G))
	plt.savefig('UC_test_figure.png')

def get_mapping_from_file(fname):
	f = open(fname, 'r')
	d = {}

	for line in f:
		line_list = line.strip().split('\t')
		d[line_list[0]] = line_list[1]

	return d

def main():
	fname_2 = 'UC_mappings.txt'
	uniprotkb_mappings = get_mapping_from_file(fname_2)

	fname = 'UC_mitab_lite.txt'
	V, interactions = get_VE_from_fname(fname, uniprotkb_mappings)
	
	colors = []
	V_list = list(V)
	count = 0
	for elt in V_list:
		if uniprotkb_mappings.has_key(elt):
			colors.append('r')
			count += 1
		else:
			colors.append('b')
	print len(V_list)
	print len(uniprotkb_mappings.keys())
	print count
	build_graph(V_list, interactions, colors)


if __name__ == '__main__':
	main()