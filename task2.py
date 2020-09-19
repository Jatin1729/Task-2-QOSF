#!/usr/bin/env python
# coding: utf-8

# In[140]:


from qiskit import *
from qiskit.quantum_info import Operator, average_gate_fidelity
from math import pi
import numpy as np
import cmath
a1 = complex(0,1)
op_1 = Operator([[a1, 0],
                  [0, a1]])

from qiskit.visualization import plot_bloch_multivector, plot_histogram
qc = QuantumCircuit(2,2)
# Applied H-gate = iRx(pi)Ry(pi/2):
#Applied X-gate = iRx(pi)
# here unitary gate is global phase i
qc.ry(pi/2,0)
qc.rx(pi,0)
qc.unitary(op_1,[0])


# Applied C-NOT gate to both qubits
qc.cx(0,1)
# Applied X-gate to first qubit
qc.rx(pi,0)
qc.unitary(op_1,[0])

qc.draw()
print(qc)


# In[141]:


# Let's see the result
backend = Aer.get_backend('statevector_simulator')
final_state = execute(qc,backend).result().get_statevector()
print (final_state)


# In[ ]:





# In[146]:


qc.measure([0],[0])
qc.measure([1],[1])
emulator = Aer.get_backend('qasm_simulator')
job = execute(qc, emulator, shots=1000 )
hist = job.result().get_counts()
plot_histogram(hist)


# In[ ]:




