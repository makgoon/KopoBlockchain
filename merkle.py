def calculateHash(index, previousHash, timestamp, data, proof):
    value = str(index) + str(previousHash) + str(timestamp) + str(data) + str(proof)
    sha = hashlib.sha256(value.encode('utf-8'))
    return str(sha.hexdigest())


def calculateHashtwo(index, previousHash):
    value = str(index) + str(previousHash)
    sha = hashlib.sha256(value.encode('utf-8'))
    return str(sha.hexdigest())


def calculateHashone(index):
    value = str(index)
    sha = hashlib.sha256(value.encode('utf-8'))
    return str(sha.hexdigest())


strTxData = []

temptHashList = []

# 거래장부 전체, 문자열 변환

importedTx = ["b", "c", "d", "e", "g"]

# 전체 거래장부(정규표현식)
checker = True
if len(importedTx) > 0:
    strTxData = importedTx

    while (checker == True):

        if (len(strTxData//16) >= 1):
            tonerList = []
            while (innerChecker == True):

                if (len(strTxData) > 16):
                    numToner = len(strTxData // 16)
                    restToner = len(strTxData % 16)
                    if(restToner != 0):
                        firstToner = random.sample(strTxData, numtoner)
                        firstTonerAdd = random.sample(strTxData, 1)
                        filter(lambda a: a != firstToner, strTxData)
                        filter(lambda a: a != firstTonerAdd, strTxData)
                        if(restToner > 0):
                            restToner = restToner - 1
                        secondToner = random.sample(strTxData, numToner)
                        filter(lambda a: a != secondToner, strTxData)
                            secondTonerAdd = random.sample(strTxData, 1)






            tempt = calculateHashtwo(a, b)

            temptHashList.append(tempt)

            strTxData.remove(a)
            strTxData.remove(b)


        elif (len(strTxData) == 1):

            temptHashList.append(calculateHashone(strTxData[0]))

            del strTxData[0]

            strTxData = temptHashList
            if (len(temptHashList) == 1):
                checker = False
                print(strTxData)

            elif (len(temptHashList) == 0):
                print("abnormal calculate")
                break
