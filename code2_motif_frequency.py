from Bio import SeqIO

record = SeqIO.read(
"/storage/emulated/0/Download/genome/ncbi_dataset/data/GCA_000005845.2/GCA_000005845.2_ASM584v2_genomic.fna",
"fasta"
)

genome = str(record.seq)

motif = "TATAAT"

count = genome.count(motif)

print("Genome ID:", record.id)

print("\nSearching motif:")
print(motif)

print("\nNumber of occurrences:")
print(count)
