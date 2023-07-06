import sys

from typing import List

def compose(notes: List[str], moves: List[int], start: int) -> List[str]:
    song = []
    notes_size = len(notes)

    for m in moves:
        song.append(notes[start])
        start = (start + m) % notes_size
    song.append(notes[start])
    return song

def main():
    """
    4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start
    position (integer). The function will return the song composed by going though the musical notes beginning with the start 
    position and following the moves given as parameter.
    """
    try:
        result = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()