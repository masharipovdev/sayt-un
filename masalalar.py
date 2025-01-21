# # # Mani raqamim 10 shundan vazifalani bajarib boshladim

# # # Foydalanuvchi kiritgan so‘zning palindrom ekanligini aniqlaydigan dastur yozing. Palindrom
# # # – bu orqadan o‘qiganda ham xuddi oldingidek o‘qiladigan so‘z (masalan, "madam",
# # # "racecar").



# # def palindrom(soz):
# #     return soz == soz[::-1]

# # soz = input("So'zni kiriting: ")
# # if palindrom(soz):
# #     print(f"{soz} — bu palindrom.")
# # else:
# #     print(f"{soz} — bu palindrom emas.")


# # def wikipedia(javob):
# #     return javob == javob
# # javob = (f"Palindrom - bir xil o'qiladigan gap , so'zlar va raqamlar .
# #          Bu yunoncha Palindromon so'zidan kelib chiqqan bo'lib, teskari, orqa-old degan ma'noni anglatadi.")
# # wiki = input(f"Wikipediyani o'qish uchun wiki so'zini yozing: ")
# # if wikipedia(javob):
# #     print( f"{javob}bu wikipediyadan olingan. ")

# # # 11-ni Topshiriqni ishladim

# # def multiply(a, b):
# #     result = 0
# #     for _ in range(abs(b)):
# #         result += a
# #     return result if b >= 0 else -result

# # # solani girishi
# # son1 = 5
# # son2 = 3
# # natija = multiply(son1, son2)
# # print(natija)




# def Butun_sonla(rim):
#     # Rim raqamlarini yozib chiqsaq
#     rim_raqamlari = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     natija = 0  # Natijani saqlash uchun o‘zgaruvchi
#     Oldingi_raqamni_qiymati = 0  # Oldingi raqamni qiymati
#     # Rim raqamlarini orqadan o‘qish
#     for char in reversed(rim):
#         qiymat = rim_raqamlari[char]  # Hozirgi raqamning qiymatini olish
#         # Agar oldingi qiymat katta bo'lsa, chiqaramiz
#         if qiymat < Oldingi_raqamni_qiymati:
#             natija -= qiymat
#         else:
#             natija += qiymat
#         Oldingi_raqamni_qiymati = qiymat  # Hozirgi qiymatni oldingi sifatida saqlaymiz
#     return natija  # Yakuniy natijani qaytoramiz
# #chiqarishimiz un print bn qilamiz
# print(Butun_sonla("XIV"))  # 14
# print(Butun_sonla("XX"))   # 20






# def find_max(a, b):
#     return (a + b + abs(a - b)) // 2

# # Misol:
# print(find_max(5, 10))  # Natija: 10

# def reverse_number(num):
#     return int(str(num)[::-1])

# # Misol:
# print(reverse_number(12345))  # Natija: 54321

# def is_armstrong(num):
#     digits = [int(digit) for digit in str(num)]
#     power = len(digits)
#     return sum([digit ** power for digit in digits]) == num

# # Misol:
# print(is_armstrong(153))  # Natija: True
# print(is_armstrong(123))  # Natija: False



import random

# Insonning javoblari
human_responses = [
    "Salom ishlar qalay?",
    "Men kitob o'qishni yoqtiraman.",
    "Sening sevimli ovqating qanday?",
    "Qiziq, sen suniy intellekt haqida nima bilasan.",
    "Bugun havo yaxshi, shunday emasmi?"
]

# Sun’iy intellekt javoblari
ai_responses = [
    "Salom, menda hammasi yaxshi savol uchun rahmat.",
    "Men kop vazifalarni bajarish uchun yaratilganman.",
    "Mening sevimli ovqatim – malumotlar.",
    "Suniy intellekt kop vazifalarni bajarishga yordam beradi.",
    "Ob-havo – kop narsalarni rejalashtrish uchun muhim.",
    "Ishni reja bilan boshlash juda muhim."
]


# Tyuring testi funksiyasi
def turing_test():
    # PEAS modeli uchun o'zgaruvchilarni ishga tushirish
    correct_guesses = 0
    total_questions = 5  # Savollar soni

    print("Tyuring testiga xush kelibsiz.")

    for i in range(total_questions):
        print(f"\nSavol {i + 1}:")
        print("ismingiz nima:")
        # Tasodifiy inson yoki sun'iy intellekt javobi tanlanadi
        if random.choice([True, False]):
            response = random.choice(human_responses)  # Mashina odamdek javob beradi
            is_human_like = True
        else:
            response = random.choice(ai_responses)  # Mashina SI ga o’xshab javob beradi
            is_human_like = False

        print("Javob: ", response)

        # Foydalanuvchidan javob kimga tegishli ekanini so'rash
        print("Sizningcha, bu insonmi yoki sun'iy intellektmi? (inson/suniy intellekt):")
        guess = input().lower()

        # Natijani tekshirish
        if (guess == "inson" and is_human_like) or (guess == "suniy intellekt" and not is_human_like):
            print("To'g'ri!")
            correct_guesses += 1
        else:
            print("Noto'g'ri.")

    # Umumiy natijani chiqarish
    print("\nTest yakunlandi.")
    print(f"Sizning to'g'ri javoblaringiz: {correct_guesses}/{total_questions}")

# Dasturni ishga tushurish
if __name__ == "main":
    turing_test()