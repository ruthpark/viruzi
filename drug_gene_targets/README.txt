api_dgidb.py is used to make the api call to the dgi database.

map_genes.py calls api_dgidb.py with a list of genes that are known to be affected by CD & UC, and produces genes_to_drugs.txt

mapping_output.txt is the mapping of genes that are affected by CD & UC to drugs that target those genes and in what way etc

intermediate.py gets genes_to_drugs and adds cols for manual inputting.

drugs_used.txt is mapping_output.txt, but indicates which drugs are currently being prescribed for UC/CD and which aren't.

