class LinkData(object):
    def __init__(self, link: str, is_short_link: bool, number_of_hits: int, number_of_links: int = 0,
                 number_of_different_users: int = 0):
        self.link = link
        self.is_short_link = is_short_link
        self.number_of_different_users = number_of_different_users
        self.number_of_links = number_of_links
        self.number_of_hits = number_of_hits

    def to_dict(self):
        return {'link': self.link, 'numberOfHits': self.number_of_hits, "numberOfSubLinks": self.number_of_links,
                'numberOfDifferentUsers': self.number_of_different_users, "isShortLink": self.is_short_link}
