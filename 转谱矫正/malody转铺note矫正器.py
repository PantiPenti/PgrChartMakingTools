import json
import os
import PyFunctionFix as py

py.FixDir()

File = open("./input.json")
Json = json.loads(File.read())
while 1:
    os.system("clear")
    JudgeLine = int(input("判定线:"))
    JudgeLineNotes = Json["judgeLineList"][JudgeLine]["notes"]
    StartNote = int(input("开始矫正物量："))
    CurNote = StartNote - 1
    EndNote = int(input("结束矫正物量："))
    CorrectRange = int(input("矫正范围："))
    while CurNote < EndNote:
        Pos = int(JudgeLineNotes[CurNote]["positionX"])
        Pos = int(py.round(Pos / CorrectRange)) * CorrectRange
        JudgeLineNotes[CurNote]["positionX"] = Pos
        CurNote = CurNote + 1
    Json["judgeLineList"][JudgeLine]["notes"] = JudgeLineNotes
    File = open("input.json","w")
    File.write(json.dumps(Json))
