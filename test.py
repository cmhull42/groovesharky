import argparse,sys,json
import youtube_dl

parser = argparse.ArgumentParser(description="blehbleh")
parser.add_argument("files")
parser.add_argument("-o")
print sys.argv
args = parser.parse_args(sys.argv[1:])
# print args.files

print args.o

config = {}

with open("config.txt") as conf:
	config = json.loads(conf.read())

songtemplate = config.get("filetemplate", "")

with youtube_dl.YoutubeDL({"outtmpl": songtemplate}) as ydl:
	ydl.add_default_info_extractors()
	ie = ydl.extract_info("http://grooveshark.com/#!/s/This+Is+Twice+Now/4aqiOJ?src=5",
	 download=True, extra_info={"song": "This Is Twice Now", "artist": "Lydia", "album": ""})
	# print ie["_type"]
	# ydl.process_info(ie)
