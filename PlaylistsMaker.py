import spotipy
import spotipy.util as util
import secrets


class token_to_log:
    def __init__(self):
        self.scope = 'playlist-modify-public'
        self.username = secrets.username
        self.CLIENT_ID = secrets.CLIENT_ID
        self.CLIENT_SECRET = secrets.CLIENT_SECRET
        self.REDIRECT_URI = secrets.REDIRECT_URI
        self.user = secrets.user
        self.token = util.prompt_for_user_token(self.username, self.scope, self.CLIENT_ID, self.CLIENT_SECRET,
                                                self.REDIRECT_URI)
        self.sp = spotipy.Spotify(self.token)
        self.playlist_name = 'Top 10 Singles of 2020 by RYM users'

    @property
    def sp(self):
        return self._sp

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @sp.setter
    def sp(self, value):
        self._sp = value

    def check_if_playlist_exists(self):  # checkin if playlist already exist
        for count, x in enumerate(self.sp.user_playlists(self.user)['items']):
            if str(self.sp.user_playlists(self.user)['items'][count]['name']) == 'Top 10 Singles of 2020 by RYM users':
                return False
        return True

    def get_playlist_id(self):  # extract playlist's ids
        for count, x in enumerate(self.sp.user_playlists(self.user)['items']):
            if str(self.sp.user_playlists(self.user)['items'][count]['name']) == 'Top 10 Singles of 2020 by RYM users':
                return str(self.sp.user_playlists(self.user)['items'][0]['id'])
        return False
