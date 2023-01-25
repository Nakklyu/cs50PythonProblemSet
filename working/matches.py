import re

lst = []

def main():
    time = input("time: ")
    print(matcher(time))

def matcher():
    while True:
        try:
            time = input("Time: ")
            matches = re.search(
            r"^([0-9]|1[0-2])((?::[0-5][0-9])?) (AM|PM) to ([0-9]|1[0-2])((?::[0-5][0-9])?) (AM|PM)$",
                time
            )
            for i in range(6):
                lst.append(matches.group(i + 1))
            if matches:
                return lst
        except AttributeError:
            print("Invalid!")
            continue
    
if __name__ == "__main__":
    main()