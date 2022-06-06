def maskCard(card_number):
    card_number=str(card_number)
    str1="*"*(len(card_number)-4)+card_number[-4:]
    return str1

card_number=int(input())
print(maskCard(card_number))