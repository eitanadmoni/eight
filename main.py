def main():
  n = input()
  for i in range(1, n + 1):
    if i % 8 == 0 or str(8) in str(i):
      print("ARAZIM")
    else:
      print(i)
  return

if __name__ == "__main()__":
  main()
