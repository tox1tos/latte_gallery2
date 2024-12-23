def pull(n: int) -> tuple[int, int]:
    
    guaranteed_4_star = (n // 10) + (1 if n % 10 >= 9 else 0)
    guaranteed_5_star = (n // 90) + (1 if n % 90 >= 89 else 0)
    
    return guaranteed_4_star, guaranteed_5_star

n = int(input())

result = pull(n)
print(f"({result[0]}, {result[1]})")
