FROM python:3
ARG GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT}
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV OPENAI_API_KEY="YOUR_OPENAPI_KEY"
WORKDIR /app
COPY MentalChatBot2.py /app/
RUN pip install openai==0.28 &&\
    pip install gradio
EXPOSE 7860    
CMD ["python","./MentalChatBot2.py"]