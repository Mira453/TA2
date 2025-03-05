import os

def main():
    file_path = r'example/input_2_1000.txt' #папка з zip

    if not os.path.exists(file_path):
        print(f"такий файл '{file_path}' не існує.")
        return
    if os.path.getsize(file_path) == 0:
        print("файл порожній")
        return
    with open(file_path, 'r') as file:
        arr = file.read().splitlines()
    first_str = arr[0]
    print("перша строка:", first_str)
    users = first_str.split(' ')
    index_user = 1

    try:
        num_users = int(users[0])
    except ValueError:
        print("елемент має бути числом")
        return
    array_matrix = []
    while (index_user <= num_users):
        try:
            num_arr = list(map(int, arr[index_user].split())) # поділила на елементи
        except ValueError:
            print("елемент має бути числом")
            return

        user = num_arr[0]
        arr_el_of_user = num_arr[1:] #елементи які містить юзер
        print("user:", user)
        print("елементи:", arr_el_of_user)


        for j in range( 1 ,len(num_arr)) :
            array_matrix.append([index_user, num_arr[j]])#матриця юзера та його елементів
        index_user = index_user+1
    print(array_matrix)
if __name__ == "__main__":
    main()