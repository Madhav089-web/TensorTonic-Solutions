import numpy as np
def Expected(C:list)->list:
    ...
    e=[]
    nc=len(C[0])
    nr=len(C)

    Sum=0
    for i in range(nr):
        print(i)
        e.append([])
        for j in range(nc):
            Sum+=C[i][j]
            
    for i in range(nr):
        for j in range(nc):
            ...
            sr=sum(C[i])
            sc=sum([C[a][j] for a in range(nr)])
            exepected=sr*sc/Sum
            e[i].append(exepected)
    return e
            
            

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    expected=Expected(C)
    chi=0
    nc=len(C[0])
    nr=len(C)
    for i in range(nr):
        for j in range(nc):
            chi+=(C[i][j]-expected[i][j])**2/expected[i][j]
    return {
        "chi2":chi,
        "expected":np.array(expected),
    }
    
    # Write code here
    # pass
    # c=np.array(C)
    
    