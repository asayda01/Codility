def valid_password(string1):
    letter_count = 0
    digit_count = 0
    for character in string1:
        if character.isalpha():
            letter_count += 1
        elif character.isdigit():
            digit_count += 1
        else:
            return False

    return letter_count % 2 == 0 and digit_count % 2 == 1

def solution(S):
    words = S.split(' ')

    max_valid_length = -1
    for word in words:
        if valid_password(word):
            max_valid_length = max(len(word), max_valid_length)

    return max_valid_length


S1 = "test 5 a0A pass007 ?xy1"
car1 =  solution(S1)
print(car1)


S2 = "a"
car2 =  solution(S2)
print(car2)


S3 = "tes11"
car3 =  solution(S3)
print(car2)