#starting from root dir after the pull 

# the first parameter is the directory name 

# second parameters is group id 

cp -f text2.txt $1 

cd $1 

rm -rf  g$2.txt 

rm -f comprimido.elmejorprofesor 

rm -f descomprimido-elmejorprofesor.txt 

python3 compresor.py text2.txt >> g$2.txt 

python3 descompresor.py  >> g$2.txt 

python3 verificador.py text2.txt >> g$2.txt 

sizeBiblia="$(wc -c <text2.txt)" 

sizeCompressed="$(wc -c <comprimido.elmejorprofesor)" 

sizedDecompressed="$(wc -c <descomprimido-elmejorprofesor.txt)" 

echo "Original size ${sizeBiblia} compressed ${sizeCompressed} decompressed ${sizedDecompressed}" >> g$2.txt 

diffOriginal=`expr $sizeBiblia - $sizedDecompressed` 

echo "compression rate ...." >> g$2.txt 

echo "Sized diff between original and decompressed ${diffOriginal}"  >> g$2.txt 

cp g$2.txt ../ 

cd .. 

 