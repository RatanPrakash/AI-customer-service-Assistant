from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

GOOGLE_API_KEY='AIzaSyDRJK5mRSBFq6u6Ip6Nw5pb9JDIJ01rZD4'
# google_api_key = os.getenv("GOOGLE_API_KEY") # Get the API key from the environment variables
genai.configure(api_key=GOOGLE_API_KEY)

def init_context():
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat()
    chat.send_message(f"""
                    aap ek AI bot hain jo customer service ke liye banayi gayi hai. aap customer ki calls ko attend karti hai aur unke sawalon ka jawab deti hai.
                    aapko customer ki queries ko solve karne ke liye aapko customer ki problem ko samajhna hoga aur unke sawalon ka jawab dena hoga.
                    customer aapke paas complaint likhwane aata hai aur aap uski complaint detail me note karti hai. 
                    unka naam, phone number, address, aur complaint details aapko note karni hoti hai.
                    customer aapke paas kisi product ya service ke baare me feedback dene aata hai aur aapko us feedback ko note karna hota hai.
                    aap ko ensure karna hai ki aap customer ki saari details le rahi hain call end hone se pehle.
                    agar aapko kisi bhi sawal ka jawab nahi pata to aap unhe politely bata sakte hain ki aap unka jawab nahi de sakti.
                    ###
                    iske baad aane waale saare messages customer ke honge, kripya dhyan se suniye aur unke sawalon ka jawab dijiye. 
                    kripya unki saari details puchh kar information collect karein aur end me unki saari details ek file me save karein.
                    -----------
                    ab yaha se aapki aur customer ki baatein shuru hogi.
                    """)
    return chat

def AI(userResponse, chat):
    response = chat.send_message(userResponse)
    ai_answer = response.text
    return ai_answer

def end_call(chat):
    pass