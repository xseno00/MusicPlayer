import playlist_classes as PC
import YT_hook as ytH
import json
import os
import subprocess as sp

my_api_key = (os.environ.get("YT_API_KEY"))
my_playlist = "PLawcFxg0tsjqHjxdh0Bkc8ZG9Qu4ElzHe"


if __name__ == '__main__':

    EdmPlaylist = PC.Playlist("edmPlaylist")
    EdmPlaylist.update_yt_links()

    # TODO Bring das hier zum laufen du Hund
    sp.run(["ls"], input="-la")
    """
    from re import search

    für die Ordner Durchsuchung

    fullstring = "StackAbuse"
    substring = "tack"

    if search(substring, fullstring):
        print "Found!"
    else:
        print "Not found!" 
    """
