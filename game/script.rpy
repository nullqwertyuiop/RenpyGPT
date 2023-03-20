init python:

    import main

define author = Character("nullqwertyuiop")

label start:

    # Always reload main modules

    python:

        import importlib
        import sys

        for __sys_module in sys.modules.copy():
            if (
                __sys_module == "main"
                or __sys_module.startswith("main.")
                or __sys_module.startswith("game.main.")
            ):
                importlib.reload(sys.modules[__sys_module])

        main.rpy_store.cleanup()
        main.mimic_run()

    scene bg room

    author "It seems you have reached the end of RenpyGPT"

    author "Feel free to restart a new session."

    return
