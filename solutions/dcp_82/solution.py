remainder = ""


def readN(n):
    global remainder
    result = remainder
    text = None
    while len(result) < n and (text is None or len(text) >= 5):
        text = read7()
        result += text
    remainder = result[n:]
    return result[:n]
