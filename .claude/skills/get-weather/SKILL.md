---
name: get-weather
description: 取得指定城市的天氣資訊。支援台北、紐約、高雄。
argument-hint: <城市名稱>
---

以下是 $ARGUMENTS 的天氣資訊：

!`python "${CLAUDE_SKILL_DIR}/weather.py" "$ARGUMENTS"`

以親切的語氣回覆，並加上一句適合當地天氣的生活建議。
