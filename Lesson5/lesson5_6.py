import random


def generate_lottery_numbers():
    regular_numbers = []
    # 隨機產生7個不重複的數值,前6個為一般號碼,最後一個為特別號
    random_numbers = random.sample(range(1, 49), 7)
    regular_numbers = sorted(random_numbers[:6])  # 將隨機產生的7個號碼的前6個的排序
    special_number = random_numbers[-1]  # 隨機產生七個號碼最後一個當作特別號
    # 回傳號碼組跟特別號
    return regular_numbers, special_number


def main():

    regular_numbers, special_number = generate_lottery_numbers()
    print(f"大樂透電腦(1-49)選號結果:{regular_numbers}")
    print(f"特別號碼:{special_number}")


if __name__ == "__main__":
    main()
