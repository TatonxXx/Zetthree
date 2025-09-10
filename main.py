from myfunc import add
from myfunc2 import add
def main():
    try:
        a = float(input("กรอกค่า A: "))
        b = float(input("กรอกค่า B: "))
        result = add(a, b)
        print(f"\nผลลัพธ์ของ A + B คือ: {result}")
    except ValueError:
        print("กรุณากรอกตัวเลขให้ถูกต้อง!")

if __name__ == "__main__":
    main()
