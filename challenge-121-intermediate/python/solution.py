from requests import get
from bs4 import BeautifulSoup, NavigableString
from re import compile, IGNORECASE

link_re = compile("/wiki/(.*)", IGNORECASE)


def has_surrounding_parens(elem):
    return sum([x.string.count('(') - x.string.count(')') for x in filter(lambda x: type(x) == NavigableString, elem.previous_siblings)]) != 0

def get_first_link(article):
    req = get('http://en.wikipedia.org/w/index.php?title={0}&printable=yes'.format(article), headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'})
    if req.status_code != 200:
        return None
    soup = BeautifulSoup(req.text)
    links = list(filter(lambda x: x['href'].startswith('/wiki/') and not has_surrounding_parens(x), soup.select('#mw-content-text > p > a')))
    return link_re.match(links[0]['href']).group(1) if links else None


def main():
    #start = input('Specify starting article: ')
    article = 'Wikipedia'
    path = [article]
    while article != 'Philosophy':
        article = get_first_link(article)
        if not article:
            break
        if article in path:
            print('cycle!')
            break
        print(article)
        path.append(article)

    if article == 'Philosophy':
        print('{0} articles from {1} to Philosophy.'.format(len(path), path[0]))
    else:
        print('Something went wrong somewhere.')

    print(path)


if __name__ == '__main__':
    main()