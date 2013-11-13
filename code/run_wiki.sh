#Takes the full path of xml file and splits the file

mkdir Wiki_Split_Files
cd Wiki_Split_Files
split -b 100M --suffix-length=4 $1
cd ..
python quantizing.py "Wiki_Split_Files/"

# Finds title and ids from the wiki pages and sorts them based on title

python find_title_id.py
sort ../output/titles.txt > sorted_titles.txt
