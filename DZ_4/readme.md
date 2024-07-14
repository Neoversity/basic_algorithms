# Звіт про аналіз алгоритмів сортування

## Опис

Цей звіт містить порівняння трьох алгоритмів сортування: злиттям, вставками та Timsort, на різних наборах даних і розмірах масивів.

## Алгоритми сортування

- **Merge Sort**: Алгоритм сортування злиттям.
- **Insertion Sort**: Алгоритм сортування вставками.
- **Timsort**: Вбудований в Python алгоритм сортування.

## Набори даних

- **Випадковий**: Випадково згенерований масив.
- **Відсортований**: Вже відсортований масив.
- **Частково відсортований**: Частково відсортований масив (перша половина відсортована, друга випадкова).
- **Зворотньо відсортований**: Масив, відсортований у зворотному порядку.

## Результати

### Розмір даних: 100

| Алгоритм       | Випадковий                  | Відсортований               | Частково відсортований      | Зворотньо відсортований     |
| -------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| Merge Sort     | 0.000115 - 0.000118 seconds | 0.000103 - 0.000104 seconds | 0.000109 - 0.000111 seconds | 0.000106 - 0.000113 seconds |
| Insertion Sort | 0.000159 - 0.000173 seconds | 0.000008 seconds            | 0.000079 - 0.000089 seconds | 0.000304 seconds            |
| Timsort        | 6.2e-06 - 4.4e-06 seconds   | 1.3e-06 seconds             | 2.7e-06 seconds             | 1.3e-06 seconds             |

### Розмір даних: 1000

| Алгоритм       | Випадковий                  | Відсортований               | Частково відсортований      | Зворотньо відсортований     |
| -------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| Merge Sort     | 0.001590 - 0.001931 seconds | 0.001360 - 0.001366 seconds | 0.001463 - 0.002759 seconds | 0.001373 - 0.001987 seconds |
| Insertion Sort | 0.018705 - 0.025288 seconds | 9.2e-05 - 9.86e-05 seconds  | 0.009061 - 0.012541 seconds | 0.034150 - 0.036023 seconds |
| Timsort        | 8.4e-05 - 8.42e-05 seconds  | 9.2e-06 - 1.23e-05 seconds  | 4.28e-05 - 4.87e-05 seconds | 9.7e-06 - 1.0e-05 seconds   |

### Розмір даних: 5000

| Алгоритм       | Випадковий                  | Відсортований               | Частково відсортований      | Зворотньо відсортований     |
| -------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| Merge Sort     | 0.009735 - 0.009588 seconds | 0.009120 - 0.008158 seconds | 0.010108 - 0.010009 seconds | 0.008487 - 0.010064 seconds |
| Insertion Sort | 0.550140 - 0.507692 seconds | 0.000517 - 0.000493 seconds | 0.256355 - 0.288016 seconds | 1.009960 - 1.037123 seconds |
| Timsort        | 0.000540 - 0.000547 seconds | 5.4e-05 - 5.31e-05 seconds  | 0.000307 - 0.000304 seconds | 5.31e-05 - 5.53e-05 seconds |

### Розмір даних: 10000

| Алгоритм       | Випадковий                  | Відсортований               | Частково відсортований      | Зворотньо відсортований     |
| -------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| Merge Sort     | 0.021849 - 0.021860 seconds | 0.019134 - 0.017802 seconds | 0.019786 - 0.020626 seconds | 0.018820 - 0.019879 seconds |
| Insertion Sort | 2.282144 - 2.164111 seconds | 0.001016 - 0.001013 seconds | 1.077263 - 1.006059 seconds | 4.284513 - 4.174381 seconds |
| Timsort        | 0.001218 - 0.001354 seconds | 0.000155 - 0.000151 seconds | 0.000790 - 0.000752 seconds | 0.000176 - 0.000168 seconds |

## Висновки

1. **Timsort**:

   - Найбільш ефективний алгоритм для всіх типів даних і розмірів масивів.
   - Відмінно працює на відсортованих та частково відсортованих наборах даних, показуючи найменші часи виконання.

2. **Merge Sort**:

   - Показує стабільну продуктивність на всіх типах даних, але поступається Timsort.
   - Виграє у Insertion Sort на великих наборах даних, особливо на зворотньо відсортованих.

3. **Insertion Sort**:
   - Дуже ефективний на малих наборах даних і відсортованих масивах.
   - Дуже неефективний на великих і зворотньо відсортованих масивах через свою квадратичну складність.

## Загальний висновок

Результати підтверджують, що алгоритм Timsort є найбільш ефективним серед усіх трьох алгоритмів сортування на різних наборах даних і розмірах масивів. Він забезпечує найкращу продуктивність для випадкових, відсортованих і частково відсортованих масивів, особливо на великих наборах даних. У той час як Merge Sort показує стабільну продуктивність на всіх типах даних, він поступається Timsort. Insertion Sort демонструє хороші результати на малих і відсортованих масивах, але стає дуже неефективним на великих і зворотньо відсортованих масивах через свою квадратичну складність. Таким чином, використання вбудованих функцій сортування Python (Timsort) є найкращим вибором для більшості випадків.