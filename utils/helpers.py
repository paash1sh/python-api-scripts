# simple helper functions i keep reusing
# makes it easier to check responses

def check_status(response, expected=200):
    if response.status_code == expected:
        print(f"  PASS - status code is {expected}")
        return True
    else:
        print(f"  FAIL - expected {expected} but got {response.status_code}")
        return False

def check_field_exists(data, field):
    if field in data:
        print(f"  PASS - field '{field}' exists")
        return True
    else:
        print(f"  FAIL - field '{field}' missing from response")
        return False

def check_not_empty(value, name):
    if value:
        print(f"  PASS - '{name}' is not empty")
        return True
    else:
        print(f"  FAIL - '{name}' is empty")
        return False

def print_response_info(response):
    print(f"  URL: {response.url}")
    print(f"  Status: {response.status_code}")
    print(f"  Time: {response.elapsed.total_seconds()}s")
# helpers
# helpers
# helpers
