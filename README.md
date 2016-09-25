# Bessy Beta
Próftöfluröðun fyrir haustið 2016

Bessy.mod er AMPL líkan notað fyrir röðun
forsendur.dat eru séróskir


Til að keyra:

sed -i 's/param phase := 0;/param phase := 1;/g' Bessy.mod

glpsol --check -m Bessy.mod -d default.dat -d forsendur.dat -d courses.dat -d resources.dat --wlp Bessy1.lp

gurobi_cl Threads=8 ResultFile=Bessy1.sol Bessy1.lp &

cat Bessy1.sol | grep Slot | grep -v ') 0' > Split.txt

python3 ChangeToRightFormatForPhases.py

# May now want to tune the tolerance
echo "param tolerancesame := 5;" > params.dat
echo "param tolerance := 15;" >> params.dat
echo "" >> params.dat

# Switch to phase 2
sed -i 's/param phase := 1;/param phase := 0;/g' Bessy.mod

glpsol --check -m Bessy.mod -d default.dat -d forsendur.dat -d courses.dat -d resources.dat -d Split.dat -d params.dat --wlp Bessy2.lp

gurobi_cl Threads=8 ResultFile=Bessy2.sol Bessy2.lp &

cat Bessy2.sol | grep Slot | grep -v ') 0' > Split.txt

python3 ChangeToRightFormatForPhases.py

glpsol -m Bessy.mod -d default.dat -d forsendur.dat -d courses.dat -d resources.dat -d Split.dat -d params.dat








