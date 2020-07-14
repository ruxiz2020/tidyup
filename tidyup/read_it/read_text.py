import os
from gtts import gTTS


def readText(text, outfile='test.mp3', language='en'):

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells

    myobj = gTTS(text=text,
                 lang=language,
                 slow=False)  # speed

    myobj.save(outfile)


if __name__ == '__main__':

    with open('ch_test.txt', 'r') as file:
        data = file.read().replace('\n', ' ')

    readText(text=data, outfile='ch_test.mp3', language='zh-cn')
