from PlaylistsMaker import token_to_log
from PlaylistBot import RymBot

bot = RymBot()
spotify_token = token_to_log()

if spotify_token.check_if_playlist_exists():
    create_playlist = spotify_token.sp.user_playlist_create(spotify_token.user, spotify_token.playlist_name, public=True)

spotify_token.sp.user_playlist_replace_tracks(spotify_token.user, spotify_token.get_playlist_id(), bot.get_ids())
