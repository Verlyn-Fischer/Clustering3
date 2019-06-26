import numpy as np
import mysql.connector as conn
import pickle


cnx = []

def establishConnection():

    global cnx
    cnx = conn.connect(user='testUser', password='disc0tech',
                              host='127.0.0.1',
                              database='Clustering')
def closeConnection():

    cnx.close()

def writeToSentences():

    cursor = cnx.cursor()
    add_sentence = ("INSERT INTO sentences (sentenceText, embedding) VALUES (%s, %s)")
    testEmbedding = np.arange(0, 300, dtype=np.float)

    pickleEmbedding = pickle.dumps(testEmbedding)
    stringEmbedding = np.array2string(testEmbedding, formatter={'float_kind': lambda x: "%.2f" % x})
    stringEmbedding2 = np.array_str(testEmbedding)
    # sentence_data = ('This is a test sentence.',testEmbedding.tobytes(),)
    sentence_data2 = ('This is a test sentence.',stringEmbedding,)
    sentence_data3 = ('This is a test sentence.', testEmbedding,)
    sentence_data4 = ('This is a test sentence.', pickleEmbedding,)
    sentence_data5 = ('This is a test sentence.', stringEmbedding2,)

    cursor.execute(add_sentence,sentence_data2)

    cnx.commit()
    cursor.close()


def readFromSentences():

    Error = ""
    query = ("SELECT embedding FROM sentences")
    cursor = cnx.cursor()

    try:

        cursor.execute(query)
        # myEmbedding = cursor.fetchone()[0]


        for outputEmbedding in cursor:
            for eachString in outputEmbedding:
                # print(eachString)
                # recallEmbedding = np.fromstring(eachString)
                unicode_line = eachString.translate({ord(c): None for c in '\n[]'})
                recallEmbedding = np.fromstring(unicode_line, dtype=float, sep=' ')
                # recallEmbedding = np.fromstring(unicode_line)
                print(recallEmbedding)
                print(recallEmbedding[0])
                print("Length: ", str(recallEmbedding.size))

        # rows = cursor.fetchall()

        # ## Get the results
        # for each in rows:
        #     ## The result is also in a tuple
        #     for pickledStoredList in each:
        #         ## Unpickle the stored string
        #         unpickledList = pickle.loads(pickledStoredList)
        #         print(unpickledList)
        # print(myEmbedding)
        # recallEmbedding = np.fromstring(myEmbedding)
        # recallEmbedding = pickle.loads(myEmbedding)
        # print(len(recallEmbedding))


    except Error as e:
        print(e)

    finally:
        cursor.close()

    # for (embedding) in cursor:
    #     # print(sentenceText)
    #     recallEmbedding = np.fromstring(embedding)
    #     print(len(recallEmbedding))




# MAIN

establishConnection()
# writeToSentences()
readFromSentences()
closeConnection()
