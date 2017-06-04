import unittest

from twitter_controller.Text import Text


class TextTest(unittest.TestCase):
    def external_links_test(self):
        t = Text('This is a little content',
                 links=['https://twitter.com',
                        'https://twitter.com/no_matter/where/the/path/leads',
                        'http://twitter.com', 'http://www.twitter.com',
                        'http://this.is.really.external.link.com/index.html'])
        self.assertEqual(len(t.get_external_links()), 1)

    def add_test(self):
        t = Text('12', hashtags=['one', 'two'], links=['l1', 'l2', 'l3'])
        p = Text('34', hashtags=['three', 'four'], links=['l3', 'l4'])
        res1 = t + p
        res2 = Text(t.content + p.content,
                    hashtags=(set(t.hashtags + p.hashtags)),
                    links=(t.links + p.links))
        self.assertEqual(res1.get_content(), res2.get_content())
        self.assertEqual(res1.get_external_links(), res2.get_external_links())
        self.assertEqual(str(res1.get_external_links()),
                         str(res2.get_external_links()))


if __name__ == '__main__':
    unittest.main()
