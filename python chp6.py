# chp6
#kpop 가수와 곡으로 구성된 튜플의 참조
'''
singer = ('bts','볼빨간사춘기','brs','블랙핑크','태연')
song = ('작은 것들을 위한 시','나만,봄','소우주','killthislove','사계')

print(singer)
print(song)

print(singer.count('bts'))
print(singer.index('볼빨간사춘기'))
print(singer.index('bts'))
print()

for i in range(len(singer)):
      print('%s: %s' % (singer[i], song[i]))


kpop = 'bts'#문자
kpop_tu = 'bts',# 튜플
kpoptup = 'bts' # 뒤에 콤마가 안붙었으므로 문자열
kpoptu = ('bts','블랭핑크')#튜플

print(kpop)
print(kpop_tu)
print(kpoptu)

#del kpop_tu
#print(kpop_tu) # kpop_tu 삭제되서 오류

day1 = ('moday','tuesday','wednesday')
day2 = ('thursday','friday','saturday')
day3 = ('sunday',)

day = day1 + day2 + day3
print(type(day))
print(day)

day = day1 + day2 + day3 *3 # day3만 3
print(day)


sports = ['축구','야구','농구','배구']
num = [11,9,5,6]

print(sports)
print(num)

for i in range(len(sports)):
    print('%s: %d명' %(sports[i], num[i]), end = ' ')
print(); print()

#2차원 리스트로 생성

sponum = [sports, num]
print(sponum)

for i in range(len(sponum[0])):
    print('%s: %d명 ' % (sponum[0][i], sponum[1][i]), end = ' ' )
print(); print()

#리스트 컴프리헨션 
psponum = [[sports[i], num[i]] for i in range(len(sports))]
print(psponum)

for one in psponum:
    print('%s : %d명 ' % (one[0], one[1]), end = ' ')
print()
print(len(sports))
'''
#b= list('2020')
#print(b)
'''
lst = [1,5,7,9,11,13,15]

print(lst[:2])
print(lst[-2:-8:-2])

day = list('월화수')
day.insert(0,'일')
print(day)
day.pop()
print(day)
day.remove('일')
print(day)
day.clear()
print(day)

korean = ('정렬','초보자','내포','사전')
english = ('sorting','novice','comprihension','dictionary')

a = input('찾을 단어 입력')

if a in korean:

    if a == '정렬':
        print(english[0])
    elif a == '초보자':
        print(english[1])
    elif a == '내포':
        print(english[2])
    elif a == '사전':
        print(english[3])

#
sports = ['축구','야구','농구','배구']
num = [11,9,5,6]

sports.insert(1 ,' ')
sports.insert(3 ,' ')
sports.insert(5 ,' ')
sports.insert(7 ,' ')

print(sports)

sports[1::2] = num[::]

print(sports)
'''
#일상코딩 6-4 1월에서 9월의 영어단어로 구성딕셔너리

month = {1: 'january', 2: 'February' , 3: 'march', 4: 'april'}
month[5] = 'may'

print(month)  

from random import randint

for i in range(5):
    r = randint(1,5)
    
    print('%d: %s' % (r, month[r])) # r -> key month[r] -> value




