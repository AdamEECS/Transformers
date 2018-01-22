from pydub import AudioSegment


song = AudioSegment.from_wav('REC030.wav')


def trans_to_mp3():
    tags = {
        'artist': '陈向群',
        'album': 'EECS',
    }
    song.export('20180113 操作系统 上午 04.mp3', format='mp3', bitrate='192k', tags=tags, cover='example.jpg')


def main():
    trans_to_mp3()


if __name__ == '__main__':
    main()
