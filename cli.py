"""CLI script for running seed generation."""
import argparse
import codecs
import json
import pickle
import random
import os
import sys
import traceback

from randomizer.Enums.Settings import SettingsMap
from randomizer.Fill import Generate_Spoiler
from randomizer.Settings import Settings
from randomizer.SettingStrings import decrypt_settings_string_enum
from randomizer.Spoiler import Spoiler


def generate():
    """Gen a seed and write the file to an output file."""
    generate_settings = decrypt_settings_string_enum("bbpRYfh9VDwiGQpkJUtjXPgQRGkV6mTCIWenrG2oBBCkNBBLA7ABQ2AC05ASw+AB4zADxAAA83AJY0AFo1AHg/ADI9APA6ADI4AAM8/9hQX8EoAycBkF1ls0FAAF1AAEGAAJ2AAIHAAN3AAMIAAR4AAQJAAV5AAUKAAZ6AAYLAAd7AAcMAAhRhoAivgDIKYAHqQAltAolmXmk0oFcSFRFgABExFAABX7ZHY5a79I4HgUyVRXY3RJNYgkgzAgjmGDcZAcWy0AhcbywWRYKS4GhQLRWKjCTRiRzSRjkgBIQwAeAH0AJwBwAFYA")
    generate_settings["seed"] = random.randint(0, 100000000)
    settings = Settings(generate_settings)
    spoiler = Spoiler(settings)
    Generate_Spoiler(spoiler)



def lambda_handler(event, context):
    generate()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }