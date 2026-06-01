from Bio import SeqIO

record = SeqIO.read(
"/storage/emulated/0/Download/genome/ncbi_dataset/data/GCA_000005845.2/GCA_000005845.2_ASM584v2_genomic.fna",
"fasta"
)

print("Genome loaded successfully")

print("\nGenome ID:")
print(record.id)

print("\nGenome Length:")
print(len(record.seq))

print("\nFirst 200 DNA Bases:")
print(record.seq[:200])
