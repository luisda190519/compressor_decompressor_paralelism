@echo off

set archivo1=LaBiblia.txt
set archivo2=descomprimido-elmejorprofesor.txt
set archivo3=comprimido.elmejorprofesor
set archivo4=g.txt

if exist "%archivo3%" del "%archivo3%"
if exist "%archivo2%" del "%archivo2%"
if exist "%archivo4%" del "%archivo4%"

python compresor.py "%archivo1%" >> "%archivo4%"
python descompresor.py >> "%archivo4%"
python verificador.py "%archivo1%" >> "%archivo4%"

for %%F in ("%archivo1%") do set "sizeBiblia=%%~zF"
for %%F in ("%archivo2%") do set "sizedDecompressed=%%~zF"
for %%F in ("%archivo3%") do set "sizeCompressed=%%~zF"

fc /b "%archivo1%" "%archivo2%" > nul
set /a diferencia=sizeBiblia-sizedDecompressed

echo Original size %sizeBiblia% compressed %sizeCompressed% decompressed %sizedDecompressed% >> "%archivo4%"
echo compression rate .... >> "%archivo4%"
echo Sized diff between original and decompressed %diferencia%  >> "%archivo4%" 