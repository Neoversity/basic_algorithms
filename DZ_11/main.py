def find_coins_greedy(amount):
    """
    Функція жадібного алгоритму для видачі решти.
    
    Параметри:
    amount (int): Сума для видачі решти.
    
    Повертає:
    dict: Словник з номіналами монет і їх кількістю.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount):
    """
    Функція динамічного програмування для видачі решти з мінімальною кількістю монет.
    
    Параметри:
    amount (int): Сума для видачі решти.
    
    Повертає:
    dict: Словник з номіналами монет і їх кількістю.
    """
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    # Динамічне програмування для знаходження мінімальної кількості монет
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    # Відновлення результату
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
        
    return dict(sorted(result.items()))

def main():
    """
    Головна функція для взаємодії з користувачем.
    """
    while True:
        # Меню вибору алгоритму
        print("Виберіть алгоритм для видачі решти:")
        print("1. Жадібний алгоритм")
        print("2. Динамічне програмування")
        print("3. Вихід")
        choice = input("Введіть номер опції (1, 2, 3): ")

        if choice == '3':
            print("Вихід з програми. До побачення!")
            break

        amount = int(input("Введіть суму для видачі решти: "))

        if choice == '1':
            # Виклик жадібного алгоритму
            result = find_coins_greedy(amount)
            print("Результат жадібного алгоритму:", result)
        elif choice == '2':
            # Виклик алгоритму динамічного програмування
            result = find_min_coins(amount)
            print("Результат динамічного програмування:", result)
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
