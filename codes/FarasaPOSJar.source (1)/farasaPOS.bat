@echo off

REM set FarasaDataDir=%~dp0..\FarasaData\
REM echo %FarasaDataDir%

set _argcActual=0

if %1 EQU -h (
    goto:ShowUsage
) 

if %1 EQU --help (
    goto:ShowUsage
) 

for %%i in (%*) do set /A _argcActual+=1

if %_argcActual% EQU 0 (

  REM echo call farasa with 0 arg
  java -Xmx2048m -Dfile.encoding=UTF-8 -jar dist\FarasaPOSJar.jar 
  goto:_EOF

)

if %_argcActual% EQU 1 (

  REM echo call farasa with one arg ""%1""
  java -Xmx2048m -Dfile.encoding=UTF-8 -jar dist\FarasaPOSJar.jar < %1
  goto:_EOF
  
)

if %_argcActual% EQU 2 (

  REM echo call farasa with -i %1 -o %2
  java -Xmx2048m -Dfile.encoding=UTF-8 -jar dist\FarasaPOSJar.jar -i %1 -o %2
  goto:_EOF
  
) 


:ShowUsage

echo FarasaPOS - Farasa Arabic Part of Speech Tagger
echo. 
echo SYNOPSIS
echo.  
echo farasaPOS.bat InputFile OutputFile
echo farasaPOS.bat InputFile
echo farasaPOS.bat ^< InputFile 
echo. 
echo arguments:
echo    InputFile   :  Text Input file encoded in UTF-8
echo    OutputFile  :  Output file
echo.
echo DESCRIPTION
echo.
echo This script will run the QCRI FarasaPOS package for POS tagging Arabic text.
echo.
echo AUTHOR
echo. 
echo ^<Kareem Darwish^> (kdarwish@qf.org.qa)
echo ^<Ahmed Abdelali^> (aabdelali@qf.org.qa)
echo. 
echo COPYRIGHT
echo. 
echo Copyright (C) ^<2015^>, QCRI.
echo. 
goto:_EOF


goto :eof


:_EOF

echo.

cmd /c exit 

