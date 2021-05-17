from dwave.system import DWaveSampler
sampler_manual = DWaveSampler(solver={'topology__type': 'chimera'})

# Check if the qubits and couplers are available given the topology of the architecture
qubit_list = [0,1,4,5]
print(f'The intended quibits are available: {all(qubit in sampler_manual.nodelist for qubit in qubit_list) }')
qubit_edges = [(0, 4), (0, 5), (1, 4), (1, 5)]
print(f'The intended couplers are available: {all(coupler in sampler_manual.edgelist for coupler in qubit_edges) }')

# Solve the problem a + b + c = 1
qubit_biases = {(0, 0): 1, (1, 1): -1, (4, 4): -1, (5, 5): 1}
coupler_strengths = {(0, 4): 2, (0, 5): -3, (1, 4): 2, (1, 5): 2}
Q = {**qubit_biases, **coupler_strengths}
iterations = 50000
sampleset = sampler_manual.sample_qubo(Q, num_reads=iterations)


print(sampleset)