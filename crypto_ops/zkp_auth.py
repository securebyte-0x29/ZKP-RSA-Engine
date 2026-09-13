import random

def run_zkp(client_pub):
    print("ZKP Handshake")
    e, n = client_pub
    
    s = random.randint(2, n - 2)
    pub_v = pow(s, e, n)
    print("Client public token : ",pub_v)
    
    r = random.randint(2, n - 2)
    x = pow(r, e, n)
    print("Client commitment : ",x)
    
    c = random.choice([0, 1])
    print("Server sends : ",c)

    if c == 0:
        y = r % n
    else:
        y = (r * s) % n
        
    print("Client sends response : ",y)
    
    left_side = pow(y, e, n)
    right_side = (x * pow(pub_v, c, n)) % n
    
    if left_side == right_side:
        print("SUCCESS: ZKP Accessed")
        return True
    else:
        print("FAILED: ZKP Denied")
        return False