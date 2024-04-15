from singleton import Singleton

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        print("Factorial of 10:", s1.factorial(10))
    else:
        print("Singleton failed, variables contain different instances.")

