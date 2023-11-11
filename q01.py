# q01.py
from pkg.modu import triangle_zhonxin

def main():
    print("請輸入三角形的 3 個頂點坐標")
    print("------------------------------")

    a_input = input("請輸入頂點 a 的坐標：")
    b_input = input("請輸入頂點 b 的坐標：")
    c_input = input("請輸入頂點 c 的坐標：")

    a = tuple(map(int, a_input.split(',')))
    b = tuple(map(int, b_input.split(',')))
    c = tuple(map(int, c_input.split(',')))

    print("------------------------------")

    centroid = triangle_zhonxin(a, b, c)

    print(f"此三角形的重心為：({centroid[0]}, {centroid[1]})")

if __name__ == "__main__":
    main()
