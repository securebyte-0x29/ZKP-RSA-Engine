def text_ascii(txt):
    x = []
    for ch in txt:
        x.append(ord(ch))
    return x

def ascii_text(arr):
    s = ""
    for num in arr:
        s+=chr(num)
    return s
