def calculate_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def generate_e(phi_n):
    for e in range(2,phi_n):
        if calculate_gcd(e,phi_n) == 1:
            return e
        
def generate_d(e,phi_n):
    k = 1
    while True:
        if (k * phi_n + 1)% e == 0:
            return (k*phi_n+1)//e 
        k+=1
