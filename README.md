GROOVESHARKY
------------------

An extractor for grooveshark songlists. It uses the tinysong api to retrieve grooveshark links from song names in the provided file 

USAGE
---------------------------
python groovesharky.py songFile downloadDir

CONFIG
---------------------------
The file config.txt contains options for the downloader and uses JSON notation.
Currently the only option is

filetemplate - template to save the file in. The expansion are any supported by youtube-dl, as well as artist, album, and song.