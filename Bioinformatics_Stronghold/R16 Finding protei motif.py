# http://saradoesbioinformatics.blogspot.com/2016/07/finding-protein-motif.html

from urllib.request import urlopen


from Bio import SeqIO
import re

ID = []
with open('sample.txt') as f:
    for line in f:
        ID.append(line.strip())

for i in range(len(ID)):
    URL = 'http://www.uniprot.org/uniprot/' + ID[i] + '.fasta'
    data = urlopen(URL)
    fasta = data.read().decode('utf-8', 'ignore')
    with open('seq_file.fasta', 'a') as text_file:
        text_file.write(fasta)

handle = open('seq_file.fasta', 'r')
motifs = re.compile(r'(?=(N[^P][ST][^P]))')
count = 0
for record in SeqIO.parse(handle, 'fasta'):
    sequence = record.seq
    positions = []
    for m in re.finditer(motifs, str(sequence)):
        positions.append(m.start() + 1)
    if len(positions) > 0:
        print(ID[count])
        print(' '.join(map(str, positions)))
    count += 1