from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from Bio import SeqIO
from pathlib import Path
from random import sample

# parameters go here, for conversion to argparse etc
sample_size=0.1
path = "../amr/azithromycin/"

# read in the data
files = [str(x) for x in Path(path).glob("**/*.fna")]
data = ["".join([str(contig.seq) for contig in SeqIO.parse(isolate, "fasta")]) for isolate in files]

# now we follow partee's sampling scheme to make our tokenizer
samples = sample(data, round(len(data) * sample_size))

tokenizer=Tokenizer(BPE())
# range for vocab_size on partee's paper: 7500 -> 10000 (see page 10:
# https://scholar.smu.edu/cgi/viewcontent.cgi?article=1150&context=datasciencereview)
trainer = BpeTrainer(initial_alphabet=['a','g','c','t'], vocab_size=10000)

tokenizer.train_from_iterator(samples, trainer)
tokenizer.save(f"json/BPE-{sample_size*100}-percent.json")
import pdb; pdb.set_trace()
