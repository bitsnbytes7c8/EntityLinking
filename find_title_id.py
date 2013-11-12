import sys
from xml.dom import minidom
import re
import os

def parse(filename):
	xmldoc = minidom.parse('./Wiki_Split_Files/'+filename);
	pagelist = xmldoc.getElementsByTagName('page');

	for s in pagelist:
		title = s.getElementsByTagName('title')[0].firstChild.nodeValue;
		pageId = s.getElementsByTagName('id')[0].firstChild.nodeValue;
		title = title.encode('ascii', 'ignore');
		print title + " " + pageId;
	return;


def main():
	files = os.listdir('./Wiki_Split_Files');
	for f in files:
		parse(f);
	return;


if __name__ == "__main__":
	main();

