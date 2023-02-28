import glob, csv, os

os.chdir("./spotify_stream_data")

all_csv_files = glob.glob("*.csv")

streamed_songs_dict = {}
for csv_file in all_csv_files:

    with open(csv_file, encoding="utf-8") as file_stream:
        all_dict_songs  = csv.DictReader(file_stream)
        date = csv_file[22:32]

        for song in all_dict_songs:
            key_name = f'{song["track_name"]} by {song["artist_names"]}'
            
            if key_name not in streamed_songs_dict:
                streamed_songs_dict[key_name] = {}

            streamed_songs_dict[key_name][date] = song["streams"]

print(streamed_songs_dict)