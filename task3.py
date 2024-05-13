import datetime


class Song:
    """
    This class represents a song and its attributes.

    Attributes
    -----------
    - title: str, The title of the song.
    - duration: datetime.timedelta, The duration of the song.
    - artist: str, The artist who performed the song.
    - album: str, The album the song belongs to.
    - year: int, The year the song was released.

    Methods
    --------
    - play(): Starts playing the song and prints a message indicating the song is playing.
    - pause(): Pauses the song and prints the elapsed time since the song started playing.
               Returns the elapsed time in seconds if the song is playing, otherwise None.
    - stop(): Stops the song and prints the total duration the song was played.

    """

    def __init__(self, title, duration, artist, album, year):
        self.title = title
        self.duration = duration
        self.artist = artist
        self.album = album
        self.year = year

    def play(self):
        """
        Starts playing the song and prints a message indicating the song is playing.
        """
        self.start_time = datetime.datetime.now()
        print(f"Играет песня {self.title}")

    def pause(self):
        """
        Pauses the song and prints the elapsed time since the song started playing.
        :return: the elapsed time in seconds if the song is playing, otherwise None.
        """
        if self.start_time:
            elapsed_time = datetime.datetime.now() - self.start_time
            print(f"Песня {self.title} поставлена на паузу. Прошло {elapsed_time}")
            return elapsed_time.total_seconds()
        else:
            print(f"Песня {self.title} не воспроизводится")
            return None

    def stop(self):
        """
        Stops the song and prints the total duration the song was played.
        """
        if self.start_time:
            elapsed_time = datetime.datetime.now() - self.start_time
            print(f"Остановлено воспроизведение песни {self.title}. Прошло {elapsed_time}")
        else:
            print(f"Песня {self.title} не воспроизводится")
        self.start_time = None


class Playlist:
    """
    This class represents a playlist containing multiple songs.

    Attributes
    -----------
    - name: str, The name of the playlist.
    - all_tracks: list, A list of Song objects representing the songs in the playlist.

    Methods
    --------
    - add_song(song): Adds a Song object to the playlist.
    - start_playing(): Displays the list of songs in the playlist and allows the user to play, pause, or stop songs.
    """

    def __init__(self, name, songs=[]):
        self.name = name
        self.all_tracks = songs

    def add_song(self, song):
        """
        Adds a Song object to the playlist.
        """
        self.all_tracks.append(song)

    def start_playing(self):
        """
        Displays the list of songs in the playlist and allows the user to play, pause, or stop songs.
        """
        while True:
            print("\n=== Список песен ===")
            for i, song in enumerate(self.all_tracks, start=1):
                print(f"{i}. {song.title} - {song.artist}")

            choice = input("Выберите номер песни для проигрывания (или 'выход' для выхода): ")
            if choice == 'выход':
                break
            elif choice.isdigit():
                current_song = self.all_tracks[int(choice) - 1]
                current_song.play()

                while True:
                    action = input("Что вы хотите сделать?\n1. Поставить на паузу\n2. Остановить\n")
                    if action == '1':
                        pause_time = current_song.pause()
                        if pause_time is not None:
                            continue_play = input("Продолжить воспроизведение? (да/нет): ")
                            if continue_play.lower() == 'нет':
                                current_song.stop()
                                break
                    elif action == '2':
                        current_song.stop()
                        break
                    else:
                        print("Некорректный ввод, попробуйте снова.")
            else:
                print("Некорректный ввод, попробуйте снова.")


def load_songs_from_file(file_name):
    songs = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            title, duration, artist, album, year = data
            duration_minutes, duration_seconds = map(int, duration.split(':'))
            duration_timedelta = datetime.timedelta(minutes=duration_minutes, seconds=duration_seconds)
            song = Song(title, duration_timedelta, artist, album, int(year))
            songs.append(song)
    return songs


song_list = load_songs_from_file('tracks.txt')
playlist_1 = Playlist("Любимые песни Тейлор Свифт", song_list)
playlist_1.start_playing()
