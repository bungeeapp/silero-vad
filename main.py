from pprint import pprint
import torch
from utils_vad import get_speech_timestamps, read_audio, init_jit_model

SAMPLING_RATE = 16000

torch.set_num_threads(1)

model = init_jit_model("./files/silero_vad.jit")


def get_silence_timestamps(speech_timestamps):
    silence_timestamps = []

    speech_end = speech_timestamps[0]['end']
    speech_timestamps.pop(0)

    for timestamp in speech_timestamps:
        speech_start = timestamp['start']
        silence_timestamps.append(
            {'end': speech_start, 'start': speech_end, 'duration': speech_start - speech_end})
        speech_end = timestamp['end']

    return silence_timestamps


def main():
    wav = read_audio('ambient_noise_audio_16hz.wav',
                     sampling_rate=SAMPLING_RATE)

    speech_timestamps = get_speech_timestamps(
        wav, model, sampling_rate=SAMPLING_RATE, return_seconds=True)

    pprint(speech_timestamps)
    pprint(get_silence_timestamps(speech_timestamps))


if __name__ == '__main__':
    main()
