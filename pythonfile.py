def bit_stuffing(data):
    stuffed_data = ""
    count = 0

    for bit in data:
        stuffed_data += bit
        
        if bit == '1':
            count += 1
        else:
            count = 0  # Reset count for '0'
        
        if count == 5:
            stuffed_data += '0'  # Stuff a '0' after five consecutive '1's
            count = 0  # Reset count after stuffing
    
    return stuffed_data

def bit_destuffing(stuffed_data):
    destuffed_data = ""
    count = 0

    i = 0
    while i < len(stuffed_data):
        bit = stuffed_data[i]
        destuffed_data += bit

        if bit == '1':
            count += 1
        else:
            count = 0  # Reset count for '0'

        # If five consecutive '1's are followed by a '0', skip the '0'
        if count == 5:
            i += 1  # Skip the '0' after five consecutive '1's
            count = 0  # Reset count after de-stuffing

        i += 1

    return destuffed_data

# Example usage
data = "011111101111110"
print("Original data:    ", data)

stuffed_data = bit_stuffing(data)
print("Stuffed data:     ", stuffed_data)

destuffed_data = bit_destuffing(stuffed_data)
print("De-stuffed data:  ", destuffed_data)
