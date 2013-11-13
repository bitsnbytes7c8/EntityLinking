import re
import sys
import os


def main():
	f = open("./nerOutput", "r");
	f2 = open("entities.txt", "w");
	ncount = 0;
	for line in f:
		list_str = line.split(" ");
		count = 0;
		output = "";
		for s in list_str:
			ent = s.split("/");
			l = len(ent);
			if l < 2:
				continue;
			if ent[l-1] != 'O':
				output = output + ent[0] + "\t";
				count = count + 1;
		if count > 0:
			f2.write(output + "\n");
		else:
			f2.write("null\n");	
			ncount = ncount + 1;
	print ncount
	return;

if __name__ == "__main__":
	main();
