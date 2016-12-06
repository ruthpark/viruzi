import os



def read_file():
	str = ""
	with open("../networks/mapping.txt") as genes:
		lines = [line.rstrip('\n') for line in genes]
		for line in lines:
			genes = line.split("\t")
			str += genes[0] + ","
	return str[:-1]


cmd = "./api_dgidb.py --genes='%s' >> ./genes_to_drugs.txt" %(read_file())


os.system(cmd)