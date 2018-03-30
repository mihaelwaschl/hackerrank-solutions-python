numE = int(input())
english = set(map(int, input().strip().split()))
numF = int(input())
french = set(map(int, input().strip().split()))

print(len(english.difference(french)))