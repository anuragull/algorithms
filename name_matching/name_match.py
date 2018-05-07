import argparse
from metaphone import doublemetaphone
import difflib
import edit_dist
import heapq

male_name = 'data/male.txt'
female_name = 'data/female.txt'
all_words = 'data/english_word_ntk.txt'



class NameMatch(object):
    def __init__(self):
        self.all_names = set()
        self.metaphone_dict = {}
        self.set_name_list()

    def set_name_list(self):
        with open(male_name, 'r') as fread:
            for line in fread.readlines():
                self.all_names.add(line.strip('\n'))
        # set metaphone
        for names in self.all_names:
            first, second = doublemetaphone(names)
            self.metaphone_dict[first + second] = names

    def direct_match(self, name):
        if name in self.all_names:
            return True
        return False

    def edit_dist(self, name):
	h = []
	# create a heap with the distances for the word
	for db_name in self.all_names:
	    heapq.heappush(h, (edit_dist.get_edit_dist(name, db_name), db_name))
        top_result = heapq.nsmallest(10, h)
        results = [n for c,n in top_result]
	return results

    def metaphone_match(self, name):
        test_f, test_s = doublemetaphone(name)
        test_metaphone = test_f+test_s
        if test_metaphone in self.metaphone_dict:
	    return self.metaphone_dict[test_metaphone]
        return "None"
    def close_match(self, name):
        return difflib.get_close_matches(name, list(self.all_names), 10)

def driver():
    argp = argparse.ArgumentParser(description="Name matching tool")
    argp.add_argument("Name", type=str, help="name to match in Database")
    argp.add_argument("Mode", type=int, help="Matching mode")
    args = argp.parse_args()

    name_match = NameMatch()
    if args.Mode == 1:
        print("Name %s matches the database %r" % (args.Name, name_match.direct_match(args.Name)))
    if args.Mode == 2:
        print("Name %s matches the metaphone database %s" % (args.Name, name_match.metaphone_match(args.Name)))
    if args.Mode == 3:
        print("Name %s matches list %s" % (args.Name, str(name_match.close_match(args.Name))))
    if args.Mode == 4:
        print("Name %s edit-dist matches %s" % (args.Name, str(name_match.edit_dist(args.Name))))
if __name__ == '__main__':
    driver()
