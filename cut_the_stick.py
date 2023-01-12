def cutTheSticks(arr):
    # Write your code here
    no_of_stick = []
    new = []

    while len(arr) > 0 :
        small_stick = min(arr)
        no_of_stick.append(len(arr))
        new = []
        for i in range ( 0 ,len(arr)):
            val = arr[i] - small_stick
            if val > 0 :
                new.append(val)

        arr = new

    return no_of_stick



                

            




arr=[1, 2 ,3 ,4 ,3, 3 ,2 ,1]

print(cutTheSticks(arr))