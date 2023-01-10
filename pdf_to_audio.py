import PyPDF2,pyttsx3

start_page = 140

my_pdf = PyPDF2.PdfReader(open('The-Invisible-Man.pdf','rb'))
num_pages= len(my_pdf.pages)
engine = pyttsx3.init()

def set_engine_properties(engine):
    engine.setProperty('rate', 130)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1


def change_voice(engine, name):
    voices = engine.getProperty('voices')
    for voice in voices:
        if name == voice.name:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language for name '{name}' not found")

    
set_engine_properties(engine)
change_voice(engine, "Microsoft Zira Desktop - English (United States)")


for page_num in range(start_page,num_pages):
    text = my_pdf.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n','')
    print(clean_text)

engine.save_to_file(clean_text,'invisible_man.mp3')
engine.runAndWait()



