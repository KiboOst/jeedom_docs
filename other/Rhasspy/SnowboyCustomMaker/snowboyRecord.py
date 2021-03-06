#! /usr/bin/env python3
# encoding: utf-8

import sys
import argparse
from codecs import open
import json
import datetime
import os
import time
import pyaudio
import wave
from utils import Audio

#no alsa warning handler:
from ctypes import *
from contextlib import contextmanager
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    try:
        asound = cdll.LoadLibrary('libasound.so')
        if asound:
            asound.snd_lib_error_set_handler(c_error_handler)
            yield
            asound.snd_lib_error_set_handler(None)
    except:
        yield


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 2.2
SNR_TRIM = 18
SNR_TRIM_CUT = 9
MAX_RECORD_DURATION = 1.6
MAX_DIFFERENCE_DURATION = 0.7

def record_one(directory, i):
    dest_path = os.path.join(directory, "{0}.wav".format(i))

    with noalsaerr():
        audio = pyaudio.PyAudio()

        input("\nPress enter to record sample %s, say your wakeword when \"recording...\" shows up"%i)
        time.sleep(0.5)

        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        print("recording...")
        frames = []

        for j in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("finished recording\n")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(dest_path, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(2)
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

def record_and_trim(wakeword, nb_records=3):
    input("You will record %s samples for your wakeword. Be sure to be in a quiet environment. Press enter once you are ready"%nb_records)
    directory = os.path.join('', wakeword)
    if os.path.exists(directory):
        os.system("rm -rf "+directory)
    os.makedirs(directory)

    is_validated = False
    while not is_validated:
        audios = []
        for i in range(nb_records):
            record_one(directory, i)
            dest_path = os.path.join(directory, "{0}.wav".format(i))
            audio = Audio.from_file(dest_path)
            audio.trim_silences(SNR_TRIM)
            while audio.duration() > MAX_RECORD_DURATION:
                print("WARNING: there seems to be too much noise in your environment.")
                record_one(directory, i)
                audio = Audio.from_file(dest_path)
                audio.trim_silences(SNR_TRIM)
            audios.append(audio)

        if any([abs(
                        audio_1.duration() - audio_2.duration()) > MAX_DIFFERENCE_DURATION
                for i, audio_1 in enumerate(audios) for j, audio_2 in
                enumerate(audios) if i < j]):
            print("WARNING: there seems to be too much difference between your records.")
        else:
            is_validated = True

    for i, audio in enumerate(audios):
        dest_path = os.path.join(directory, "{0}.wav".format(i))
        audio.write(dest_path)

    #remove silences:
    for i, audio in enumerate(audios):
        dest_path = os.path.join(directory, "{0}.wav".format(i))
        audio = Audio.from_file(dest_path)
        audio.write(dest_path.replace('.wav', '_uncut.wav'))
        audio.trim_silences(SNR_TRIM_CUT)
        audio.write(dest_path)

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), directory)
    print("Your samples have been saved in %s"%path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Snowboy Recorder', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--wakeword', help='key/folder for wakeword to train (no special characters)', type=str, default=None)
    args = parser.parse_args()

    if not args.wakeword:
        parser.print_help(sys.stderr)
        sys.exit(1)

    record_and_trim(args.wakeword)
