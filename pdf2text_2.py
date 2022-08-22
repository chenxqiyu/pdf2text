from cnocr import CnOcr

with open("p2t.txt", "w", encoding="utf-8") as f:
    f.write("")
    ocr = CnOcr()
    pages = 340  # 上一步有多少页，这里就是多少
    n = 0

    
    for n in range(pages):
        i = 0
        j = 0
        name = "./images/images_" + str(n + 1) + ".png"
        res = ocr.ocr(name)
        string_list = []
        ocr_result_string=""
        for i in range(len(res)):
            string_list.append(res[i]["text"])
            ocr_result_string = "".join(string_list)
        
        f.write(ocr_result_string)  # 这句话自带文件关闭功能，不需要再写f.close()
        print("Page ", str(n + 1))
    
    print("转换结束。")
