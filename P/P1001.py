import sys


def main():
    line = sys.stdin.readline()

    nums = list(map(int, line.split()))

    ans = sum(nums)

    print(ans)


if __name__ == "__main__":
    main()
