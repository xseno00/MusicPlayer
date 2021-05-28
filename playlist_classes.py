import json


class Song:
    def __init__(self, title: str, duration: int, priority: int, downloaded: bool, url: str):
        """
        The class for the Items of a playlist.
        :param title: the name of the song; mutable
        :param duration: the duration in second of the song; non-mutable
        :param priority: the priority which with the Song was provided, either high for 'heard a lot' or low for
        'heard less'; mutable
        :param downloaded: whether the Song is already available locally on the Computer; mutable
        :param url: the YouTube-URL, where the Song was downloaded from; mutable
        """
        self.title = title
        self.duration = duration
        self.priority = priority
        self.downloaded = downloaded
        self.url = url

    def toJSON(self) -> json:
        """
        Attributes where parsed into a dictionary and then into a JSON-String. Pretty-printing enabled!
        :return: the class-attributes as JSON-String
        """
        jsonStr = json.dumps(self.__dict__, indent=4, sort_keys=True)
        return jsonStr

    try:
        @property
        def __set_title(self, title: str):
            self.title = title

        @property
        def __set_prio(self, priority: int):
            self.priority = priority

        @property
        def __set_download(self, downloaded: bool):
            self.downloaded = downloaded

        @property
        def getTitle(self):
            return self.title

        @property
        def getDuration(self):
            return self.duration

        @property
        def getPriority(self):
            return self.priority

        @property
        def getDownloaded(self):
            return self.downloaded

        @property
        def getURL(self):
            return self.url
    except Exception as error:
        print("A" + str(error) + " is occurred")
        pass


class Playlist:
    def __init__(self):
        """
        The playlist filled with Song-Objects
        """
        self.items = []
        self.duration = 0

    @property
    def setDuration(self, duration: int):
        self.duration = duration

    def maxDuration(self) -> int:
        """
        FIXME wie greife ich auf die Attribute der Dinger in dem Array zu?
        Adds every second of each item together
        :return: sets the overall duration of the entire playlist
        """
        maxDuration = 0
        for i in len(self.items):
            maxDuration += self.items[i].duration
        return maxDuration

    def addItems(self, *kwargs: Song):
        """
        Fills a playlist with items.
        :type kwargs: Song
        :param kwargs: The provided Songs
        :return: The attribute item filled with Song-Objects
        :except: if the kwargs-Argument is not a Song, raises an 'AssertionError'
        """
        try:
            for item in kwargs:
                self.items.append(item)
        except Exception:
            print("An Error has occurred. Items to be added are no Songs!")

    def parseToJSON(self):
        """
        FIXME: Permission denied | PermissionError: [Errno 13] Permission denied: 'playlistItems.txt' |
        opens a file and saves all the contained data of the playlist
        :return: a nice JSON-file with all the meta-data from all the Elements of the playlist
        """
        with open("playlistItems.json", "a") as json_file:
            for i in self.items:
                json_file.write(i)


# DEBUG
song1 = Song("Noob", 120, 0, False, "www.duhurensohn.de").toJSON()
song2 = Song("Nutte", 17, 1, False, "www.duhurensohn.de").toJSON()
song3 = Song("Dreck", 175, 3, False, "www.duhurensohn.de").toJSON()
song4 = Song("Vik", 155, 0, False, "www.duhurensohn.de").toJSON()

playlist1 = Playlist()
playlist1.addItems(song1, song2, song3, song4)
#print(playlist1.maxDuration)
