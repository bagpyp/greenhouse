import os
import pathlib

from dotenv import load_dotenv

properties = {}


def initialize():
    global properties

    # machine specific
    root_dir = pathlib.Path(__file__).parents[2]
    properties["ROOT_DIR"] = root_dir

    # environment specific
    ENV = os.environ.get("ENV", "local")  # default to local env
    properties["ENV"] = ENV
    load_dotenv(os.path.join(root_dir, f".env.{ENV.lower()}"))

    for env_var in [
        "OPENWEATHERMAP_API_KEY",
        "LOG_LEVEL",
    ]:
        properties[env_var] = os.getenv(env_var)
