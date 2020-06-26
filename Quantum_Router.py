# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:32:08 2020

@author: codie
"""

from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np


#################################User_Input######################

n = int(input("Length of the password[Root]:-")) 
Pass_R = list(map(float,input("Set the Password[Root](Any number between [0,3](Int) with space between each):- ").strip().split()))[:n]
Rand = 2
#Rand = int(input("Enter a random number between [1,10] for your dummey signel creation :- "))
Signal = str(input("Put your Binary signal here:-"))


################################/User_Input#####################

##############################Manual_Input#######################
'''
Rand = [2,3,4]

n = 3
Pass_R= [1,2,3]
Pass = [1,2,6]

Data = [0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,0,1]
'''
##############################/Manual_Input#######################


############################/Algorithm##########################

def Root(Pass,Input):
    m = len(Pass)
    output = 0
    
    if m >= n:
        
        qc = QuantumCircuit()
        
        q = QuantumRegister(3+2*m, 'q')
        c = ClassicalRegister(1, 'c')
        
        qc.add_register(q)
        qc.add_register(c)
        
        qc.u3(np.pi*Input,0,0,q[0])
        qc.u3(np.pi / Rand, 0, 0, q[1])
        for i in range (n):
             qc.u3(np.pi-Pass_R[i], 0, 0, q[3+i])
             
        for i in range(m):
            qc.u3(Pass[i], 0, 0, q[3+i])
            
            
        qc.mct(q[3:3+m], q[2], q[3+m:3+2*m])
        qc.cswap(q[2], q[0], q[1])
        qc.measure(q[1], c[0])
        
        Shots = 1
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc, backend=backend,shots = Shots)
        job_result = job.result()
        output = (list(job_result.get_counts(qc).keys())[0])
            
        #print(job_result.get_counts(qc))
    if m<n:
        
        qc = QuantumCircuit()
        
        q = QuantumRegister(3+2*n, 'q')
        c = ClassicalRegister(1, 'c')
        
        qc.add_register(q)
        qc.add_register(c)
        
        qc.x(q[0])
        qc.u3(np.pi / Rand, 0, 0, q[1])
        for i in range (n):
             qc.u3(np.pi-Pass_R[i], 0, 0, q[3+i])
             
        for i in range(m):
            qc.u3(Pass[i], 0, 0, q[3+i])
            
            
        qc.mct(q[3:3+n], q[2], q[3+n:3+2*n])
        qc.cswap(q[2], q[0], q[1])
        qc.measure(q[1], c[0])
        
        Shots = 1
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc, backend=backend,shots = Shots)
        job_result = job.result()
        output = (list(job_result.get_counts(qc).keys())[0])

        #print(job_result.get_counts(qc))
        
        
        
    return output


#########################/Algorithm##################
    
######################Some_helpful_Function############

def List_To_String(A):
    str = ""
    for i in A:
        str+= i
    return str
def String_To_List(A):
    C = []
    for i in (list(A)):
        C.append(int(i))
    return C

####################/Some_helpful_Function##############
    
###################Output#######################
Data = String_To_List(Signal)

p = 1
while p!=0:
    Output = []
    print("Data has been saved enter password to recover")
    m1 = int(input("Length of your password:-")) 
    Pass = list(map(float,input("Enter your Password:- ").strip().split()))[:m1]
    
    for i in range (len(Data)):
        #print(Root(Pass,Data[i]))
        #print (type(Root(Pass,Data[i])))
        Output.append(Root(Pass,Data[i]))
    print (List_To_String(Output))
    p = int(input("Enter 1 to continue and 0 to Exit :-"))

#################/Output#######################


'''End'''