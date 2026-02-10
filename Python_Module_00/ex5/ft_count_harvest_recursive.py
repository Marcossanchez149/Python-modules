
def ft_count_harvest_recursive():
    day = int(input('Days until harvest: '))

    def count_recursive(days, cont):
        if (days + 1 > cont):
            print("Day", cont)
            count_recursive(days, cont + 1)
    cont = 1
    count_recursive(day, cont)
    print("Harvest time!")
