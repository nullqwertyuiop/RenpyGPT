import contextlib
import time

import renpy
import renpy.exports as rpy


class _RenpyGPTStore:
    _finished: bool = False
    _contents: list[str] = []

    @contextlib.contextmanager
    def _flag(self):
        self._finished = False
        yield
        self._finished = True

    def generate(self):
        with self._flag():

            # TODO Impl GPT3.5
            #  Using sleep to mimic long-running process.
            for i in range(10):
                rpy.notify(f"Seq: {i}")
                time.sleep(1)
                self._contents.append(f"Hello ({i})")

        rpy.notify("Finished")

    @property
    def finished(self):
        return self._finished

    @property
    def contents(self):
        return self._contents


_rpy_store = _RenpyGPTStore()


def mimic_run():
    name = rpy.input("What is your name?")
    chara = renpy.character.Character(name)

    rpy.invoke_in_thread(_rpy_store.generate)
    _said_loading = False
    while not _rpy_store.finished:
        if not _said_loading:
            rpy.say(chara, "Loading...")
            _said_loading = True
        else:
            rpy.say(chara, "Still loading...")

    for part in _rpy_store.contents:
        rpy.say(chara, part)
