import playlist_classes as pc
from googleapiclient.discovery import build



def get_playlist_items(api_key: str, playlist_id: str):
    """
    1.  Builds up a connection to the YouTube-API with the 'service'-attribute
    2.  Makes a request to receive data with the 'request'-attribute
    3.  In the while-loop the program calculates/request the 'nextPageToken' of the play list-request.
        Its done, because the maximum of results that can be requested at once is 50. Therefore the next items are
        saved in another page.
    4.  Then checks if the added items are already in the List of Items. Either pops or adds it to the dict(cleanup).
    :param api_key: The developer Key generated by Google on their site
    :param playlist_id: The Playlists ID from YouTube
                        https://www.youtube.com/playlist?list= ... |PLkmghnJPShXRV5J1cSfENMAuhb4WPhtxP| ...
    :return:    returns a dictionary with ALL the 'contentDetails' of the 'youtube#playlistItemListResponse'
    """
    service = build("youtube", "v3", developerKey=api_key)
    request = service.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=50,
    ).execute()

    nextPageToken = request.get('nextPageToken')
    while "nextPageToken" in request:
        nextPage = service.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken
        ).execute()
        request['items'] = request['items'] + nextPage['items']

        if "nextPageToken" not in nextPage:
            request.pop("nextPageToken", None)
        else:
            nextPageToken = nextPage['nextPageToken']
    return request


def extract_vid_ids(api, playlist):
    """
    Calls get_playlist_items() first and then saves all 'videoId' given by the Function in a List
    :param api: The developer Key generated by Google on their site
    :param playlist: The Playlists ID from YouTube
    :return:    List of all video IDs from the given YouTube Playlist
    """
    request_dict = get_playlist_items(api_key=api, playlist_id=playlist)
    vid_ids = []
    for i in range(len(request_dict['items'])):
        vid_ids.append(request_dict['items'][i]['contentDetails']['videoId'])
    return vid_ids
