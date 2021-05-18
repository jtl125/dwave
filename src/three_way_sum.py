from dwave.system import DWaveSampler, EmbeddingComposite
sampler_manual = DWaveSampler(solver={'topology__type': 'chimera'})

# Check if the qubits and couplers are available given the topology of the architecture
qubit_list = [0,1,4,5]
print(f'The intended quibits are available: {all(qubit in sampler_manual.nodelist for qubit in qubit_list) }')
qubit_edges = [(0, 4), (0, 5), (1, 4), (1, 5)]
print(f'The intended couplers are available: {all(coupler in sampler_manual.edgelist for coupler in qubit_edges) }')


manual = False
if manual:
    # Define the problem a + b + c = 1 using the manual embedding
    qubit_biases = {(0, 0): 1, (1, 1): -1, (4, 4): -1, (5, 5): 1}
    coupler_strengths = {(0, 4): 2, (0, 5): -3, (1, 4): 2, (1, 5): 2}
    solver = DWaveSampler(solver={'topology__type': 'chimera'})
else: 
    # Define the same problem using the automatic embedding
    qubit_biases = {('a', 'a'): -1, ('b', 'b'): -1, ('c', 'c'): -1}
    coupler_strengths = {('a', 'b'): 2, ('b', 'c'): 2, ('a', 'c'): 2}
    solver = EmbeddingComposite(DWaveSampler(solver={'topology__type': 'chimera'}))

Q = {**qubit_biases, **coupler_strengths}
iterations = 5000
sampleset = solver.sample_qubo(Q, num_reads=iterations)

print(sampleset)