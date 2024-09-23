from dj_ai_1_5.orchestrator import Orchestrator
from dj_ai_1_5.genre import Genre

def main():
    Orchestrator.play_loop(Genre.HARDGROOVE, "HG2_1A_138bpm", 40)

if __name__ == "__main__":
    main()
