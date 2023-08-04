import json
import os
from pprint import pprint

import requests

SEPARATOR = "_" * 40


def main():
    auth_token = os.getenv("TOKEN")
    base_url = "https://openepd.staging.buildingtransparency.org/api"
    headers = {"Authorization": f"Bearer {auth_token}"}

    created_epd_id = None

    print_section("Creating necessary organisations")
    # ensure we have verifier, manufacturer, and program_operator, the hard way
    for org_json in ["manufacturer.json", "program_operator.json", "third_party_verifier.json"]:
        with open(f"{org_json}") as f:
            org = json.load(f)

            response = requests.post(f"{base_url}/orgs", json=org, headers=headers)
            if response.status_code == 201:
                print(f"Created org by {org_json}")
            else:
                print(f"Exists? Org creation failed with {response.status_code}. {response.text}")

    # ensure we have a plant, the hard way
    print_section("Creating dependency plant")
    with open("plant.json") as f:
        plant = json.load(f)
        response = requests.post(f"{base_url}/plants", json=plant, headers=headers)
        if response.status_code == 201:
            print("Created new plant by plant.json")
        else:
            print(f"Exists? Plant creation failed with {response.status_code}. {response.text}")

    # deposit an EPD
    print_section("Depositing an EPD")
    with open("epd.json") as f:
        epd = json.load(f)
        response = requests.post(f"{base_url}/epds", json=epd, headers=headers)
        if response.status_code == 201:
            created_epd_id = response.json()['id']
            print(f"Created new EPD, id: {created_epd_id}")
        else:
            print(f"EPD creation failed with {response.status_code}. {response.text}")

    # now, read it back form API
    print_section("Reading back created EPD from the API")
    if created_epd_id:
        response = requests.get(f"{base_url}/epds/{created_epd_id}", headers=headers)
        if response.status_code == 200:
            print(f"Read back EPD: {pprint(response.json())}")
        else:
            print(f"EPD read failed with {response.status_code}. {response.text}")


def print_section(section_name: str):
    print(SEPARATOR)
    print(f"> {section_name}\n")


if __name__ == "__main__":
    main()
