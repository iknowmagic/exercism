def response(hey_bob: str) -> str:
    bob_trim = hey_bob.strip()

    if bob_trim.strip() == "":
        return "Fine. Be that way!"
    elif bob_trim == bob_trim.upper() and bob_trim != bob_trim.lower():
        if bob_trim[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif bob_trim[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
