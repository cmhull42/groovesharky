import csv, sys, requests, argparse, os
from urllib import quote_plus, unquote_plus
import youtube_dl

TINYAPI="3ff3fe93e57d32689612dfdb26bc137d"
BASEURL="http://tinysong.com/a/"
OPTIONS="?format=json&key="+TINYAPI

# input: songFile, file to read in
# output: a list of songs, represented by a dict with keys artist, song, album
def readSongs(songFile):
	songs = []
	with open(songFile) as csvfile:
		reader = csv.reader(csvfile, dialect=csv.get_dialect('excel'))
		fields = next(reader)
		songIndex = fields.index("SongName")
		artistIndex = fields.index("ArtistName")
		albumIndex = fields.index("AlbumName")
		for row in reader:
			if len(row) >= 3:
				song = {"song": row[songIndex], "artist": row[artistIndex], "album": row[albumIndex]}
				songs.append(song)

	return songs

# input: a properly escaped song query
# output: the json response
# retrieves the response from TinySong
def retrieveLinks(encoded_search):
	r = requests.get(BASEURL+encoded_search+OPTIONS)
	return r.json()

def __main__():

	if len(sys.argv) == 1:
		print("Error: pass in file to process")
		exit()

	parser = argparse.ArgumentParser(description="A grooveshark downloader")
	parser.add_argument("songFile")
	parser.add_argument("downloadDir")
	args = parser.parse_args(sys.argv[1:]) # ignore script name

	songfile = args.songFile

	downloadDir = args.downloadDir
	if not os.path.isdir(downloadDir):
		os.mkdir(downloadDir)

	songList = []

	try:
		songList = readSongs(songfile)
	except IOError:
		print("Error: File "+songfile+" could not be opened.")
		exit()

	links = []

	with YoutubeDL({"outtmpl": "%(title)s.%(ext)s"}) as ydl:
		for song in songList:
			link = retrieveLinks(quote_plus(" ".join(song.values())))
			ydl.download(link)

__main__()