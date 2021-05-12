from tokenizers import Tokenizer
import tqdm
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from Bio import SeqIO
from pathlib import Path
from random import sample

# parameters go here, for conversion to argparse etc
sample_size=0.01
path = "contigs/"

files = [str(x) for x in Path(path).glob("**/*.txt")]


tokenizer=Tokenizer(BPE())
# range for vocab_size on partee's paper: 7500 -> 10000 (see page 10:
# https://scholar.smu.edu/cgi/viewcontent.cgi?article=1150&context=datasciencereview)
trainer = BpeTrainer(initial_alphabet=['a','g','c','t'])

tokenizer.train(files[:4], trainer)

tokenizer.save(path="json/BPE-4-contigs.json")
import pdb; pdb.set_trace()
