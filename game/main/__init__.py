import renpy
import renpy.exports as rpy
from game.main.util.text import escape
from game.main.util.store import RenpyGPTStore


rpy_store = RenpyGPTStore()

__narrator = renpy.character.Character(None)


def mimic_run():
    name = rpy.input("What is your name?", default="You")
    rpy.say(__narrator, "TestMenu")
    result = rpy.display_menu([("Test", "test"), ("Test1", "test1")])
    rpy.say(__narrator, f"You chose: {result}")
    chara = renpy.character.Character(name)

    rpy.invoke_in_thread(rpy_store.generate)
    _said_loading = False
    while not rpy_store.finished:
        if not _said_loading:
            rpy.say(chara, "Loading...")
            _said_loading = True
        else:
            rpy.say(chara, "Still loading...")

    for part in rpy_store.contents:
        rpy.say(chara, escape(part))
