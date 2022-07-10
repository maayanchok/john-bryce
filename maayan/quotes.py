import random
 
love = [
        "Love all, trust a few, do wrong to none.",
        "You call it madness, but I call it love.",
        "All you need is love.",
        "True love stories never have endings.",
        "Love is shown more in deeds than in words."
    ]
life = [
        "The purpose of our lives is to be happy." ,
        "You only live once, but if you do it right, once is enough.",
        "The big lesson in life, baby, is never be scared of anyone or anything.",
        "Life is not a problem to be solved, but a reality to be experienced.",
        "Don’t settle for what life gives you; make life better and build something.",
    ]
happy = [
        "There is no path to happiness; happiness is the path.",
        "Don't worry. Be happy."
    ]
sad = [
        "Tears come from the heart and not from the brain."
    ]
quotes = [love,life,happy,sad]
weights = [1,1,1,1]

 
your_cate = random.choice(quotes)
your_quote = random.choice(your_cate)
print(your_quote)
print(random.choices(quotes, weights, k = 1))
 
#quote likes
like = input("did you like this quote? y/n ")
if like == "y":
    a=1