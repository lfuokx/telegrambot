from googleapiclient.discovery import build

DEVELOPER_KEY = 'AIzaSyB9t01g0gC-Slkx0iSDbKLygnBY8AbqULw'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(text):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=text,
        part='id,snippet',
        maxResults=10
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s %s%s' % (search_result['snippet']['title'], 'https://www.youtube.com/watch?v=',
                                       search_result['id']['videoId']) + '\n')

    vids = ('Videos:\n', '\n'.join(videos), '\n')
    res = ''.join(vids)
    return res
