from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 

def bin(str1):
	str2 = str1[::-1]
	x = 0
	binary = 0
	lengthstr2 = len(str2)
	for x in range(0,lengthstr2):
		if str2[x] == "1":
			temp = pow(2,x)	
			binary = binary+temp
	return binary


txt = "aaabbbcccddd"
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
# in Python 3.1+:
# symb2freq = collections.Counter(txt)
huff = encode(symb2freq)
print "Symbol\tWeight\tHuffman Code"
for p in huff:
    print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])
