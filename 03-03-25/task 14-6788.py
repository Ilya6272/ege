for x in range(68):
    num1 = 1*68**4 + 2*68**3 + 3*68**2 + x*68 + 5
    num2 = 1*68**4 + x*68**3 + 2*68**2 + 3*68 + 3
    num = num1 + num2
    if num % 12 == 0:
        print(num // 12)

