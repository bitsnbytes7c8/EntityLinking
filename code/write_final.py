import re
import os
from itertools import izip;

def main():
	file_entities = open("../output/entities.txt", "r");
	file_details = open("../output/newsDeatils.txt", "r");
	out = open("../output/entityLinkage.txt", "w");
	for line1,line2 in izip(file_entities, file_details):
		line1 = line1.strip("\n");
		line2 = line2.strip("\n");
		s1 = line1.split("\t");
		s2 = line2.split("\t");
		filename = s2[0];
		title = s2[1];
		entities = "";
		for e in s1:
			entities = entities + e + " ";
		timestamp = s2[4];
		location = "nil";
		author = s2[2];
		url = s2[3];
		out.write(filename + "\t" + title + "\t" + entities + "\t" + timestamp + "\t" + location + "\t" + author + "\t" + url + "\n");
	return;

if __name__ == "__main__":
	main();
