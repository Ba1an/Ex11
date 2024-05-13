import datetime


class Song:
    def __init__(self, title, duration, artist, album, year):
        self.title = title
        self.duration = duration
        self.artist = artist
        self.album = album
        self.year = year

    def play(self):
        self.start_time = datetime.datetime.now()
        print(f"Играет песня {self.title}")

    def pause(self):
        if self.start_time:
            elapsed_time = datetime.datetime.now() - self.start_time
            print(f"Песня {self.title} поставлена на паузу. Прошло {elapsed_time}")
            return elapsed_time.total_seconds()
        else:
            print(f"Песня {self.title} не воспроизводится")
            return None

    def stop(self):
        if self.start_time:
            elapsed_time = datetime.datetime.now() - self.start_time
            print(f"Остановлено воспроизведение песни {self.title}. Прошло {elapsed_time}")
        else:
            print(f"Песня {self.title} не воспроизводится")
        self.start_time = None


class Playlist:
    def __init__(self, name, songs=[]):
        self.name = name
        self.all_tracks = songs

    def add_song(self, song):
        self.all_tracks.append(song)

    def start_playing(self):
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




