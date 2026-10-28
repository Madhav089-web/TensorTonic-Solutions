import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    # pass
    if(isinstance(x,float)) or (isinstance(x,int)):
        return 1/(1+np.exp(-1.0*x))
    if (isinstance(x,list)):
        u=np.asarray(x,dtype=float)
        
        # for i in x:
        #     u.append( 1/(1+np.exp(-1.0 * i)))
        return 1/(1+np.exp(-1.0*u))
        