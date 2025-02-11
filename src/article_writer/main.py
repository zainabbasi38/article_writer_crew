from crewai.flow.flow import start, listen, Flow
from pydantic import BaseModel
from article_writer.crews.poem_crew.poem_crew import ArticleCrew
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


class ArticleState(BaseModel):
    topic : str = ""
    article : str = ""

class ArticleFlow(Flow[ArticleState]):

    @start()
    def topic(self):
        print("Generating article topic")
        self.state.topic = input("Enter topic: ")


    @listen(topic)
    def generate_article(self):
        print("Generating article")
        result = ArticleCrew().crew().kickoff(inputs={"topic": self.state.topic})

        print("Article generated", result.raw)
        self.state.article = result.raw

    @listen(generate_article)
    def save_article(self):
        print("Saving article")
        with open("article.md", "w") as f:
            f.write(self.state.article)

def kickoff():
    flow = ArticleFlow()
    flow.kickoff()

def plot():
    flow = ArticleFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()