
for HW_NUM in {8..16}
do
    mkdir homework/homework${HW_NUM}
    mkdir homework/homework${HW_NUM}/src
    mkdir homework/homework${HW_NUM}/data
    mkdir homework/homework${HW_NUM}/data/raw
    mkdir homework/homework${HW_NUM}/data/processed
    mkdir homework/homework${HW_NUM}/notebook
    cd homework/homework${HW_NUM}
    touch .env
    touch .env.example
    cd ..
    cd ..
done