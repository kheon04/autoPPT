from pptx import Presentation
import shutil
import copy

# 단순, 파일을 복사하기
source = "Theme.pptx"
destination_folder = r"lyrics\\"
destination = destination_folder + r"test1.pptx"
shutil.copyfile(source, destination)

Theme_prs = Presentation(destination)