#!/bin/bash

declare PATTERN
declare COLLECTION
declare NUMBER
FORMAT="csv"

while test $# -gt 0; do
  case "$1" in
    -h|--help)
      echo " "
      echo "Qual ID - get qualitative IDs"
      echo " "
      echo "qual-id [options]"
      echo " "
      echo "options:"
      echo "-h, --help                show brief help"
      echo "-p, --pattern             specify the pattern of the qual IDs"
      echo "-c, --collection          specify which collection to use"
      echo "-n, --number              specify how many qual IDs to receive"
      echo "-f, --format              specify the format of the qual IDs"
      echo " "
      exit 0
      ;;
    -c|--collection)
      shift
      if test $# -gt 0; then
        COLLECTION=$1
      else
        echo "no collection specified"
        exit 1
      fi
      shift
      ;;
    -p|--pattern)
      shift
      if test $# -gt 0; then
        PATTERN=$1
      else
        echo "no pattern specified"
        exit 1
      fi
      shift
      ;;
    -n|--number)
      shift
      if test $# -gt 0; then
        NUMBER=$1
      else
        echo "no number specified"
        exit 1
      fi
      shift
      ;;
    -f|--format)
      shift
      if test $# -gt 0; then
        FORMAT=$1
      else
        echo "no format specified"
        exit 1
      fi
      shift
      ;;
    *)
      break
      ;;
  esac
done

URL="curl -s https://qual-id.herokuapp.com/get/"

if ! [ -z $PATTERN ]
then
  URL="${URL}\?pattern\=${PATTERN}"
fi

if ! [ -z $COLLECTION ]
then
  URL="${URL}\&collection\=${COLLECTION}"
fi

if ! [ -z $NUMBER ]
then
  URL="${URL}\&number\=${NUMBER}"
fi

if ! [ -z $FORMAT ]
then
  URL="${URL}\&format\=${FORMAT}"
fi

eval $URL
