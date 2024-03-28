# The main class is Download import it in your project as so

from simple_image_download import simple_image_download as simp 

# Then create a new class instance

response = simp.simple_image_download

# Next you can use response to activate methods 

keyword = ["jonny depp jack", "jack sparrow"] # 키워드를 리스트로 작성

# 작성된 키워드들을 각각 50개씩 다운로드
for kw in keyword:
    response().download(kw, 50)