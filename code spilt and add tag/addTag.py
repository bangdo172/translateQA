import json
import array
import os

def insert(source_str, add_str ,pos):
    return source_str[:pos] + add_str + source_str[pos:]

def insertATag (pos, length, tag1, tag2):
    isTag[pos] = isTag[pos] + "<a" + tag1 +"_"+ tag2 + ">"
    isTag[pos + length] = "<a" + tag1 + "_" + tag2 + "/>" + isTag[pos + length]

def insertBTag (pos, length, tag1, tag2):
    isTag[pos] = isTag[pos] + "<b" + tag1 +"_"+ tag2 + ">"
    isTag[pos + length] = "<b" + tag1 + "_" + tag2 + "/>" + isTag[pos + length]


for eachFolder in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/train"):
    if (eachFolder != ".DS_Store"):
        for eachFile in os.listdir("/Users/bangdo/Documents/theProject/MachinelearningCode/ReadingWikiToAnswerOpenQuestion/translateAPI/train/" + eachFolder):
            if (eachFile != ".DS_Store"):
                with open("train/" + eachFolder + "/" + eachFile, "r") as file:
                    database = json.load(file)
                question_count = 0
                lengthContext = int(len(database['context']))

                #init isTag
                isTag = []
                for i in range(lengthContext + 1):
                    isTag.append('')

                #implement with each question of a paragraph
                for eachQuestion in database['qas']:
                    answer_count = 0
                    answer_start = 0
                    if eachQuestion['is_impossible'] == False:
                        for eachAnswer in eachQuestion['answers']:
                            insertATag(eachAnswer['answer_start'], int(len(eachAnswer['text'])), str(question_count), str(answer_count))
                            answer_count = answer_count + 1    
                    else:
                        for eachAnswer in eachQuestion['plausible_answers']:
                            insertBTag(eachAnswer['answer_start'], int(len(eachAnswer['text'])), str(question_count), str(answer_count))
                            answer_count = answer_count + 1
                    question_count = question_count + 1
                    del answer_count
                    del answer_start
                # insert tag to paragraph
                for l in range(lengthContext - 1, -1, -1):
                    database['context'] = insert(database['context'], isTag[l], l)
                del isTag[:]
                del question_count
                del lengthContext

                # file
                with open("train/" + eachFolder + "/" + eachFile, "w") as file:
                    json.dump(database,file)

