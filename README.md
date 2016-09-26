# Bessy - Beta 0.0.1 próftöfluröðun

Bessy.mod er AMPL líkan notað fyrir röðun
forsendur.dat eru séróskir deilda...


# Fasi 1

sed -i 's/param phase := 0;/param phase := 1;/g' Bessy.mod

glpsol --check -m Bessy.mod -d default.dat -d forsendur.dat -d courses.dat -d resources.dat --wlp Bessy1.lp

nohup gurobi_cl Threads=8 ResultFile=Bessy1.sol Bessy1.lp &

# now wait for many hours ;)

cat Bessy1.sol | grep Slot | grep -v ') 0' > Split.txt

python3 ChangeToRightFormatForPhases.py

# Stilla breytur fyrir fasa 2
echo "param tolerancesame := 5;" > params.dat

echo "param tolerance := 15;" >> params.dat

echo "" >> params.dat

# Fasi 2
sed -i 's/param phase := 1;/param phase := 0;/g' Bessy.mod

glpsol --check -m Bessy.mod -d default.dat -d forsendur.dat -d courses.dat -d resources.dat -d Split.dat -d params.dat --wlp Bessy2.lp

gurobi_cl Threads=8 ResultFile=Bessy2.sol Bessy2.lp

# this phase should be fast

cat Bessy2.sol | grep Slot | grep -v ') 0' > Split.txt

python3 ChangeToRightFormatForPhases.py

# Prenta lausn

glpsol -m Bessy.mod -d default.dat -d forsendur.dat -d courses.dat -d resources.dat -d Split.dat -d params.dat



