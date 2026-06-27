import re
import sys

"""
sample script to clean E.164 phone numbers

PER GOOGLE ADS:
The E.164 format requires the following information:
- Plus sign (+)
- Country Code (CC)
- National Destination Code (NDC)
- Subscriber Number (SN)

"""

# -------------------
# core cleaning logic
# -------------------

def extract_digits(phone: str) -> str:
    """Strip everything except digits."""
    return re.sub(r"\D", "", phone)

output = extract_digits('+1(614)220-2073')

def scrub_phone(original: str, default_code: str = "1") -> dict:
    """
    input: raw phone number string

    output: a dictionary with
        original - raw input
        cleaned - formatted number
        e164 - e164 formatted number
        value - bool if number is valid or not
        notes - debugging/processing notes

    """
    # building results dictionary to populate
    result = {
        "original": original,
        "cleaned": None,
        "e164": None,
        "valid": False,
        "notes": None,
    }

    if not original or not original.strip():
        result["notes"] = "no phone number supplied"
        return result

    # checking if phone number starts with a plus sign
    original_stripped = original.strip()
    number_starts_plus = original_stripped.startswith("+")

    # extracting digts only
    digits = extract_digits(original_stripped)

    if not digits:
        result["notes"] = "no digits found in supplied value"
        return result

    # create country code / digits
    country_code = default_code
    print(f'{country_code=}')
    subscriber = digits
    print(f'{subscriber=}')

    if number_starts_plus or len(digits) > 10:
        # attempt to match a known 1- or 2-digit country code at the front of string
        match_cc = re.match(r"^(1|7|2[07]|3[0-469]|4[013-9]|5[1-8]|6[0-6]|8[1246]|9[0-58])(\d+)$", digits)
        if match_cc:
            country_code = match_cc.group(1)
            print(f'{country_code=}')
            subscriber = match_cc.group(2)
            print(f'{subscriber=}')
        else:
            # fallback: treat first digit as country code if >10 digits
            country_code = digits[0]
            print(f'{country_code=}')
            subscriber = digits[1:]
            print(f'{subscriber=}')

    # validate subscriber length
    if country_code == "1":
        # north america: exactly 10 subscriber digits
        if len(subscriber) != 10:
            result["notes"] = f"north america number must have 10 digits (got {len(subscriber)})"
            return result

        # north america area code can't start with 0 or 1
        if re.match(r"^[01]", subscriber):
            result["notes"] = "Invalid north america area code (starts with 0 or 1)"
            return result

        # north america exchange (middle 3) can't start with 0 or 1
        if re.match(r"^\d{3}[01]", subscriber):
            result["notes"] = "Invalid north america exchange (starts with 0 or 1)"
            return result

        area, exchange, line = subscriber[:3], subscriber[3:6], subscriber[6:]
        result["cleaned"] = f"+1 ({area}) {exchange}-{line}"
        result["e164"] = f"+1{subscriber}"

    else:
        # international attempt: accept 6–12 subscriber digits (rough-ish heuristic)
        if not (6 <= len(subscriber) <= 12):
            result["notes"] = f"Subscriber number length {len(subscriber)} is unusual (expected 6–12)"
            return result

        result["cleaned"] = f"+{country_code} {subscriber}"
        result["e164"] = f"+{country_code}{subscriber}"

    result["valid"] = True
    return result

# test cases
scrub_phone('614-220-9082')
scrub_phone('+44 20 7123 4567')

