# from flask import Flask

# 第3章
# 複数行の処理
print("""これは、とても、とても
とても、とても長い複数行の
コードです。""")

# 改行されたスクリプト
print\
("""これは、とても、とても
とても、とても長い複数行の
コードです。""")

# インクリメント
x = 10
x += 1
print(x)
# デクリメント
x = 10
x -= 1
print(x)

# not演算子
x = 100
print(x == 100)
print(not x == 100)

# if-else文
home = "火星"
if home == "日本":
    print(f"Hello! {home}!")
elif home == "アメリカ":
    print(f"Hello! {home}!")
elif home == "中国":
    print(f"Hello! {home}!")
elif home == "イギリス":
    print(f"Hello! {home}!")
elif home == "フランス":
    print(f"Hello! {home}!")
elif home == "ドイツ":
    print(f"Hello! {home}!")
else:
    print(f"Hello! World!")


# 第4章
# 関数の作成
def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)

# 関数にreturnがない場合はNoneを返す
def f():
     z = 1 + 2

result = f()
print(result)

# 組み込み関数
print\
(len("Monty")
,str(100)
,int("100")
,int(20.54)
,float(100)
,float("16.4")
,float(99)
)

# 入力（input関数）
# age = input("Enter your age:")
# int_age = int(age)
# if int_age < 21:
#     print("You are young!")
# else:
#     print("Wow, you are old!")

# 必須引数とオプション引数
def add_it(x, y = 10):
    return x + y

result = add_it(2, 5)
print(result)
result = add_it(2)
print(result)

# 例外処理（try except）
# try:
#     a = input("type a number:")
#     b = input("type another:")
#     a = int(a)
#     b = int(b)
#     print(a / b)
# except(ZeroDivisionError, ValueError):
#     # 条件はOR条件となる
#     print("Invalid input.")

# ドキュメンテーション文字列
def add(x, y):
    """
    :param x: int.
    :param y: int.
    :return: int sum of x and y
    """
    return x + y


# 第5章
# リスト（イテラブル、ミュータブル）
# colors = ["purple", "orange", "green"]
# guess = input("何色でしょう？")
# if guess in colors:
#     print("当たり！")
# else:
#     print("はずれ")

# タプル（イテラブル、イミュータブル）
dys = ("1984", "Brave New World", "Fahrenheit 451")
print(dys[1])
print("1984" in dys)

# 辞書型（ミュータブル）
fruits = {"Apple": "Red",
          "Banana": "Yellow"}
print(fruits)
# キー・バリューの追加
fruits["Kiwi"] = "Green"
print(fruits)
# キーでの参照
print(fruits["Kiwi"])
# キーの検索（バリューでの検索ではない）
print("Kiwi" in fruits)
print("Green" in fruits)
# キーの削除
del fruits["Kiwi"]
print(fruits)
# サンプル
# songs = {"1": "fun",
#         "2": "blue",
#         "3": "me",
#         "4": "floor",
#         "5": "live"}
# n = input("数字を入力してください：")
# if n in songs:
#     song = songs[n]
#     print(song)
# else:
#     print("見つかりません。")

# コンテナのネスト
lists = []
rap = ["カニエ・ウエスト", "ジェイ・Z", "エミネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッド・テッド", "ティエスト"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)

rap = lists[0]
rap.append("ケンドリック・ラマー")
print(rap)
print(lists)


# 第6章
# 書式化
# what = input("何が：")
# when = input("いつ：")
# where = input("どこで：")
# do = input("どうした：")
# r = f"{what}は{when}に{where}で{do}。"
# print(r)

# 分割（split）
print("今日も、元気です！".split("."))
# 結合（join）
words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(words)
print(one)
# 空白除去（strip）
s = "  The   "
s = s.strip()
print(s)
# 置換え（replace）
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)
# インデックス検索（index）※例外処理もよく使う
try:
    ind = "animals".index("a")
    print(ind)
except:
    print("Not found.")
# エスケープ文字
print("彼女は\"そうだね\"と言った")
# 改行
print("line1\nline2\nline3")


# 第7章
# ループ
name = "Ted"
for character in name:
    print(character)

shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)

people = {"G.Bluth IT": "A.Develoment"
          ,"Barney": "HIMYM"
          ,"Dennis": "Always Sunny"}
for character in people:
    print(character)

tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i = i + 1
print(tv)

tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []
for show in tv:
    show = show.upper()
    all_shows.append(show)
for i, show in enumerate(tv):
    show = tv[i]
    show = show.upper()
    all_shows.append(show)
for show in coms:
    show = show.upper()
    all_shows.append(show)
for i, show in enumerate(coms):
    show = coms[i]
    show = show.upper()
    all_shows.append(show)
print(all_shows)

# 整数の生成（range）
for i in range(1, 11):
    print(i)

# whileループ（無限ループの中断は対話シェルでCtrl+C）
# x = 10
# while x > 0:
#     print(f"{x}")
#     x -= 1
# print("Happy New Year!")
#
# # whileループ+break（%剰余を使った繰り返し）
# qs = ["What is your name?",
#       "What is your fav. color?",
#       "What is your quest?"]
# n = 0
# while True:
#     print("Type q to quit")
#     a = input(qs[n])
#     if a == "q":
#         break
#     n = (n + 1) % len(qs)

# continue
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# ループのネスト（外側のループと内側のループのバランスに注意。3回以上ネストする場合は再考）
for i in range(1, 4):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

# while input("y or n?") != "n":
#     for i in range(1, 6):
#         print(i)


# 第8章
# モジュール
import math
print(math.pow(2,3))
import random
print(random.randint(0,100))
import statistics
nums = [1, 5, 23, 56, 12, 89, 56, 72, 50, 67, 98, 15]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))
import keyword
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
# 自作の別モジュールの読み込み
import hello
hello.print_hello()
import module1


# 第9章
# ファイルパスの取得（os.path.join）
import os
path = os.path.join("Users", "Sashiro", "Murayama", "PycharmProjects", "Self-Taught_Programmer", "st.txt")
print(path)
# ファイルの書き出し（withを使うことで閉じ忘れを防止）
st = open("st.txt", "w", encoding="utf-8")
st.write("Hi from Python!")
st.close()
with open("st.txt", "a", encoding="utf-8") as f:
    f.write("\nHi from Python!")

# ファイルの読み込み
with open("st.txt", "r", encoding="utf-8") as f:
    print(f.read())
with open("st.txt", "r", encoding="utf-8") as f:
    temp = f.read()
    my_list = temp.split("\n")
print(my_list)

# csvの読み込み・書き込み
import csv
with open("st.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])
with open("st.csv", "r", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
# 出力先の確認
print(os.getcwd())


# 第10章
# ハングマン
# def hangman():
#     wlist = ["cat", "dog", "apple", "ball"]
#     word = random.choice(wlist)
#     wrong = 0
#     stages = ["",
#              "________        ",
#              "|               ",
#              "|        |      ",
#              "|        0      ",
#              "|       /|\     ",
#              "|       / \     ",
#              "|               "
#               ]
#     rletters = list(word)
#     board = ["_"] * len(word)
#     win = False
#     print("ハングマンへようこそ！")
#
#     while wrong < len(stages) - 1:
#         print("\n")
#         msg = "1文字を予想してね"
#         char = input(msg)
#         if char in rletters:
#             cind = rletters.index(char)
#             board[cind] =char
#             rletters[cind] = "$"
#         else:
#             wrong += 1
#         print(" ".join(board))
#         e = wrong + 1
#         print("\n".join(stages[0:e]))
#         if "_" not in board:
#             print("あなたの勝ち!")
#             print(" ".join(board))
#             win = True
#             break
#     if not win:
#         print("\n".join(stages[0:wrong+1]))
#         print(f"あなたの負け！正解は{word}")
# hangman()

# 第12章
# 手続き型
x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)

# 関数型
def increment(a):
    return a + 1
print(increment(5))

# オブジェクト型
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

orl= Orange(10, "dark Orange")
print(orl)
print(orl.weight)
print(orl.color)
orl.weight = 100
orl.color = "light orange"
print(orl)
print(orl.weight)
print(orl.color)
orl1 = Orange(10, "dark orange")
orl2 = Orange(100, "light orange")
orl3 = Orange(50, "yellow orange")
orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())


# 第13章
# オブジェクト指向：カプセル化
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n
# ダメな変更方法
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)
# 変更メソッドなどを用いる方がよい（文頭に"_"をつけているのがプライベート変数）
data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

# 継承
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print(f"{self.width} by {self.len}")

my_shape = Shape(20, 25)
my_shape.print_size()
# ここで子クラスを定義
class Square(Shape):
    # pass
    def area(self):
        return self.width * self.len
    # メソッドオーバーライド（上書き）
    def print_size(self):
        print(f"I am {self.width} by {self.len}")

a_square = Square(20, 20)
a_square.print_size()
print(a_square.area())

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name
# PersonオブジェクトをDogオブジェクトの変数に使う
mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)


# 第14章
# クラス変数
class Rectangle:
    # クラス変数（メソッドの外で宣言する）：リストにタプルを入れる
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print(f"{self.width} by {self.len}")

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)
print(Rectangle.recs)

# 特殊メソッド
# 特殊メソッド__repr__をオーバーライド
class Lion:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
lion = Lion("Dilbert")
print(lion)

# 特殊メソッド__add__を付与
class AlwaysPositibe:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)
x = AlwaysPositibe(-20)
y = AlwaysPositibe(10)
print(x + y)

# is:同じメソッドか（ら派生しているか）を判別
class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)
another_bob = Person()
print(bob is another_bob)

# 第15章
# 戦争ゲーム
class Card:
    # クラス変数
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    # メソッド
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.value < c2.value:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.value > c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2)
print(card1 > card2)

card = Card(3, 2)
print(card)

from random import shuffle
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                # Cardクラスを呼び出し
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

deck = Deck()
for card in deck.cards:
    print(card)

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレイヤー1の名前")
        name2 = input("プレイヤー2の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = f"このラウンドは{winner}が勝ちました"
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = f"{p1n}は{p1c}、{p2n}は{p2c}を引きました！"
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を開始します！")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print(f"ゲーム終了、{win}の勝利です！")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"

# game = Game()
# game.play_game()


# 第17章
import re
l = "Beautiful is better than ugly"
matches = re.findall("beautiful", l, re.IGNORECASE)
print(matches)
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
m = re.findall("^If", zen, re.MULTILINE)
print(m)

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__",t)
for match in found:
    print(match)

# 第18章
# import sys
# print(sys.path)
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"
app.run(port=8000)

