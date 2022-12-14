import os
from docx import Document




def docx_to_dict(name_of_file):
    docx_dict={}
    document=Document(name_of_file)
    indx = 0
    for para in document.paragraphs:
        indx += 1
        if (len(para.text) > 0):
            #print("\n paragraph", indx, "is")
            #print(para.text)
            docx_dict[indx] = para.text
    return docx_dict

directory="test_documents"
docx_content={}

for filename in os.listdir(directory):
    if filename.endswith(".docx") or filename.endswith(".doc"):
        #print('file name is',filename)
        print(os.path.join(directory, filename))
        path_to_docx = os.path.join(directory, filename)
        docx_content[path_to_docx] = docx_to_dict(path_to_docx)

        writeable_content = list(docx_content.items())
        with open(str(path_to_docx)+'.txt', 'w', encoding="utf-8") as writer:
            for value in writeable_content:
                writer.write(str(value))
        writeable_content = []

        docx_content = {}
        print("\nОбработка документа окончена\n")







