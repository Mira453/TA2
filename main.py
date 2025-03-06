import os

def merge_and_count(arr):
    """Алгоритм підрахунку інверсій за допомогою Merge Sort"""
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_and_count(arr[:mid])
    right, right_inv = merge_and_count(arr[mid:])
    merged, split_inv = merge_and_count_split(left, right)

    return merged, left_inv + right_inv + split_inv

def merge_and_count_split(left, right):
    """Злиття двох частин та підрахунок інверсій"""
    i = j = inv_count = 0
    merged = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count

def write_sorted_inversions(user_x, inversion_results, output_file="output.txt"):
    """Запис відсортованих інверсій у файл"""
    sorted_results = sorted(inversion_results, key=lambda x: x[1])

    with open(output_file, "w") as f:
        f.write(f"{user_x}\n")
        for user_id, inversions in sorted_results:
            f.write(f"{user_id} {inversions}\n")

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
    
    index_user = 1
    array_matrix = []
    
    while (index_user <= num_users):
        try:
            num_arr = list(map(int, arr[index_user].split())) # поділила на елементи
        except ValueError:
            print("елемент має бути числом")
            return

        user = num_arr[0]
        arr_el_of_user = num_arr[1:] #елементи які містить юзер
        
        _, inversions_count = merge_and_count(arr_el_of_user)
        array_matrix.append((user, inversions_count))

        index_user += 1

    # Номер головного користувача (X)
    user_x = users[1]

    # Запис у файл
    write_sorted_inversions(user_x, array_matrix)
    print("Файл 'output.txt' успішно створено!")

if __name__ == "__main__":
    main()