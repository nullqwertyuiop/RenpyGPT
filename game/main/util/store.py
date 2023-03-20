import contextlib
import time

import renpy.exports as rpy


class RenpyGPTStore:
    _finished: bool = False
    _contents: list[str] = []

    @property
    def finished(self):
        return self._finished

    @property
    def contents(self):
        return self._contents

    @contextlib.contextmanager
    def _lock(self):
        self._finished = False
        yield
        self._finished = True

    def generate(self):
        with self._lock():

            # TODO Impl GPT3.5
            #  Using sleep to mimic long-running process.
            for i in range(10):
                rpy.notify(f"Seq: {i}")
                time.sleep(0.1)
                self._contents.append(f"Hello [{i}]")

        rpy.notify("Finished")

    def cleanup(self):
        with self._lock():
            rpy.notify("Running clean up")
            self._contents.clear()
