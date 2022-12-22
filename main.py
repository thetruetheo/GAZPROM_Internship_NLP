import os
from docx import Document

def text_extractor(path):
    doc_obj=open(path,"rb")
    doc_reader=Document(doc_obj)
    data=""
    for p in doc_reader.paragraphs:
        data +=p.text+"\n"
    return data

directory="test_documents"

document_text=""

for filename in os.listdir(directory):
    if filename.endswith(".docx") or filename.endswith(".doc"):
        print("\nНачалась обработка документа: \n")
        print(os.path.join(directory, filename))
        path_to_docx = os.path.join(directory, filename)
        document_text=text_extractor(path_to_docx)
        #print(document_text)

        with open(str(path_to_docx)+'.txt', 'w', encoding="utf-8") as writer:
            for value in document_text:

                writer.write(value)
        document_text=""
        print("\nОбработка документа завершена.\n")







