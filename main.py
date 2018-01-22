from pydub import AudioSegment


song = AudioSegment.from_wav('REC032.wav')


def trans_to_mp3():
    tags = {
        'artist': '李胜',
        'album': 'EECS',
    }
    song.export('20180114 图形学 06.mp3', format='mp3', bitrate='192k', tags=tags, cover='example.jpg')


def main():
    trans_to_mp3()


if __name__ == '__main__':
    main()
