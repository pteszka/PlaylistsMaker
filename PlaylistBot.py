from selenium import webdriver
from PlaylistsMaker import token_to_log
from time import sleep
import re


class RymBot:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_ids(self):
        spotify_token = token_to_log()
        self.driver.get(
            'https://rateyourmusic.com/customchart?page=1&chart_type=top&type=single&year=2020&genre_include=1'
            '&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none'
            '&countries=')

        sleep(10)

        listOfSongs = []
        tbody = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody")
        str_tbody = '/html/body/div[2]/div[3]/table/tbody'

        for count, row in enumerate(tbody.find_elements_by_xpath('./tr')):
            if (count + 1) % 8 == 0:
                continue
            try:
                var = self.driver.find_element_by_xpath((str_tbody + '/tr[{}]/td[3]/div[2]/div').format(count + 1))
            except:
                continue
            song = var.find_elements_by_tag_name('a')  # .get_attribute("a")
            listOfSongs.append(song)

        idAlbums = []
        for count, x in enumerate(listOfSongs):
            for nr, tags in enumerate(x):
                if str(listOfSongs[count][nr].get_attribute("title")) == 'Spotify':
                    idAlbums.append(listOfSongs[count][nr].get_attribute("href"))

        for nr, album in enumerate(idAlbums):
            idAlbums[nr] = re.sub("https://open.spotify.com/album/", "", idAlbums[nr])

        idSongs = []
        topNumber = 0
        for counter, album in enumerate(idAlbums):
            if topNumber == 10:
                break
            album_tracks = spotify_token.sp.album_tracks(idAlbums[counter])
            for nr, song in enumerate(album_tracks['items']):
                idSongs.append(album_tracks['items'][nr]['id'])
            topNumber += 1

        return idSongs
