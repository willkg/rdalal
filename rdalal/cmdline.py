import random
import webbrowser


# FIXME: Should scrape YouTube for this list
SONGS = [
    'https://www.youtube.com/watch?v=NMZcwXh7HDA',  # Apples and Cinnamon
    'https://www.youtube.com/watch?v=N-j6MRgC3tM',  # Red Red Bird
    'https://www.youtube.com/watch?v=VrgVE1i8hMw',   # After You
    'https://www.youtube.com/watch?v=kOTm4T7et-U',  # Love Just Wasn't Enough
]


def run():
    song = random.choice(SONGS)
    webbrowser.open(song, new=2, autoraise=True)
