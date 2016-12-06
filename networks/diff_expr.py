import sys
import networkx as nx

def read_file(fname):
	f = open(fname, 'r')
	genes = []

	for line in f:
		line_list = [elt[1:-1] for elt in line.strip().split('\t')]
		genes.append(expressed_gene(line_list))

	return genes[1:]

def write_genes(gene_list, fname):
	f = open(fname, 'w')

	for gene in gene_list:
		if float(gene.Pval) < 0.05 and abs(float(gene.logFC)) >= 1:
			f.write(gene.geneSymbol + '\n')

	f.close()


class expressed_gene():
	def __init__(self, data):
		self.data = data
		self.ID = data[0]
		self.adjPval = data[1]
		self.Pval = data[2]
		self.t = data[3]
		self.B = data[4]
		self.logFC = data[5]
		self.geneSymbol = data[6]
		self.geneTitle = data[7]

def main():
	fname = 'UC_expression.txt'
	fname_write = 'UC_diff_expr_genes.txt'
	gene_list = read_file(fname)
	write_genes(gene_list, fname_write)


if __name__ == '__main__':
	main()