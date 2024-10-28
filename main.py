from spotifyAPI import SpotifyAPI
import pandas


def main():
    spotify = SpotifyAPI()
    artists_dataframe = pandas.DataFrame.from_dict(spotify.get_popular_artists())
    artists_dataframe.to_excel('artists.xlsx')

if __name__ == "__main__":
    main()