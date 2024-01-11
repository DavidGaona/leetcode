# C/B# C#/Db D D#/Eb E/Fb F/E# F#/Gb G G#/Ab A A#/Bb B/Cb
scale = {"B#": 0, "C#": 1, "D": 2, "D#": 3, "Fb": 4, "E#": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "Cb": 11}
scale_2 = {"C": 0, "Db": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "Gb": 6, "G": 7, "Ab": 8, "A": 9, "Bb": 10, "B": 11}

notes = ["B#,", "C#", "D", "D#", "Fb", "E#", "F#", "G", "G#", "A", "A#", "Cb"]
notes_2 = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

translation = {"SECOND": 1, "THIRD": 2, "FOURTH": 3, "FIFTH": 4, "SIXTH": 5, "SEVENTH": 6, "OCTAVE": 7}


def generate_major_scale(key):
    major_scale_pos = {}
    major_scale = [""] * 7
    index = 0
    if key in scale:
        index = scale[key]
    else:
        index = scale_2[key]
    major_scale[0] = key
    major_scale_pos[key] = 0
    for i in range(1, 7):
        # Semitone
        if i == 3:
            index += 1
        else:
            index += 2

        major_scale_pos[notes_2[index % 12]] = i
        major_scale[i] = notes_2[index % 12]

    return major_scale_pos, major_scale


def tomar_input():
    inputs = []
    while True:
        key = input()
        if key == "":
            return inputs
        queries = input()
        inputs.append((key, queries))


for single_input in tomar_input():
    key = single_input[0]
    queries = single_input[1].split(";")
    print("Key of", key)
    major_scale_pos, major_scale = generate_major_scale(key)
    # print(major_scale)
    for query in queries:
        note, direction, interval = query.split(" ")
        was_scale_2 = True

        if note in scale:
            was_scale_2 = False
            if note in scale_2:
                was_scale_2 = True
            note_2 = notes_2[scale[note]]
        else:
            note_2 = note
            note = notes[scale_2[note]]

        if note_2 not in major_scale_pos:
            if was_scale_2:
                print(f"{note_2}: invalid note for this key")
            else:
                print(f"{note}: invalid note for this key")
            continue

        if direction == "UP":
            next_note = major_scale[(major_scale_pos[note_2] + translation[interval]) % 7]
        else:
            next_note = major_scale[(major_scale_pos[note_2] - translation[interval]) % 7]

        if was_scale_2:
            print(f"{note_2}: {direction} {interval} > {next_note}")
        else:
            print(f"{note}: {direction} {interval} > {notes[scale_2[next_note]]}")
    print()
