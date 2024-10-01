from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

llm = ChatGroq(model="llama3-70b-8192")

router = APIRouter(prefix="/text_summarization", tags=["text_summarization"])

summarize_template_string = """
Provide a summary of the following text:
{text}

"""

summarize_promt = PromptTemplate(
    template=summarize_template_string,
    input_variables=['text'],
)

chain = LLMChain(
    llm=llm,
    prompt=summarize_promt
)

@router.post("/summarize")
async def summarize_text(text: str):
    summary = chain.run(text)
    return {"summary": summary}
    