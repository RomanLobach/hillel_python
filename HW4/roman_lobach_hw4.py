# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.

sentence1 = 'Hello! My name is Bob, I\'m python developer.'
sentence2 = 'The eager beaver leaped over the sleeping sheep'

def words_with_two_vowel(input_sentence): # пишу функцію для компактності коду
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    str_sliced = input_sentence.split() if type(input_sentence) is str else str(input_sentence).split()
    word_counter = 0 # лічильник слів з двома голоснимі підряд

    for word in str_sliced:
        letter_counter = 0 # лічильник голосних

        for letter in word:
            # ЯКЩО літера голосна - по-перше: інкрементую лічильник літер, по-друге: якщо він дорівнює 2, інкрементую лічильник слів з двома голоснимі підряд. ІНАКШЕ (якщо літера приголосна) - обнуляю лічильник літер
            if letter in vowels:
                letter_counter = letter_counter + 1

                if letter_counter == 2:
                    word_counter = word_counter + 1
            else:
                letter_counter = 0

    
    return print(f'> For sentence: "{input_sentence}" number of words with two vowels in a row: {word_counter}')

words_with_two_vowel(sentence1) # > For sentence: "Hello! My name is Bob, I'm python developer." number of words with two vowels in a row: 0
words_with_two_vowel(sentence2) # > For sentence: "The eager beaver leaped over the sleeping sheep" number of words with two vowels in a row: 5

print('------------------------')

# --------------------------
# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

store_price_list = { 
    "cito": 47.999, 
    "BB_studio": 42.999, 
    "momo": 49.999, 
    "main-service": 37.245, 
    "buy.now": 38.324, 
    "x-store": 37.166, 
    "the_partner": 38.988, 
    "store": 37.720, 
    "rozetka": 38.003
}

def filtered_stores_by_price(stores, lower_limit, upper_limit):
    filtered_stores = []
    result_message = '> match:'
    for key, value in stores.items():
        if value >= lower_limit and value <= upper_limit:
            filtered_stores.append(key)

    if not filtered_stores:
        return print('> There is no matched stores in yor price range!')
    else:
        for store in filtered_stores:
            result_message = result_message + f' {str(store)},'
        
        return print(result_message)

filtered_stores_by_price(store_price_list, 35.9, 37.339) # > match: main-service, x-store,
filtered_stores_by_price(store_price_list, 47, 50) # > match: cito, momo,
filtered_stores_by_price(store_price_list, 0, 2) # > There is no matched stores in yor price range!
filtered_stores_by_price(store_price_list, 0, 100) # > match: cito, BB_studio, momo, main-service, buy.now, x-store, the_partner, store, rozetka,