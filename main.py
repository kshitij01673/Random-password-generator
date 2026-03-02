import random
allchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?`~"

def generate_password(length):
    password = ""
    for i in range(length):
        password += allchars[random.randint(0, len(allchars)-1)]
    return password

def main():
    length = int(input("Enter the length of the password: "))
    print(f"Your password is: {generate_password(int(length))}")

if __name__ == "__main__":
    main()