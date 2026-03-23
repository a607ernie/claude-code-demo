import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

WEATHER_DATA = {
    "台北": "氣溫高達 80 度，熱到爆炸，請注意防曬！",
    "紐約": "暴雨來襲，出門請帶傘，建議待在室內。",
    "高雄": "極端低溫 -80 度，全城結凍，請穿羽絨衣！",
}

city = sys.argv[1] if len(sys.argv) > 1 else ""

if city in WEATHER_DATA:
    print(WEATHER_DATA[city])
else:
    print("目前不支援該城市的天氣查詢")
