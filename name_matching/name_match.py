import argparse
from metaphone import doublemetaphone

male_name = 'data/male.txt'
female_name = 'data/female.txt'
all_words = 'data/english_word_ntk.txt'

class NameMatch(object):
    def __init__(self):
        self.all_names = set()
        self.metaphone_set = set()
        self.set_name_list()

    def set_name_list(self):
        with open(male_name, 'r') as fread:
            for line in fread.readlines():
                self.all_names.add(line.strip('\n'))
        # set metaphone

    for names in self.all_names:
        first, second = doublemetaphone(names)
        self.metaphone_set.add(first + second)

    def direct_match(self, name):
        if name in self.all_names:
            return True
        return False

    def edit_dist(self, name):
        pass

    def metaphone_match(self, name):
        test_f, test_s = doublemetaphone(name)
        test_metaphone = test_f+test_s
        if test_metaphone in self.metaphone_set:
            return True
        return False

def driver():
    argp = argparse.ArgumentParser(description="Name matching tool")
    argp.add_argument("Name", type=str, help="name to match in Database")
    argp.add_argument("Mode", type=int, help="Matching mode")
    args = argp.parse_args()

    name_match = NameMatch()
    if args.Mode == 1:
        print("Name %s matches the database %r" % (args.Name, name_match.direct_match(args.Name)))
    if args.Mode == 2:
        print("Name %s matches the metaphone database %r" % (args.Name, name_match.metaphone_match(args.Name)))

if __name__ == '__main__':
    driver()