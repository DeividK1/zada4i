import webbrowser

# Въпрос и очакван отговор
question = "КОЙ Е ИЗПЪЛНИТЕЛЯ НА МАМИНО АНЧЕ?"
correct_answer = "ВЛАДИ МАРКОВ"

# Въведи отговор
answer = input(question + "")

# Проверка на отговора
if answer.lower() == correct_answer.lower():
    print("Правилен отговор!")
    youtube_url = "https://www.youtube.com/watch?v=U3v-gVNFJSU"  # Въведи URL на песента
    webbrowser.open(youtube_url)
else:
    print("Грешен отговор.")
