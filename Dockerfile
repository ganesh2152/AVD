FROM python
RUN pip install streamlit
RUN mkdir /myapp
WORKDIR /myapp
COPY app.py .
EXPOSE 8501
CMD ["streamlit","run","app.py"]