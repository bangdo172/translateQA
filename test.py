import json
import os
import array

def deleTagAns(answer):
    result = ""
    index = 0
    while index < int(len(answer)):
        if answer[index] == "<":
            index = answer.find(">", index, int(len(answer)))
        else:
            result = result + answer[index]
        index = index + 1
    result = result.strip()
    check = 0
    while check != -1:
        result = result.replace("  ", " ")
        check = result.find("  ", 0, int(len(result)))
    return result

"""
string = " <a44_5>  do van  <a_6>  bang <a4_6/>  <a4_5/>  "
print(string)
print(deleTagAns(string
"""

for eachFolder in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/testdata"):
    if (eachFolder != ".DS_Store"):
        for eachFile in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/testdata/" + eachFolder):
            if (eachFile != ".DS_Store"):
                with open("testdata/" + eachFolder + "/" + eachFile, "r") as file:
                    database = json.load(file)
                lengthContext = int(len(database['context']))
                question_count = 0
                for eachQuestion in database['qas']:
                    answer_count = 0
                    if eachQuestion['is_impossible'] == False:
                        for eachAnswer in eachQuestion['answers']:
                            tag1 = "<a" + str(question_count) + "_" + str(answer_count) + ">"
                            tag2 = "<a" + str(question_count) + "_" + str(answer_count) + "/>"
                            posTag1 = database['context'].find(tag1, 0, lengthContext + 1)
                            posTag2 = database['context'].find(tag2, 0, lengthContext + 1)
                            theAnswer = database['context'][posTag1:posTag2]
                            print(theAnswer)
                            print(deleTagAns(theAnswer))
                            #print(eachAnswer['text']) 
                            #print(str(question_count) + "___" + str(answer_count))
                            answer_count = answer_count + 1
                    question_count = question_count + 1