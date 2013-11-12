import sys
import xml.etree.ElementTree as et
import re
import os

def main():
	files = os.listdir('./Wiki_Split_Files');
	fl = open("title_id.txt", "w");
	i = 0;
	for f in files:
		i = i+1;
		print str(i)+" "+f;
		t = et.parse("./Wiki_Split_Files/"+f);
		root = t.getroot();
		for page in root:
			for tags in page:
				if tags.tag=="title":
					fl.write(tags.text.encode('utf-8')+'  ')
				if tags.tag=="id":
					fl.write(tags.text.encode('utf-8')+'\n')


if __name__ == "__main__":
	main();

