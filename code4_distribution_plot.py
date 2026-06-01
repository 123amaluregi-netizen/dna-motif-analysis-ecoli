from Bio import SeqIO
import matplotlib.pyplot as plt

record = SeqIO.read(
"/storage/emulated/0/Download/genome/ncbi_dataset/data/GCA_000005845.2/GCA_000005845.2_ASM584v2_genomic.fna",
"fasta"
)

genome = str(record.seq)

motif = "TATAAT"

positions = []

for i in range(len(genome)):
    if genome[i:i+len(motif)] == motif:
        positions.append(i)

plt.figure(figsize=(10, 2))

plt.plot(positions, [1]*len(positions), '|')

plt.xlabel("Genome Position")
plt.title("Distribution of TATAAT Motifs in E. coli Genome")

plt.show()
