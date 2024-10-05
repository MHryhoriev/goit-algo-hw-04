## Аналіз продуктивності алгоритмів сортування

### Огляд

У цьому аналізі порівнюються три алгоритми сортування:
- **Сортування злиттям** (Merge Sort)
- **Сортування вставками** (Insertion Sort)
- **Timsort** (вбудована функція сортування в Python)

Я протестував кожен алгоритм на трьох різних наборах даних: 100, 1000 та 10000 елементів. Мета полягала в тому, щоб спостерігати час виконання кожного алгоритму та підтвердити їх теоретичну складність у практичних умовах.

### Підсумок результатів

#### Набір даних розміром 100 елементів
- **Сортування злиттям**: ~0.000705 секунд
- **Сортування вставками**: ~0.000895 секунд
- **Timsort**: ~0.000022 секунд

#### Набір даних розміром 1000 елементів
- **Сортування злиттям**: ~0.010600 секунд
- **Сортування вставками**: ~0.132306 секунд
- **Timsort**: ~0.000560 секунд

#### Набір даних розміром 10000 елементів
- **Сортування злиттям**: ~0.156469 секунд
- **Сортування вставками**: ~14.152589 секунд
- **Timsort**: ~0.008638 секунд

### Висновки

1. **Сортування злиттям** демонструє стабільну продуктивність і добре масштабується з ростом розміру набору даних. Його продуктивність відповідає очікуваній складності $O(n \ log \ n)$. Однак, хоча цей алгоритм працює добре для середніх наборів даних, він поступається за швидкістю Timsort.

2. **Сортування вставками** працює відносно добре на малих наборах даних, але його продуктивність різко погіршується зі збільшенням розміру набору, що відображає його квадратичну складність $O(n^2)$. Для набору з 10000 елементів час виконання був значно повільнішим, ніж у сортування злиттям і Timsort, що робить його непридатним для великих масивів даних.

3. **Timsort** значно перевершує обидва інші алгоритми в усіх протестованих сценаріях. Це очікувано, враховуючи його гібридний підхід, який поєднує найкращі аспекти сортування злиттям і вставками, та оптимальну продуктивність для реальних шаблонів даних (із найгіршою складністю $O(n \ log \ n)$ ).

### Рекомендації

- **Timsort** варто використовувати за замовчуванням для сортування загального призначення, особливо коли продуктивність важлива для великих наборів даних.
- **Сортування злиттям** залишається хорошим варіантом для ситуацій, де потрібна стабільна та передбачувана продуктивність сортування для різних розмірів наборів даних.
- **Сортування вставками** підходить лише для дуже малих наборів даних або майже відсортованих даних через його погану масштабованість.
