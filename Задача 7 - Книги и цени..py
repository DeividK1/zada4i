# Дефиниране на променливите за книгите и техните цени
book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book2_name = "Learn You a Haskell"
book2_price = 0
book3_name = "The Healthy Programmer"
book3_price = 50
book4_name = "Code Complete"
book4_price = 60
book5_name = "The Pragmatic Programmer"
book5_price = 20
book6_name = "Pro Git"
book6_price = 0
book7_name = "Introduction to Algorithms"
book7_price = 80
book8_name = "Concrete Mathematics"
book8_price = 100

# Списък с книги и цени
books = [
    (book1_name, book1_price),
    (book2_name, book2_price),
    (book3_name, book3_price),
    (book4_name, book4_price),
    (book5_name, book5_price),
    (book6_name, book6_price),
    (book7_name, book7_price),
    (book8_name, book8_price)
]

# Изпринтване на всяка книга с нейната цена
print("Налични книги и техните цени:")
for name, price in books:
    print(f"{name}: ${price}")

# Изчисляване на сумата на всички книги
total_price = sum(price for _, price in books)
print(f"\nСумата на всички книги е: ${total_price}")

# Изчисляване на общия брой на книгите
total_books = len(books)
print(f"Общият брой на всички книги е: {total_books}")

# Изчисляване на цената при 25% намаление за Introduction to Algorithms и Concrete Mathematics
discounted_price = (book7_price + book8_price) * 0.75
print(f"\nЦената за Introduction to Algorithms и Concrete Mathematics след 25% намаление е: ${discounted_price:.2f}")

# Изчисляване на броя на книгите, които могат да бъдат купени с бюджет от $150
budget = 150
affordable_books = []
affordable_books_price = 0

# Сортиране на книгите по цена възходящо
sorted_books = sorted(books, key=lambda x: x[1])

# Добавяне на книги докато не достигнем бюджета
for name, price in sorted_books:
    if affordable_books_price + price <= budget:
        affordable_books.append(name)
        affordable_books_price += price

print(f"\nС бюджет от $150 може да се купят следните книги ({len(affordable_books)} броя):")
for name in affordable_books:
    print(f"- {name}")
print(f"Обща цена: ${affordable_books_price}")
