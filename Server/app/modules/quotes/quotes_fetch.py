#!/usr/bin/python
# coding=iso-8859-15
import random
def main():
	quotes_list=[ 'Whatever the mind of man can conceive and believe, it can achieve. –Napoleon Hill','Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.  –Robert Frost','I attribute my success to this: I never gave or took any excuse. –Florence Nightingale','The most difficult thing is the decision to act, the rest is merely tenacity. –Amelia Earhart',' I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. –Maya Angelou','Either you run the day, or the day runs you. –Jim Rohn','Whatever you can do, or dream you can, begin it.  Boldness has genius, power and magic in it. –Johann Wolfgang von Goethe','Do not wait to strike till the iron is hot, but make it hot by striking.– William B. Sprague','Whether you think you can or think you can’t, you’re right.– Henry Ford','You must be the change you want to see in the world.– Mahatma Gandhi','You can get everything in life you want if you will just help enough other people get what they want.– Zig Ziglar','Desire is the starting point of all achievement, not a hope, not a wish, but a keen pulsating desire which transcends everything.– Napoleon Hill','Failure is the condiment that gives success its flavor.– Truman Capote','In any situation, the best thing you can do is the right thing; the next best thing you can do is the wrong thing; the worst thing you can do is nothing.– Theodore Roosevelt','If you keep saying things are going to be bad, you have a chance of being a prophet.– Isaac B. Singer','Setting an example is not the main means of influencing others; it is the only means.– Albert Einstein' ' Remember that happiness is a way of travel, not a destination.– Roy Goodman''If you want to test your memory, try to recall what you were worrying about one year ago today.– E. Joseph Cossman'
	]
	return random.choice(quotes_list)

if __name__ == '__main__':
	print (main())
	

