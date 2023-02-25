def your_salary():
    rate = 20
    while True:
        try:
            t_name = input("Enter the teacher's name : ")
            t_period = int(input("Enter the teacher's periods : "))
            if t_period < 0:
                print("periods must be positive !")
            else:
                if t_period <= 100:
                    g_salary = t_period * rate
                elif t_period > 100:
                    n_period = t_period - 100
                    som = n_period * (rate + 5)
                    g_salary = 100 * rate + som
                return print(f"Teacher : {t_name}\nPeriods: {t_period}\nGross salary : {g_salary:,}$")
        except ValueError:
            print("please, respect the format of your entries")


your_salary()    
