def make_album(artist, album, tracks=''):
    """builds a dictionary describing a music album"""
    if tracks:
        music =  {'artist': artist, 'album':album, 'number of tracks':tracks}
    else:
        music = {'artist': artist, 'album':album}
    return music

while True:
    print("\nPlease tell me an artist and an album by them:")
    print("(enter 'q' at any time to quit)")

    user_artist = input("Name of artist: ")
    if user_artist == 'q':
        break

    user_album = input("Name of album: ")
    if user_album == 'q':
        break

    user_choice = make_album(user_artist,user_album)
    print(user_choice)
