cleanup steps

Bash:

                for i in *.csv ; do
                  echo "$i" ;
                  sleep 1 ;
                  cat $i | cut -d, -f1 | sort -n | uniq >> alleles_parsed.txt ;
                done

                perl -pe 's/\"//g' alleles_parsed.txt > alleles_parsed.parsed.txt
                perl -pe 's/(.*)\|(.*)/$1/g' alleles_parsed.parsed.txt > alleles_parsed.names.txt

                #!/bin/sh

                ARR=($(<alleles_parsed.names.txt))
                for i in "${ARR[@]}" ; do
                  rgx="[[:space:]]"
                  if [[ ! "$i" =~ $rgx ]] ; then
                    V=$(echo "$i" | cut -d_ -f1)
                    if [[ "$V" = "Mamu" ]] ; then
                      echo "$i" >> alleles_parsed.final.txt ;
                    else
                      AVAL=$(echo "$i" | cut -d_ -f2-) ;
                       echo "$AVAL" >> alleles_parsed.final.txt
                    fi
                  fi
                done

             cat alleles_parsed.final.txt | sort -n | uniq > allele_names.txt

Then manually parse to remove entries like "runID"


Repeat above steps with data text files, with the modifications:
              
              perl -pe "s/\"//g" dataTextFile.txt > dataTextFile.parsed.txt
              perl -pe "s/\'//g" dataTextFile.parsed.txt > dataTextFile.parsed2.txt
