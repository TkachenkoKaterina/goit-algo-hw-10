# Обчислення визначеного інтеграла методом Монте-Карло та перевірка результату

## Завдання 2
Обчислити значення визначеного інтеграла функції f(x) = x^2 методом Монте-Карло на інтервалі [0, 2]. Перевірити точність результатів за допомогою аналітичного методу через функцію `quad` з бібліотеки SciPy.

## Порівняльний аналіз результатів
- Метод Монте-Карло: 2.6684
- Метод `quad`: 2.666666666666667 (з похибкою 2.960594732333751e-14)

Метод Монте-Карло дав близьке значення до точного результату, але з певною похибкою. Чим більше випадкових точок буде використовуватись у методі Монте-Карло, тим точніший результат буде отримано. Метод `quad` надає високу точність і підходить для точного обчислення інтегралів.

## Висновки
- Метод Монте-Карло є ефективним для обчислення інтегралів у випадках, коли важко або неможливо знайти аналітичне рішення. Проте, для точніших результатів, таких як у нашому прикладі, метод `quad` є більш надійним.

