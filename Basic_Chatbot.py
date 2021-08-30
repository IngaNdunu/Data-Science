from nltk.chat.util import Chat, reflections

responses = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|hello|greetings|whats up)', ['Hi There']],
    ['(.*)question(.*)', ['What is your question?', 'What do you need help with?']],
    ['(.*)your name?', ['My name is Inga The Chatbot', 'I am Inga The Chatbot, here to help you start your new business']],
    ['(.*)kind of business', ['Be sure your business is one that \n-You are passionate about \n-Is within your reach to fund \n-Has the potential to grow into something big in a reasonable time frame \n-You have some experience in']],
    ['(.*)how are you?', ['Im doing pretty good!', 'Im doing just fine, Thank you for asking!']],
    ['(.*)capital(.*)', [' Your starting capital should be as much as you can reasonably afford, and definitely enough to carry you for at least 6 to 9 months with no income. What you will find is that it always takes you longer to get revenues, and you will undoubtedly incur more expenses than you anticipated.\nBelow are some sources of capital for your new business\n-Personal funds\n-Credit cards\n-Friends and family\n-Angel investors\n-Crowdsourcing sites\n-Bank loans\n-Venture capitalists\n-Equipment loan financin']],
    ['(.*)robot?', ['Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?']],
    ['(.*)insurance', ['-General liability insurance\n-Product liability insurance\n-Professional liability insurance\n-Property insurance\n-Worker’s compensation insurance\n-D & O (directors & officers) insurance\n-Health insurance for employees\n-Business interruption insurance\n-Commercial auto insurance\n-Data breach insurance\n-Key man life insurance']],
    ['(.*)thank you', ['Glad I could help!']],
    ['(.*)quit', ['It was great talking to you!Hope you got what you wanted from this.All the best going forward!!!']],
    ['(.*)mistakes', ['-Not starting with enough capital\n-Thinking that success will come quickly\n-Not carefully budgeting\n-Not focusing on the quality of the product or service\n-Underestimating the importance of sales and marketing\n-Not adapting quickly enough\n-Not understanding the competitive landscape\n-Ignoring legal and contract matters\n-Hiring the wrong employees\n-Mispricing the product or service']],
    ['(.*)challenges', ['Entrepreneurship isn’t easy. Some of the challenges you’ll face include \n-Shortage of capital and cash flow\n-Having a good business plan\n-Coming up with a great product or service\n-Sticking to it\n-Working more than you expected\n-Getting through the frustrations of being constantly rejected by customers\n-Hiring good employees\n-Knowing when to fire bad employees\n-Having to wear so many hats\n-Managing your time\n-Maintaining some kind of work/life balance']],
    ['(.*)',["Okay,I don't know how to answer that.Please check the following link and get a book that will teach you more about how to start a business:\n https://www.amazon.com/Go-Legal-Yourself-Lifecycle-Business/dp/0998946702"]],
    
]

#default message at the start of chat
print("Welcome!!!This is a chatbot created to help answer any questions you might have about starting a business,or redirect you to the appropriate place to get the answers you need.\nAsk away,and type quit(in small letters) to end conversation ")
#Create Chat Bot
chat = Chat(responses, reflections)
#Start conversation
chat.converse()
