# Leia 3 numeros e informe o maior e o menor
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
n3 = int(input('Informe o último número: '))

nums = [n1, n2, n3]
nums.sort()
print('O maior número foi: {} e o menor: {}'.format(nums[-1], nums[0]))
