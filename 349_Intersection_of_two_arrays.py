def quick_sort(data, left, right):
    i = left  # 左のインデックス
    j = right  # 右のインデックス
    pivot = data[(left + right) // 2]  # 軸となる値

    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]  # 交換
        i += 1
        j -= 1

    # 再帰処理
    if left < j:
        quick_sort(data, left, j)
    if right > i:
        quick_sort(data, i, right)


if __name__ == "__main__":
    list = [7,8,3,9,0,0,9,1,5]
    quick_sort(list, 0, len(list))
    print(list)