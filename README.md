GROOVESHARKY
------------------

An extractor for grooveshark songlists. It uses the tinysong api to retrieve grooveshark links from song names in the provided file 

USAGE
---------------------------
python groovesharky.py songFile

check out [GrooveBackup](http://groovebackup.com) for a way to download your library in a format supported by groovesharky. Any other format should work, granted that it is a csv file and begins with a line specifying the order of fields, i.e.
"SongName","ArtistName","AlbumName"

CONFIG
---------------------------
The file config.txt contains options for the downloader and uses JSON notation.
Currently the only option is

fileTemplate - template to save the file in. The expansions are any supported by youtube-dl, as well as artist, album, and song. see [the youtube-dl docs](http://rg3.github.io/youtube-dl/documentation.html#d8) for more information.

downloadDir - directory to save the file in, defaults to current directory.