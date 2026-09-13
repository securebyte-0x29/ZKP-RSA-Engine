from math_ops.prime_gen import gen_prime
from math_ops.gcd_e_d import generate_d , generate_e

def create_key():
    p = gen_prime()
    q = gen_prime()
    
    while p==q:
        q = gen_prime()
    
    n = p * q 
    phi_n = n - p - q + 1
    
    e = generate_e(phi_n)
    d = generate_d(e,phi_n)
    
    return (e,n), (d,n)
    
def system_keys():
    c_pub_k , c_pvt_k = create_key()
    s_pub_k , s_pvt_k = create_key()
    
    return c_pub_k , c_pvt_k , s_pub_k , s_pvt_k

def encrypt_message(m_array, public_key):
    e, n = public_key 
    l = []
    for m in m_array:
        l.append(pow(m, e, n))
    return l

def decrypt_message(n_array, private_key):
    d, n = private_key
    l = []
    for c in n_array:
        l.append(pow(c, d, n))
    return l

