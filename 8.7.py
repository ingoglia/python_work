def make_album(artist, album, tracks=''):
    """builds a dictionary describing a music album"""
    if tracks:
        music =  {'artist': artist, 'album':album, 'number of tracks':tracks}
    else:
        music = {'artist': artist, 'album':album}
    return music

musician_album = make_album("Ren", "The Space of all things")
print(musician_album)

musician_album = make_album("Future Sounds", "We have explosives")
print(musician_album)

musician_album = make_album("Merzbow", "Offering")
print(musician_album)

musician_album = make_album("Yasunao Tone", "things", "6")
print(musician_album)
