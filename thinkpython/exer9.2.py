word_count = 0
no_e_count = 0

fin = open('word.txt')

for line in fin:
    word = line.strip()
    word_count += 1
    if 'e' not in word:
        no_e_count += 1

print 'word count =', word_count
print 'no e word count =', no_e_count
print 'percentage of no e word is:', 100.0 * no_e_count / word_count, '%'
