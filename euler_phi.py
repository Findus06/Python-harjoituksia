import CoPrimo as cp

def euler_phi(n):
    return len(cp.coPrimo(n))

if __name__ == "__main__":
    print(euler_phi(8)) # 4    
