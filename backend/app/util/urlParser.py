from urllib import parse

def confirmPttUrl(url):
    if 'http' not in url:
        url = "https://" + url
    result = parse.urlparse(url)
    if 'www.ptt.cc' in result.netloc :
        return url
    else:
        return False