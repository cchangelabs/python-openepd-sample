# EC3 Public API Python client example

## References

* Public API (openEPD) for EC3: https://openepd.buildingtransparency.org/#/epds/post_epds
* Documentation on authentication: https://staging.buildingtransparency.org/ec3/manage-apps/api-doc/guide#/02_Accessing_API/01_Authentication.md

## Installing

* Python 3.10 or higher
* Optional: use virtual environment to isolate python packages
  * install venv, and create a virtual environment with `python -m venv venv`
  * switch to it by running `source venv/bin/activate`
* Python packages: requests. Install with `pip install requests`

## Running

* Create an account by registered at [EC3 Staging](https://staging.buildingtransparency.org)
* Contact Apisupport@buildingtransparency.org to get access to EPD Creators permissions
* Create an API key via [Key management section](https://staging.buildingtransparency.org/ec3/manage-apps/keys) with 
  `READ WRITE` scopes. Store the `token` somewhere locally.
* Run `TOKEN=replace_token python ./ec3_public_api_sample.py`, replacing `replace_token` with the token you got from 
  the previous step.

Script would output results of the operation.
Please see json files for object examples.
