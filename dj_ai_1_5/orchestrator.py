from pydub import AudioSegment
from pydub.playback import play
from dj_ai_1_5.genre import Genre

loop_prefix = "bin/loop/"

class Orchestrator:
    def play_loop(genre: Genre, id: str, repetitions: int):
        soundId = loop_prefix + genre.value + "/" + id + ".wav"
        sound = AudioSegment.from_file(soundId, format="wav")
        play(sound * repetitions)