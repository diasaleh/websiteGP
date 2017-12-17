#!/bin/sh
echo `mkdir $4_shell_output`
echo `mkdir $4_shell_output/Farasa`
echo `mkdir $4_shell_output/Farasa_details`
# echo "start Sheda_Leen"
# echo `python Sheda_Leen.py $1 $2 $3 $4` >> $4_shell_output/charout$4.txt
# echo "finish Sheda_Leen"
# echo "start entifakh"
# echo `python entifakh.py $1 $2 $3 $4` >> $4_shell_output/charout$4.txt
# echo "finish entifakh"
# echo "start CharOuts"
# echo `python charOut/main.py $1 $2 $3 $4` >> $4_shell_output/charout$4.txt
# echo "finish CharOuts"
# echo "start Mahmos_Mahjor"
# echo `python character\ frequency/main.py  $1 $2 $3 $4` >> $4_shell_output/Mahmos_Mahjor$4.txt
# echo "finish Mahmos_Mahjor"
# echo "start avgWordL"
# echo `python avgWordL/main.py  $1 $2 $3 $4` >> $4_shell_output/avgWordL$4.txt
# echo "finish avgWordL"
# echo "start charFreq"
# echo `python character\ frequency/charFreq.py $1 $2 $3 $4` >> $4_shell_output/charFreq$4.txt
# echo "finish charFreq"
echo "start FarasaPOS"
echo `java -jar "FarasaPOSJar.source (1)/dist/FarasaPOSJar.jar"  $1 $2 $3 $4`
echo "finish FarasaPOS"
# echo "start Farasa_out_Pro"
# echo `python Farasa_out_Pro/main.py   $1 $2 $3 $4` >> $4_shell_output/Farasa_out_Pro$4.txt
# echo "finish Farasa_out_Pro"

# echo "start PRON_New"
# echo `python Farasa_PRON.py $1 $2 $3 $4  PRON_New` >> $4_shell_output/PRON$4.txt
# echo "finish PRON_New"
# echo "start PRON_cat"
# echo `python PRON_cat.py $1 $2 $3 $4  PRON_cat` >> $4_shell_output/PORN_cat$4.txt
# echo "finish PRON_cat"
# echo "start NegWordsFreq"
# echo `python neg_word_new.py $1 $2 $3 $4` >> $4_shell_output/NegWordsFreq$4.txt
# echo "finish NegWordsFreq"
# echo "start PREP_NEW"
# echo `python Farasa_PREP.py $1 $2 $3 $4  PREP_NEW` >> $4_shell_output/PRON$4.txt
# echo "finish PREP_NEW"
