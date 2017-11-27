from pydub import AudioSegment


song = AudioSegment.from_wav('example.wav')


def trans_to_mp3():
    tags = {
        'artist': '汪国平',
        'album': 'EECS',
    }
    song.export('example.mp3', format='mp3', bitrate='192k', tags=tags, cover='example.jpg')


def main():
    trans_to_mp3()


if __name__ == '__main__':
    main()
