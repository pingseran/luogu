import sys


def run():
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and i != k:
                    n1 = i * 100 + j * 10 + k
                    n2 = 2 * n1
                    n3 = 3 * n1

                    s1 = str(n1)
                    s2 = str(n2)
                    s3 = str(n3)
                    if (
                        len(s1) == 3
                        and len(s2) == 3
                        and len(s3) == 3
                        and set(s1 + s2 + s3) == set("123456789")
                    ):
                        print(n1, n2, n3)


def main():
    run()


if __name__ == "__main__":
    main()
