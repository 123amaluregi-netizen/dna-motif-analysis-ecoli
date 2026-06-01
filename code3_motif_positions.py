from Bio import SeqIO

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

print("Genome ID:", record.id)

print("\nMotif searched:")
print(motif)

print("\nTotal occurrences:")
print(len(positions))

print("\nFirst 20 positions:")
print(positions[:20])
