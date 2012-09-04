# Noun Pluralizer
# Michael Simpson 27/06/11
# michaelesimp@gmail.com

import re
import sys

rule_tuple = (
('[ml]ouse$', '([ml])ouse$', '\\1ice'), 
('child$', 'child$', 'children'), 
('booth$', 'booth$', 'booths'), 
('foot$', 'foot$', 'feet'), 
('ooth$', 'ooth$', 'eeth'), 
('l[eo]af$', 'l([eo])af$', 'l\\1aves'), 
('sis$', 'sis$', 'ses'), 
('man$', 'man$', 'men'), 
('ife$', 'ife$', 'ives'), 
('eau$', 'eau$', 'eaux'), 
('lf$', 'lf$', 'lves'), 
('[sxz]$', '$', 'es'), 
('[^aeioudgkprt]h$', '$', 'es'), 
('(qu|[^aeiou])y$', 'y$', 'ies'), 
('$', '$', 's')
)

def regex_rules(rules=rule_tuple):
  for rule in rules:
    pattern, search, replace = rule
    yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)

def pluralize(noun):
  for rule in regex_rules():
    result = rule(noun)
    if result: 
      return result

if __name__ == '__main__':

  print "\n---------------------------------"
  print "|	Noun Pluralizer		|"
  print "---------------------------------\n"

  while True:
    noun = raw_input("Enter the word to pluralize or exit if you're done: ")
	
    if noun == "exit":
      sys.exit()
	
    print "\n" + pluralize(noun)
	
    print "\n---------------------------------"