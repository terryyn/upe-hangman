import time
import requests



words= []
url = "http://upe.42069.fun/orCkY"
target = []
sizes = []
guessed = []
dictionary = []

def start_game():
    sizes[:]= []
    target[:] = []
    start = requests.get(url=url)
    start_data = start.json()
    target_string = start_data["state"]
    temp = ""
    for k in range(len(target_string)):
        if target_string[k]=='_':
            temp = temp+target_string[k]
        else:
            if len(temp)!=0:
                target.append(temp)
            temp=""
    for item in target:
        sizes.append(len(item))
    guessed[:] = []

def post_guess(a):
    data = {"guess":a}
    sizes[:] = []
    received = requests.post(url=url,data=data)
    received_data  =received.json()
    target_string = received_data["state"]
    target[:] = []
    temp = ""
    for k in range(len(target_string)):
        if target_string[k].isalpha():
            temp = temp+target_string[k]
        else:
            if len(temp)!=0 and '_' in temp:
                target.append(temp)
            temp=""
    for item in target:
        sizes.append(len(item))
    guessed.append(a)
    return received_data["status"]

def guess_algorithm():
    probability = {}
    for x in range(ord('a'),ord('z')+1):
        probability[chr(x)] = 0
    for char in guessed:
        probability[char] = -10000000
    for word in words:
        if(len(word) not in sizes):
            continue
        location = sizes.index(len(word))
        target_string = target[location]
        valid_flag= True
        for i in range(len(target_string)):
            if target_string[i]!='_' :
                if target_string[i]!=word[i]:
                    valid_flag = False
                    break
        if(valid_flag):
            for i in range(len(word)):
                if word[i].isalpha():
                    probability[word[i].lower()]+=1
    max = 0
    result = ''
    for x in range(ord('a'),ord('z')+1):
        if(probability[chr(x)]>max):
            max = probability[chr(x)]
            result = chr(x)
    if result == '':
        for x in range(ord('a'),ord('z')+1):
            if chr(x) not in guessed:
                return chr(x)
    return result
        

def main():
    with open('words_alpha.txt','r') as ins:
        for line in ins:
            words.append(line.strip())
    for i in range(62):
        start_game()
        ans = guess_algorithm()
        while(post_guess(ans)=='ALIVE'):
            time.sleep(1)
            ans = guess_algorithm()
        print(ans)
        print(post_guess(ans))
    data  = {"guess":"a"}
    end_data = requests.post(url=url,data=data)
    print(end_data.json()["win_rate"])
    reset_data  = {"email":"yeyunong@hotmail.com"}
    requests.post(url="http://upe.42069.fun/orCkY/reset",data=reset_data)
if __name__ == '__main__':
    main()


