## Pregunta #4 

cut -d ","  -f5,18,21 sites.csv > pdb.csv 

cut -d "," -f1 pdb.csv | tail -n +2 | sort -u | wc -l 
cut -d "," -f2 pdb.csv | tail -n +2 | sort -u | wc -l
cut -d "," -f3 pdb.csv | tail -n +2 | sort -u | wc -l