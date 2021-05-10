def main():
    less20 = ["null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
              "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    less100 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    f1 = open('textdemo.txt', 'r+')
    f1.write("\ninput converts numbers to words\n")

    for line in f1.readlines():
        line = line.lstrip();
        line = line.rstrip();
        if line.isdigit():
            if int(line) < 20:
                for i in range(20):
                    if line == str(i):
                        print(line + "  " + less20[i], end='\n')
                        f1.write(line + "  " + less20[i] + '\n')
                        break
            elif int(line) in range(20, 100):
                a = int(line) // 10
                b = int(line) % 10
                if b == 0:
                    print(line + "  " + less100[a - 2], end='\n')
                    f1.write(line + "  " + less100[a - 2] + '\n')
                elif b > 0:
                    print(line + "  " + less100[a - 2] + "-" + less20[b], end='\n')
                    f1.write(line + "  " + less100[a - 2] + "-" + less20[b] + '\n')
            elif int(line) in range(100, 1000):
                c = int(line) // 100
                d = int(line) % 100
                if d == 0:
                    print(line + "  " + less20[c] + " hundred ", end='\n')
                    f1.write(line + "  " + less20[c] + " hundred" + '\n')
                elif d > 0:
                    if d < 20:
                        for i in range(20):
                            if str(d) == str(i):
                                print(line + "  " + less20[c] + " hundred and " + less20[i], end='\n')
                                f1.write(line + "  " + less20[c] + " hundred and " + less20[i] + '\n')
                                break
                    elif d >= 20:
                        a = d // 10
                        b = d % 10
                        if b == 0:
                            print(line + "  " + less20[c] + " hundred and " + less100[a - 2], end='\n')
                            f1.write(line + "  " + less20[c] + " hundred and " + less100[a - 2] + '\n')
                        elif b > 0:
                            print(line + "  " + less20[c] + " hundred and " + less100[a - 2] + "-" + less20[b], end='\n')
                            f1.write(line + "  " + less20[c] + " hundred and " + less100[a - 2] + "-" + less20[b] + '\n')

                print("Output file is created.")
    f1.close()


if __name__ == '__main__':
    main()
