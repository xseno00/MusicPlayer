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


    def update_yt_links(self):
        """
        TODO Must be extended for all attributes
        updates the playlist.
        [x] Url
        [ ] Title
        [ ] Duration
        [ ] Downloaded
        :return void-Method. just updates the playlist object.
        """
        # local variables
        my_api_key = (os.environ.get("YT_API_KEY"))
        my_playlist = "PLawcFxg0tsjqHjxdh0Bkc8ZG9Qu4ElzHe"

        # extracts all video IDs
        vids_ids = ytH.extract_vid_ids(my_api_key, my_playlist)

        for i in range(len(vids_ids)):
            url = vids_ids[i]
            self.addItems(Song("", 0, 0, False, "https://www.youtube.com/watch?v=" + url).toJSON())

        self.parseToJSON()
