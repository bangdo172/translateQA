import json
import os
import array
import re

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


for eachFolder in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/testdata"):
    if (eachFolder != ".DS_Store"):
        for eachFile in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/testdata/" + eachFolder):
            if (eachFile != ".DS_Store"):
                with open("testdata/" + eachFolder + "/" + eachFile, "r") as file:
                    database = json.load(file)
                print("____________" + str(eachFolder) + "_____" + str(eachFile))
                data = database['context']
                index = 0
                while index <= int(len(data)):                    
                    if data[index - 1:index] == "  ":
                        data = data.replace(data[index - 1:index]," ")
                    
                    if data[index] == "<":
                        if data[index + 1] == "a":
                            x = [int(s) for s in re.findall(r'-?\d+\.?\d*', data[index:index + 8])][0]
                            y = [int(s) for s in re.findall(r'-?\d+\.?\d*', data[index:index + 8])][1]
                            tag1 = "<a" + str(x) + "_" + str(y) + ">"
                            tag2 = "<a" + str(x) + "_" + str(y) + "/>"
                            print("________" + tag1 + tag2)
                            posTag2 = data.find(tag2, 0, int(len(data)) )
                            theAnswer = data[index:posTag2]
                            theAnswer = deleTagAns(theAnswer)
                            #get the Answer
                            database['qas'][x]['answers'][y]['text'] = theAnswer
                            print(theAnswer)
                            data = data.replace(tag1, "")
                            data = data.replace(tag2, "")
                            data = data[index:].replace("  ", " ")
                            data = data[index:].replace(" .", ".")
                            data = data[index:].replace(" ,", ",")
                            database['qas'][x]['answers'][y]['answer_start'] = index
                            #get index
                            print(database['qas'][x]['answers'][y]['answer_start'])
                            del theAnswer
                            del tag1
                            del tag2
                            del posTag2
                        else:
                            x = [int(s) for s in re.findall(r'-?\d+\.?\d*', data[index:index + 8])][0]
                            y = [int(s) for s in re.findall(r'-?\d+\.?\d*', data[index:index + 8])][1]
                            tag1 = "<b" + str(x) + "_" + str(y) + ">"
                            tag2 = "<b" + str(x) + "_" + str(y) + "/>"
                            print("________" + tag1 + tag2)
                            posTag2 = data.find(tag2, 0, int(len(data)) )
                            theAnswer = data[index:posTag2]
                            theAnswer = deleTagAns(theAnswer)
                            # get the Answer
                            database['qas'][x]['plausible_answers'][y]['text'] = theAnswer
                            print(theAnswer)
                            data = data.replace(tag1, "")
                            data = data.replace(tag2, "")
                            data = data[index:].replace("  ", " ")
                            data = data[index:].replace(" .", ".")
                            data = data[index:].replace(" ,", ",")
                            # get index
                            database['qas'][x]['plausible_answers'][y]['answer_start'] = index
                            print(database['qas'][x]['plausible_answers'][y]['answer_start'])
                            del theAnswer
                            del tag1
                            del tag2
                            del posTag2
                        index = index - 1

                    index = index + 1
                    if(index >= len(data)):
                        break
                database['context'] = data
                with open("testdata/" + eachFolder + "/" + eachFile, "w") as file:
                    json.dump(database,file)
                print(data)
                print("--------------------")
                print("")
                del index
                del data
                del database
            #break
        #break