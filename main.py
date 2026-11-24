"""Write one short rant to /output/entry.txt.

The rant is a single text of at most 400 characters about one small
everyday annoyance: a smoke detector whose low-battery chirp performs
innocence all day and hunts at 3 a.m.

The shipped rant won a ten-candidate duel on the judge's own criteria
(see candidates.md): it is the most specific scene in the set — a
chair dragged over at 3 a.m., a man standing on it in his underwear,
a pillow — and its angle, the chirp that waits until your head
touches the pillow, is the freshest. It beat the runner-up, a
self-checkout that accuses its user of stealing a bag, on
specificity and freshness; the USB plug's three flips fell first,
as an angle heard a hundred times.
"""

import os

RANT = (
    "The smoke detector waits until 3 a.m. to announce its battery "
    "is dying. One chirp. I drag a chair over and climb up in my "
    "underwear, and it goes silent — silent all day, silent all "
    "evening, a model citizen — until my head touches the pillow. "
    "Then: chirp. It is not dying. It is hunting."
)


def main():
    assert 1 <= len(RANT) <= 400, "rant must fit the 400-character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
