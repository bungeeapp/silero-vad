# Setup & Run

```
$ pipenv install
$ pipenv shell
(env) $ python3 main.py
```

# Extract audio from video

```
ffmpeg -i VIDEO_PATH -ac 1 -ar 16000 AUDIO_PATH
```
