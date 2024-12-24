def pull(n: int) -> tuple[int, int]:
    pyt = n//90
    if n>=90:
        n-=1
    chetir = n//10
    return chetir, pyt