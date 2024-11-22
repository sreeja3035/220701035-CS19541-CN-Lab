import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])

def calc_redundant_bits(m):
    r = 0
    while (2**r < m + r + 1):
        r += 1
    print(f"Number of redundant bits: {r}")  # Display the number of redundant bits
    return r

def pos_redundant_bits(data, r):
    j = 0
    k = 0
    m = len(data)
    res = ''
    print("Placing redundant bits at positions: ", end="")
    for i in range(1, m + r + 1):
        if i == 2**j:
            res = res + '0'
            print(i, end=" ")  
            j += 1
        else:
            res = res + data[k]
            k += 1
    print()
    return res

def calc_parity_bits(arr, r):
    n = len(arr)
    arr = list(arr)
    parity_output = "Parity Bits: "
    for i in range(r):
        parity = 0
        position = 2**i
        for j in range(1, n+1):
            if j & position:
                parity ^= int(arr[j-1])
        arr[position-1] = str(parity)
        parity_output += f"[Position {position}: {parity}] "
    print(parity_output.strip())  
    return ''.join(arr)

def detect_and_correct(data, r):
    n = len(data)
    res = 0
    for i in range(r):
        parity = 0
        position = 2**i
        for j in range(1, n+1):
            if j & position:
                parity ^= int(data[j-1])
        if parity != 0:
            res += position

    if res != 0:
        print(f"Error detected at position: {res}")
        data = list(data)
        if res <= n:
            data[res - 1] = '0' if data[res - 1] == '1' else '1'
            print(f"Error corrected at position: {res}")
        else:
            print("Error position out of range. No correction performed.")
        corrected_data = ''.join(data)
        return corrected_data
    else:
        print("No error detected.")
        return data

def remove_redundant_bits(data, r):
    j = 0
    original_data = ''
    for i in range(1, len(data) + 1):
        if i == 2**j:
            j += 1
        else:
            original_data += data[i-1]
    return original_data

def introduce_error(data, position):
    if position < 1 or position > len(data):
        print("Error position is out of range.")
        return data
    data = list(data)
    data[position - 1] = '0' if data[position - 1] == '1' else '1'
    print(f"Introduced error at position: {position}")
    return ''.join(data)

def sender(text):
    binary_data = text_to_binary(text)
    m = len(binary_data)
    r = calc_redundant_bits(m)
    arr = pos_redundant_bits(binary_data, r)
    arr = calc_parity_bits(arr, r)
    print(f"Sender output (binary with redundant bits): {arr}")
    return arr

def receiver(data):
    r = calc_redundant_bits(len(data))
    print(f"Binary with error: {data}")
    corrected_data = detect_and_correct(data, r)
    print(f"Binary after error correction: {corrected_data}")
    original_data = remove_redundant_bits(corrected_data, r)
    ascii_output = binary_to_text(original_data)
    print(f"Decoded text: {ascii_output}")

if __name__ == "__main__":
    input_text = input("Enter the text to be encoded: ")
    channel_data = sender(input_text)
    corrupted_data = introduce_error(channel_data, 2)
    receiver(corrupted_data)