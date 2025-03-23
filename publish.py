"""Publish a release to mods.factorio.com."""
# When a new release tag is made, run this script

import os

import requests

MODS_API_BASE_URL = "https://mods.factorio.com/api/v2/mods"
DETAILS_ENDPOINT = MODS_API_BASE_URL + "/edit_details"
UPLOAD_ENDPOINT = MODS_API_BASE_URL + "/releases/init_upload"
PUBLISH_ENDPOINT = MODS_API_BASE_URL + "/init_publish"


def get_token() -> str:
    """Get the token from the environment."""
    if token := os.getenv("FACTORIO_TOKEN"):
        return token
    msg = "No token found in environment"
    raise ValueError(msg)

def verify_token(_token: str) -> bool:
    """Verify the token is valid."""
    headers = {
        "mod": "ModName",
    }
    _response = requests.post(DETAILS_ENDPOINT, headers=headers, timeout=5)
    return False

def main() -> None:
    """Publish a release to mods.factorio.com."""
    token = get_token()
    if not verify_token(token):
        msg = "Invalid token"
        raise ValueError(msg)


if __name__ == "__main__":
    main()
