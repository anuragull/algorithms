# Problem

Given a name find the matching name, the variant can be

* Efficient direct matching
* Phonetic similarity	Jesus ↔ Heyzeus ↔ Haezoos
* Nicknames	William ↔ Will ↔ Bill ↔ Billy
* Missing spaces or hyphens	MaryEllen ↔ Mary Ellen ↔ Mary-Ellen
* Titles and honorifics	Dr. ↔ Mr. ↔ Ph.D.
* Truncated name components	McDonalds ↔ McDonald ↔ McD
* Missing name components	Phillip Charles Carr ↔ Phillip Carr
* Out-of-order name components	Diaz, Carlos Alfonzo ↔ Carlos Alfonzo Diaz
* Initials	J. E. Smith ↔ James Earl Smith
* Names split inconsistently across database fields	Dick. Van Dyke ↔ Dick Van . Dyke
* Same name in multiple languages	Mao Zedong ↔ Мао Цзэдун ↔ 毛泽东 ↔ 毛澤東
* Semantically similar names	Eagle Pharmaceuticals, Inc. ↔ Eagle Drugs, Co.
* Semantically similar names across language

## Name matching techniques

1. Common Key Method : Reduce the names to a code (Soundex/Metaphone)
1. List method : Prepare a list of common possible spelling
1. Edit Distance :
1. Statistical similarity: Needs to train on pairs
1. Approximate String matching :
   1. Finding dictionary strings that match the pattern approximately.
   1. Use of fast indexing and database (suffix-trees, bloom-filters)
1. similarity based approach like min-hash

## Approach

* Create a database
* Create common key using double Metaphone
* Use either edit distance to rank the "common keys"
* Train or use association mining rules to get the confidence score
* Try Approximate string matching


## Literatture Survey

1. http://www.basistech.com/whitepapers/the-name-matching-you-need-EN.pdf
1. https://en.wikipedia.org/wiki/Metaphone
1. https://github.com/oubiwann/metaphone
1. http://www.ece.umd.edu/~oard/pdf/cikm09.
1. https://waset.org/publications/8664/a-comparison-and-analysis-of-name-matching-algorithms-
1. https://pdfs.semanticscholar.org/654d/51abeb59861dde5f8097127a5b5a12147f9f.pdf
