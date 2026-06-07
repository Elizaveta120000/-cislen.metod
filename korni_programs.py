import math
import matplotlib.pyplot as plt

lg = math.log10
ln = math.log
sin = math.sin
cos = math.cos


# ---------- общий метод половинного деления ----------
def bisect(f, a, b, eps):
    n = 0
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        n += 1
    return (a + b) / 2, n


# ---------- общий метод простой итерации ----------
def iterate(phi, x0, eps, maxn=1000):
    x = x0
    for n in range(maxn):
        xn = phi(x)
        if abs(xn - x) < eps:
            return xn, n + 1
        x = xn
    return x, maxn


# ==================================================================
# 2.1. Отделение корней (таблица знаков + график).
# ==================================================================
def skrin1():
    print("=== СКРИН 1: отделение корней ===")

    fa = lambda x: lg(x) + 6 - x ** 2          # а) lg x + 6 = x^2
    fb = lambda x: x * sin(x) - 1              # б) x sin x - 1 = 0

    print("а) lg x + 6 - x^2:")
    for x in [1e-7, 1e-6, 1e-5, 1, 2, 2.5, 2.55, 3]:
        print("   f(%g) = %+.5f" % (x, fa(x)))
    print("   -> корни около 1e-6 и на [2.5; 2.55]")

    print("б) x sin x - 1:")
    for x in [0, 1, 1.1, 1.2, 1.5708]:
        print("   f(%g) = %+.5f" % (x, fb(x)))
    print("   -> наименьший ненулевой корень на [1.1; 1.2]\n")

    # графики
    xs = [0.01 + i * 0.01 for i in range(400)]
    plt.figure(figsize=(9, 4))
    plt.subplot(1, 2, 1)
    plt.plot(xs, [lg(x) + 6 for x in xs], label="lg x + 6")
    plt.plot(xs, [x ** 2 for x in xs], label="x^2")
    plt.title("a) lg x + 6 = x^2"); plt.legend(); plt.grid(True); plt.ylim(0, 8)
    xs2 = [i * 0.02 for i in range(1, 200)]
    plt.subplot(1, 2, 2)
    plt.plot(xs2, [sin(x) for x in xs2], label="sin x")
    plt.plot(xs2, [1 / x for x in xs2], label="1/x")
    plt.title("б) x sin x = 1"); plt.legend(); plt.grid(True); plt.ylim(-1, 3)
    plt.tight_layout(); plt.savefig("skrin1_graph.png", dpi=110)
    print("График: skrin1_graph.png\n")


# ==================================================================
# 2.2. Половинное деление x sin x - 1 = 0, eps = 1e-4.
# ==================================================================
def skrin2():
    print("=== СКРИН 2: половинное деление x sin x - 1 = 0 (eps=1e-4) ===")
    f = lambda x: x * sin(x) - 1
    x, n = bisect(f, 1.1, 1.2, 1e-4)
    print("   корень x = %.4f  (за %d делений)\n" % (x, n))


# ==================================================================
# 2.3(2). Метод простой итерации x sin x - 1 = 0, eps = 1e-5.
# ==================================================================
def skrin3():
    print("=== СКРИН 5.2: простая итерация x sin x - 1 = 0 (eps=1e-5) ===")
    phi = lambda x: 1 / sin(x)                 # x = 1/sin x
    x = 1.1
    n = 0
    print("    n      x_n          x_(n+1)        |разность|")
    while True:
        xn = phi(x)
        print("   %2d  %.7f   %.7f   %.2e" % (n, x, xn, abs(xn - x)))
        if abs(xn - x) < 1e-5:
            break
        x = xn
        n += 1
    print("   корень x = %.5f  (за %d итераций)\n" % (xn, n + 1))


if __name__ == "__main__":
    skrin1()
    skrin2()
    skrin3()
