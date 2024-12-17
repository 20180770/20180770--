#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

# 학생 정보 생성코드
def generate_students(count=30):
    students = []
    for _ in range(count):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 두 글자 이름 생성
        age = random.randint(18, 22)  # 나이 18~22 사이
        score = random.randint(0, 100)  # 성적 0~100 사이
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬
def selection_sort(students, key, reverse=False):
    n = len(students)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (students[j][key] < students[idx][key]) ^ reverse:
                idx = j
        students[i], students[idx] = students[idx], students[i]

# 삽입 정렬
def insertion_sort(students, key, reverse=False):
    n = len(students)
    for i in range(1, n):
        key_item = students[i]
        j = i - 1
        while j >= 0 and (key_item[key] < students[j][key]) ^ reverse:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_item

# 퀵 정렬
def quick_sort(students, left, right, key, reverse=False):
    if left < right:
        pivot_index = partition(students, left, right, key, reverse)
        quick_sort(students, left, pivot_index - 1, key, reverse)
        quick_sort(students, pivot_index + 1, right, key, reverse)

def partition(students, left, right, key, reverse):
    pivot = students[right][key]
    i = left - 1
    for j in range(left, right):
        if (students[j][key] < pivot) ^ reverse:
            i += 1
            students[i], students[j] = students[j], students[i]
    students[i + 1], students[right] = students[right], students[i + 1]
    return i + 1

# 기수 정렬
def counting_sort(students, key, exp):
    n = len(students)
    output = [{} for _ in range(n)]
    count = [0] * 10

    for student in students:
        index = student[key] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = students[i][key] // exp
        output[count[index % 10] - 1] = students[i]
        count[index % 10] -= 1
    
    for i in range(n):
        students[i] = output[i]

def radix_sort(students, key):
    max_score = max(student[key] for student in students)
    exp = 1
    while max_score // exp > 0:
        counting_sort(students, key, exp)
        exp *= 10

# 학생 정보 출력
def print_students(students):
    for student in students:
        print(student)

# 메인
def main():
    students = generate_students()
    
    print("생성된 학생 정보:")
    print_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        
        choice = input("정렬 기준을 선택하세요 (1, 2 ,3, 4): ")
        
        if choice == '4':
            print("프로그램을 종료합니다.")
            break
        
        if choice in ['1', '2', '3']:
            sort_key = ''
            if choice == '1':
                sort_key = '이름'
            elif choice == '2':
                sort_key = '나이'
            elif choice == '3':
                sort_key = '성적'
            
            print("정렬 방식 선택: 1. 오름차순, 2. 내림차순")
            order_choice = input("선택하세요 (1-2): ")
            reverse = True if order_choice == '2' else False
            
            print(f"\n{sort_key} 기준으로 정렬합니다...")
            
            # 정렬 알고리즘 선택
            print("정렬 알고리즘 선택: 1. 선택 정렬, 2. 삽입 정렬, 3. 퀵 정렬, 4. 기수 정렬 (성적 기준)")
            algo_choice = input("선택하세요 (1-4): ")
            
            if algo_choice == '1':
                selection_sort(students, sort_key, reverse)
            elif algo_choice == '2':
                insertion_sort(students, sort_key, reverse)
            elif algo_choice == '3':
                quick_sort(students, 0, len(students) - 1, sort_key, reverse)
            elif algo_choice == '4' and sort_key == '성적':
                radix_sort(students, sort_key)
            else:
                print("잘못된 선택입니다.")
                continue
            
            print("정렬된 학생 정보:")
            print_students(students)
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()


# In[ ]:




