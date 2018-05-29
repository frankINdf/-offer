chineseToNumberDict={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}
def genrateWordsList(strings,zeroIn=False):
###将输入的汉字数字转换为单个字列表，并取出零
###输入：汉字数字,是否包含零
###输出：不含零的单个汉字列表
	wordList=[]
	for word in strings:
		if word!="零" or zeroIn:
		    wordList.append(word)
	return wordList
def changeToInt(strings):
###汉字数字列表转换为数字
###输入：数字列表
###输出：数字
	if len(strings)==0:
		return 0
	words = genrateWordsList(strings) 
	number=0
	for i in range(len(words)):
		if words[i]=='千':
			index = words[i-1]
			number += chineseToNumberDict[index]*1000
		if words[i]=='百':
		    index = words[i-1]
		    number += chineseToNumberDict[index]*100
		if words[i]=='十':
		    index = words[i-1]
		    number += chineseToNumberDict[index]*10
	if words[len(words)-1]!='千' and words[len(words)-1]!='百' and words[len(words)-1]!='十':
		index = words[len(words)-1]
		number+=chineseToNumberDict[index]
	return number
def inputCheck(strings):
###汉字拼写检查
###还有
    checkList = ["百","千","万","亿"]
    if len(strings)==0:
        print("字符长为0")
        return False
    words = genrateWordsList(strings,True)
    if words[0]=="零" or words[len(words)-1]=="零":
        print("拼写错误,不能以零为开头或结尾")
        return False
    for i in range(len(words)):
        if words[i] == "零" and words[i-1] in checkList and words[i+1] in chineseToNumberDict.keys():
        	if words[i-1]-words[i+1]<1:
        	    return True
        return False

    





###思路：生成{"亿":[],"万":[],"个":[]}形式的字典
###再遍历字典，将对应数位上的数字乘以相应的系数
def splitChineseNumber(strings):
###生成{"亿":[],"万":[],"个":[]}形式的字典
###输入不含零的汉字列表
    inputCheck(strings)
    numberdict={"亿":[],"万":[],"个":[]}
    tempList = []

    words = genrateWordsList(strings)

    for i in range(len(words)):
        if words[i]=="亿":
            numberdict["亿"]=tempList
            tempList = []
        elif words[i]=="万":
            numberdict["万"]=tempList
            tempList = []
        else:
            tempList.append(words[i])
    numberdict["个"]=tempList
    return numberdict
def chineseToNumber(strings):
####将对应数位上的数字乘以相应的系数
####输入汉字数字
####输出数字
    outValue=0
    inputVaild = True
    inputVaild=inputCheck(strings)
    if inputVaild == False:
        return False
    numberdict = splitChineseNumber(strings)
    for key in numberdict:
        value=changeToInt(numberdict[key])
        if key =="亿":
            outValue += 100000000*value
        if key =="万":
            outValue += 10000*value
        if key =="个":
            outValue += value
    return  outValue
a=chineseToNumber("五十八")
b=chineseToNumber("一百二十三万四千五百六十七")
c=chineseToNumber("三千二百一十万零二百一十五")
d=chineseToNumber("一亿零九十万零七十六")
f=chineseToNumber("")
print("五十八",a)
print("一百二十三万四千五百六十七",b)
print("三千二百一十万零二百一十五",c)
print("一亿零九十万零七十六",d)




