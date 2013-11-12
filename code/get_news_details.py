import sys
import xml.etree.ElementTree as et
import re
import os
import traceback

def main():
	i = 20120601;
	outTitle = open("../output/newsTitles.txt", "w");
	outDetails = open("../output/newsDeatils.txt", "w");
	while i <= 20120615:
		print i;
		files = os.listdir("../news/"+str(i));
		for f in files:
			#if f!="huffingtonpost.sports.html":
				#continue;
			try:
				if f.find('usatoday') != -1:
					continue;
				t = et.parse("../news/"+str(i)+"/"+f);
				root = t.getroot();
				for page in root:
					titleFormat = "title";
					pdateFormat = "pubDate";
					authorFormat = "author";
					linkFormat = "link";
					itemFormat = "item";
					nameFormat = "name";
					title = "nil";
					timstamp = "nil";
					author = "nil";
					url = "nil";
					if page.tag == "{http://www.w3.org/2005/Atom}entry":
						pdateFormat = "{http://www.w3.org/2005/Atom}published";
						titleFormat = "{http://www.w3.org/2005/Atom}title";
						authorFormat = "{http://www.w3.org/2005/Atom}author";
						linkFormat = "{http://www.w3.org/2005/Atom}link";
						itemFormat = "{http://www.w3.org/2005/Atom}item";
						nameFormat = "{http://www.w3.org/2005/Atom}name";
						for further in page:
							if further.tag == titleFormat and further.text is not None:
								title = further.text.encode('utf-8');
							if further.tag == linkFormat and further.text is not None:
								url = further.text.encode('utf-8');
							if further.tag == pdateFormat and further.text is not None:
								timestamp = further.text.encode('utf-8');
							if further.tag == authorFormat:
								for ft in further:
									if ft.tag == nameFormat and ft.text is not None:
										author = ft.text.encode('utf-8');
						title = title.replace("\n", " ");
						title = title.replace("\t", " ");
						author = author.replace("\n", " ");
						author = author.replace("\t", " ");
						url = url.replace("\n", " ");
						url = url.replace("\t", " ");
						timestamp = timestamp.replace("\n", " ");
						timestamp = timestamp.replace("\t", " ");
						outTitle.write(title+"\n");
						outDetails.write(str(i)+"/"+f+"\t"+title+"\t"+author+"\t"+url+"\t"+timestamp+"\n");
					for tags in page:	
						title = "nil";
						timestamp = "nil";
						author = "nil";
						url = "nil";
						if tags.tag == itemFormat:
							for further in tags:
								if further.tag == titleFormat and further.text is not None:
									title = further.text.encode('utf-8');
								if further.tag == linkFormat and further.text is not None:
									url = further.text.encode('utf-8');
								if further.tag == pdateFormat and further.text is not None:
									timestamp = further.text.encode('utf-8');
								if further.tag == authorFormat:
									for ft in further:
										if ft.tag == nameFormat and ft.text is not None:
											author = ft.text.encode('utf-8');
							title = title.replace("\n", " ");
							title = title.replace("\t", " ");
							author = author.replace("\n", " ");
							author = author.replace("\t", " ");
							url = url.replace("\n", " ");
							url = url.replace("\t", " ");
							timestamp = timestamp.replace("\n", " ");
							timestamp = timestamp.replace("\t", " ");
							outTitle.write(title+"\n");
							outDetails.write(str(i)+"/"+f+"\t"+title+"\t"+author+"\t"+url+"\t"+timestamp+"\n");
			except:
				print str(i)+"/"+f;
				#traceback.print_exc(file=sys.stdout);
		i = i+1;
	outDetails.close();
	outTitle.close();
	return;

if __name__ == "__main__":
	main();
