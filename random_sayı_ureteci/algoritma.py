import random

def xor_mod_shuffle_prng(seed, N, M=2**31 - 1):
    """
    XOR + MOD + KARIŞTIRMA tabanlı,
    sonlu ve 0-1 dengesi garanti edilen
    rastgele bit dizisi üretici.
    """

    if N % 2 != 0:
        raise ValueError("N çift olmalıdır (0 ve 1 eşitliği için).")

    original_seed = seed
    bits = []

    # 1. AŞAMA: XOR + MOD tabanlı bit üretimi
    while len(bits) < N:
        seed = (seed ^ (seed << 1)) % M
        bit = seed % 2
        bits.append(bit)

    # 2. AŞAMA: 0 ve 1 dengesini sağlama
    ones = bits.count(1)
    zeros = bits.count(0)
    target = N // 2

    if ones > target:
        diff = ones - target
        for i in range(len(bits)):
            if diff == 0:
                break
            if bits[i] == 1:
                bits[i] = 0
                diff -= 1

    elif zeros > target:
        diff = zeros - target
        for i in range(len(bits)):
            if diff == 0:
                break
            if bits[i] == 0:
                bits[i] = 1
                diff -= 1

    # 3. AŞAMA: Karıştırma (Shuffle)
    random.seed(original_seed)
    random.shuffle(bits)

    return bits


# ÖRNEK KULLANIM
seed = 23
N = 34

bit_dizisi = xor_mod_shuffle_prng(seed, N)
print(bit_dizisi)
print("0 sayısı:", bit_dizisi.count(0))
print("1 sayısı:", bit_dizisi.count(1))
