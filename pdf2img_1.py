import sys, fitz
import os
import datetime


def pyMuPDF_fitz(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.page_count):
        page = pdfDoc[pg]
        rotate = int(0)
        # 此处若是不做设置，默认图片大小为：792X612, dpi=72 我扫描的文件是200dpi
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        zoom_x = 1.3  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.3
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.save(imagePath + "/" + "images_%s.png" % (pg + 1))  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print("pdf2img时间=", (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":
    pdfPath = r"F:\efibak\zhongyi_sun.pdf"
    imagePath = "./images"
    pyMuPDF_fitz(pdfPath, imagePath)
