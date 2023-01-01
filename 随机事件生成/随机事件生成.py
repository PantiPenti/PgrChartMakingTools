import json
import os
import random
import time
import PgrStandard as pgr
import PyFunctionFix as py

py.FixDir()

File = open("./input.json")
Json = json.loads(File.read())
while 1:
    os.system("clear")
    JudgeLine = int(input("输入对象判定线："))
    GenEventType = pgr.LineEventType[int(input("随机事件类型：")) - 1]
    ObjJudgeLine = Json["judgeLineList"][JudgeLine]["eventLayers"][0][GenEventType]
    GenStartTime = pgr.time(input('事件生成开始时间(用":"间隔)：'))
    GenEndTime =  pgr.time(input("事件生成结束时间："))
    GenEventValRange = json.loads(input("请输入事件生成事项（Json数组）："))
    GenStartEvent = 0
    while GenStartEvent < len(ObjJudgeLine):
        if pgr.TimeJudge(ObjJudgeLine[GenStartEvent]["startTime"], GenStartTime) >= 2 and pgr.TimeJudge(ObjJudgeLine[GenStartEvent]["endTime"], GenEndTime) <= 2:    break
        GenStartEvent = GenStartEvent + 1
    CurEvent = GenStartEvent
    if CurEvent >= len(ObjJudgeLine):
        print("没有符合此时间段的事件！")
        time.sleep(5)
        continue
    while CurEvent < len(ObjJudgeLine) and pgr.TimeJudge(ObjJudgeLine[CurEvent]["endTime"], GenEndTime) <= 2:
        EventValGroup = GenEventValRange[random.randint(0, len(GenEventValRange) - 1)]
        ObjJudgeLine[CurEvent]["start"] = random.randint(EventValGroup["StartValRange"][0],EventValGroup["StartValRange"][1])
        ObjJudgeLine[CurEvent]["end"] = random.randint(EventValGroup["EndValRange"][0],EventValGroup["EndValRange"][1])
        CurEvent = CurEvent + 1
    Json["judgeLineList"][JudgeLine]["eventLayers"][0][GenEventType] = ObjJudgeLine
    File = open("./input.json","w")
    File.write(json.dumps(Json))
    print("成功！")
    time.sleep(3)

# 样例范围输入：
#[{"StartValRange":[200,500], "EndValRange":[-50,250]}, {"StartValRange":[-500,200], "EndValRange":[-250,50]}]
#[{"StartValRange":[80,90], "EndValRange":[70,80]}, {"StartValRange":[90,100], "EndValRange":[100,110]}]
#[{"StartValRange":[70,120], "EndValRange":[0,0]}]
#3、5～7:37.5～39 2:36.75 4:36