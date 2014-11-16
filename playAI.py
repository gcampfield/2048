import ai

b = ai.SimpleAI(.25)
b.goal = 1024
b.prob = 1
b.loop(printBoard=True)