#!/bin/bash -e

BASEDIR=$(dirname $0)

: <<=cut
=pod

=head1 NAME

FarasaPOS - Farasa Arabic Part of Speech Tagger

=head1 SYNOPSIS
  
farasaPOS.sh <InputFile> <OutputFile>
farasaPOS.sh < InputFile
farasaPOS.sh -i InputFile -o OutputFile 
  
 arguments:
   InputFile         Text Input file encoded in UTF-8
   OutputFile        Output file

=head1 DESCRIPTION

This script will run the QCRI FarasaPOS package for POS tagging Arabic text.

=head1 AUTHOR

<Kareem Darwish> (kdarwish@qf.org.qa)
<Ahmed Abdelali> (aabdelali@qf.org.qa)

=head1 COPYRIGHT

Copyright (C) <2016>, QCRI.

=cut

function VERBOSE {
  echo $@ > /dev/null
}

SHOWHELP=false 

while [[ $# -gt 0 ]]; do
  case "$1" in
   "--option1")
   #set something
    shift
    ;;
   "-h")
    shift
    SHOWHELP=true;
    ;;
   "--help")
    shift
    SHOWHELP=true;
    ;;
     *)
      break;
  esac
done

if $SHOWHELP;
then
  pod2text $0
  exit 0
fi


# 

if [[ $# -eq 0 ]]; then
  java -Xmx2048m -Dfile.encoding=UTF-8 -jar $BASEDIR/dist/FarasaPOSJar.jar 
fi

if [[ $# -eq 1 ]]; then
  java -Xmx2048m -Dfile.encoding=UTF-8 -jar $BASEDIR/dist/FarasaPOSJar.jar < $1
fi

if [[ $# -eq 2 ]]; then
  java -Xmx2048m -Dfile.encoding=UTF-8 -jar $BASEDIR/dist/FarasaPOSJar.jar -i $1 -o $2
fi

exit 0

