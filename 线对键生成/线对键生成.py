import json
import os
import time
import PgrStandard as pgr
import PyFunctionFix as py

py.FixDir()

File = open("./input.json")
Json = json.loads(File.read())
while 1:
    os.system("clear")
    PerformLine = int(input("输入表演线编号:"))
    NoteLine = int(input("请输入键线编号:"))
    ObjPerformLine = Json["judgeLineList"][PerformLine]["eventLayers"][0]["moveXEvents"]
    ObjNoteLine = Json["judgeLineList"][NoteLine]["notes"]
    GenStartTime = pgr.time(input("请输入生成开始时间（用:分隔）:"))
    GenEndTime = pgr.time(input("请输入结束生成时间:"))
    GenStartEvent = 0
    while GenStartEvent < len(ObjPerformLine):
        if pgr.TimeJudge(ObjPerformLine[GenStartEvent]["startTime"], GenStartTime) >= 2 and pgr.TimeJudge(ObjPerformLine[GenStartEvent]["endTime"], GenEndTime) <= 2:    break
        GenStartEvent = GenStartEvent + 1
    CurEvent = GenStartEvent
    if CurEvent >= len(ObjPerformLine):
        print("没有符合此时间段的事件！")
        time.sleep(3)
        continue
    GenStartNote = 0
    while GenStartNote < len(ObjNoteLine):
        if pgr.TimeJudge(ObjNoteLine[GenStartNote]["startTime"], GenStartTime) >= 2 and pgr.TimeJudge(ObjNoteLine[GenStartNote]["endTime"], GenEndTime) <= 2:    break
        GenStartNote = GenStartNote + 1
    CurNote = GenStartNote
    if CurNote >= len(ObjNoteLine):
        print("没有符合此时间段的Note！")
        time.sleep(3)
        continue
    LastNoteTime = [0,0,0]
    while pgr.TimeJudge(ObjNoteLine[CurNote]["endTime"], GenEndTime) <=2:
        if pgr.TimeJudge(ObjNoteLine[CurNote]["startTime"], LastNoteTime) == 2:
            CurNote = CurNote + 1
            continue
        LastNoteTime = ObjNoteLine[CurNote]["startTime"]
        ObjPerformLine[CurEvent]["start"] = ObjNoteLine[CurNote]["positionX"]
        ObjPerformLine[CurEvent]["end"] = ObjNoteLine[CurNote]["positionX"]
        CurEvent = CurEvent + 1
        CurNote = CurNote + 1
    Json["judgeLineList"][PerformLine]["eventLayers"][0]["moveXEvents"] = ObjPerformLine
    File = open("./input.json", "w")
    File.write(json.dumps(Json))
    print("成功！")
    time.sleep(3)