from Bio import SeqIO
import matplotlib.pyplot as plt

record = SeqIO.read(
"/storage/emulated/0/Download/genome/ncbi_dataset/data/GCA_000005845.2/GCA_000005845.2_ASM584v2_genomic.fna",
"fasta"
)

genome = str(record.seq)

motifs = ["TATAAT", "TTGACA", "GCGCGC"]

counts = []

for motif in motifs:
    count = genome.count(motif)
    counts.append(count)

    print(f"{motif}: {count}")

plt.bar(motifs, counts)

plt.xlabel("Motifs")
plt.ylabel("Occurrences")
plt.title("Comparison of DNA Motif Frequencies")

plt.show()
