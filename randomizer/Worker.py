"""Task file to run functions in the background via webworkers."""
import json
import uuid
import js


def background(body):
    """Background a function via a webworker.

    This is a fully isolated function, you can not access the UIs DOM.

    Args:
        function (func): The function we run after backgrounding.
        args (list): List of args to pass to the function.
        returning_func (func): Function to run once we complete the main function.
    """
    branch = "dev"
    if js.location.hostname in [
        "dev.dk64randomizer.com",
        "dk64randomizer.com",
    ]:
        if "dev" not in str(js.location.hostname).lower():
            branch = "master"
        url = "https://dk64-seed-generator.adaptable.app/generate"
    else:
        url = f"http://{str(js.window.location.hostname)}:5000/generate"
    id = str(uuid.uuid1())
    js.generate_seed(url, json.dumps(body), branch, id)
