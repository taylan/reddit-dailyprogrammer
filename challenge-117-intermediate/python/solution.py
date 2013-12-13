from praw import Reddit
from praw.objects import Submission
from re import compile
from operator import attrgetter

post_re = compile(r'Challenge (?P<chnum>#\d+) (?P<chcat>\[[a-zA-Z]+\]) (?P<chtitle>.*)')


def get_all_posts():
    r = Reddit(user_agent='DailyProg')
    r.config.decode_html_entities = True
    return list(r.get_subreddit('DailyProgrammer').get_hot(limit=1000))


Submission.__str__ = lambda self: '{0} {1} "{2}" {3}'.format(self.chcat, self.chnum, self.chtitle, self.url)


def main():

    posts = []
    for p in get_all_posts():
        src = post_re.search(p.title)
        if not src:
            continue
        for k, v in src.groupdict().items():
            setattr(p, k, v)

        posts.append(p)

    print('Posts sorted by # and category:')
    [print(p) for p in sorted(posts, key=attrgetter('chnum', 'chcat'))]

    print('Posts sorted by category and #:')
    [print(p) for p in sorted(posts, key=attrgetter('chcat', 'chnum'))]






if __name__ == '__main__':
    main()
