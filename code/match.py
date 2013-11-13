import os
import re
import porter2
from pprint import pprint

word_id = {};
id_title = {};

def create_index():
	global word_id;
	global id_title;
	inp = open("../output/titles.txt", "r");
	j = 0;
	for line in inp:
		j = j+1;
		line = line.strip("\n");
		strlist = line.split("  ");
		id_title[strlist[1]] = strlist[0];
		i = strlist[1];
		strlist[0] = re.sub(r'([^\s\w]|_)+', ' ', strlist[0]);
		strlist[0] = re.sub(' +', ' ', strlist[0]);
		title = strlist[0].split(" ");
		for word in title:
			word = word.lower();
			if len(word) < 2:
				continue;
			if word in word_id and len(word_id[word]) >= 1000:
				continue;
			if word in word_id:
				word_id[word].append(i);
			else:
				word_id[word] = [];
				word_id[word].append(i);
	return;

def match_entity():
	global word_id;
	global id_title;
	inp = open("../output/entities.txt", "r");
	oup = open("../output/entity_title.txt", "w");
	j = 0;
	for line in inp:
		j = j+1;
		print j;
		line = line.strip("\n");
		entlist = line.split("\t");
		for entity in entlist:
			if entity == "null":
				continue;
			url = "";
			entity = entity.lower();
			if entity in word_id:
				idlist = word_id[entity];
				top = id_title[idlist[0]];
				minwords = len(re.split(r'([^\w]|_)+', id_title[idlist[0]]));
				for id in idlist:
					words = len(re.split(r'([^\w]|_)+', id_title[id]));
					if words < minwords:
						top = id_title[id];
						minwords = words;
				oup.write(top+"\t");
		oup.write("\n");
	oup.close();
	return;
				



def main():
	create_index();
	print "Finished indexing";
	match_entity();
#	pprint(word_id);
#	pprint(id_title);
	return;

if __name__ == "__main__":
	main();
