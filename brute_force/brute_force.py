
def main():
    assert format_time(30) == "30.0 seconds"
    assert format_time(3600) == "1.0 hours"
    assert format_time(31536000) == "1.0 years"

    t = simulate_brute_force(56, 1_000_000_000)
    assert 1.0 < t / 31536000 < 1.5
    
    return 0
    
# mean time to analyse half of keys in keyspace
def simulate_brute_force(key_bits: int, keys_per_second: float):
    return float((2 ** key_bits / 2) / keys_per_second)

# conversion of seconds in more readable string
def format_time(seconds: float):
    if seconds < 60:
        return(f"{seconds:,.1f} seconds")
    elif seconds < 3600:
        return(f"{seconds/60:,.1f} minutes")
    elif seconds < 86400:
        return(f"{seconds/3600:,.1f} hours")
    elif seconds < 31536000:
        return(f"{seconds/86400:,.1f} days")
    else:
        years = round(seconds/31536000, 1)
        return(f"{years:,}" + " years")

def print_keyspace_table(keys_per_second: float):
    key_bits = [8, 16, 32, 40, 56, 64, 80, 128, 256]
    
    print("Key bits |         Possible keys |         Mean attack time")

    for i in key_bits:
        print(str(i) + " | " + str(2**i) + " | " + format_time(simulate_brute_force(i, keys_per_second)))

if __name__ == "__main__":
    main()
