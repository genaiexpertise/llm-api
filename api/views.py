from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import  UserSerializer, SummarizeTextSerializer
from .models import SummarizeText

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


llm = ChatGroq(model="llama3-70b-8192")

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class SummarizeTextViewSet(viewsets.ModelViewSet):
    queryset = SummarizeText.objects.all()
    serializer_class = SummarizeTextSerializer
    permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=['post'])
    def summarize(self, request, pk=None):
        if 'text' in request.data:
            text = request.data['text']
            summary = chain.run(text)
            summarize_text = SummarizeText.objects.create(text=text, summary=summary)
            serializer = SummarizeTextSerializer(summarize_text)
            return Response(serializer.data)
        else:
            return Response({'error': 'Text field is required'}, status=400)

     

