class Url:
    def __init__(self, scheme, authority, path, query, fragment):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __str__(self):
        self.Url = ''
        if len(self.scheme) > 0:
            self.Url += self.scheme + ':'
        if len(self.authority) > 0:
            self.Url += '//' + self.authority
        if len(self.path) > 0 and self.path is not None and isinstance(self.path, list):
            self.Url += f"'/'{'/'.join(self.path)}"
        if len(self.query) > 0 and self.query is not None and isinstance(self.query, dict):
            self.Url += f"'?'{'&'.join([f'{k}={v}' for k, v in self.query.items()])}"
        if len(self.fragment) > 0:
            self.Url += '#' + self.fragment
        return self.Url

class HttpsUrl(Url):
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__(self, scheme, authority, path, query, fragment)
        self.sheme = 'https'

class HttpUrl(Url):
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__(self, scheme, authority, path, query, fragment)
        self.sheme = 'http'

class GoogleUrl (HttpsUrl):
    def __init__(self, sheme, authority, path, query, fragment):
        super().__init__(self, sheme, authority, path, query, fragment)
        self.authority = 'google.com'

class WikiUrl (HttpsUrl):
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__(self, scheme, authority, path, query, fragment)
        self.authority = 'wikipedia.org'


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'
