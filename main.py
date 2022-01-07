from typing import List

def generate_kmers(text: str, k: int) -> List[str]:
  kmers = list()
  for i in range(len(text) - k + 1):
    kmers.append(text[i:i+k])
  return kmers

def kmer_sequence_to_text(kmers: List[str]) -> str:
  text = kmers[0]
  for kmer in kmers[1:]:
    text += kmer[-1]
  return text

def construct_overlap_graph(kmers: List[str]) -> dict:
  """Creates an adjacency graph for the kmers
  """
  graph = {kmer: set() for kmer in kmers}
  for kmer_source in kmers:
    for kmer_target in kmers:
      source_suffix = kmer_source[1:]
      target_prefix = kmer_target[:-1]
      if source_suffix == target_prefix:
        graph[kmer_source].add(kmer_target)
  return graph

# Helper functions

def text_to_lines(text):
  return [t.strip() for t in text.strip().split('\n')]

if __name__ == '__main__':
  inp = """CT
TG
TG
TC
TT
TCG"""
  kmers = text_to_lines(inp)
  print(construct_overlap_graph(kmers))
