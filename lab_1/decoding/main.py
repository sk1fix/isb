def frequency_analysis():
    key={}
    k=0
    a=[]
    with open('D:/Ycheba/isb/lab_1/decoding/decod.txt','w+',encoding='UTF-8') as wr:
        with open('D:/Ycheba/isb/lab_1/decoding/code1.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                temp = ''
                line = line.strip()
                for i in line:
                    try:
                        key[i]+=1
                    except:
                        key[i]=0
                    k+=1
            for i in key:
                a.append([str(i), key[i]/k])
            sorted_data = sorted(a, key=lambda x: x[1], reverse=True)
            for i in sorted_data:
                wr.write(i[0] + ' : ' + str(i[1]) + '\n')

    



def main():
    frequency_analysis()



if __name__ == "__main__":
    main()