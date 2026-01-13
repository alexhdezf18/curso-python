"""
Dado un array de numero y un numero goal, encuentra los dos primeros numeros del
array que sumen el numero goal y devuelve sus indices. Si no existe tal combinacion,
devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def find_first_sum(nums, goal):
    for i in nums:
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]
    return None # No se encontro ninguna combinacion


nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal) 
print(result)


"""
Misma solucion pero ahora con un diccionario
"""

def find_first_sum(nums, goal):
    seen = {}
    
    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return [seen[missing], index]
        seen[value] = index
    
    return None
    
nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal) 
print(result)