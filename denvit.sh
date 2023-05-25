## Pregunta #2 

for archivo in *.csv; do 
	echo "Numero de filas del archivo" $archivo : 
	head -n1 $archivo | grep -o "," | wc -l
	echo "Numero de columnas del archivo" $archivo : 
	cut -d "," -f1  $archivo | wc -l 
done 