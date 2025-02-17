import streamlit as st
from article_writer.crews.poem_crew.poem_crew import ArticleCrew
from dotenv import load_dotenv

load_dotenv()


def app():
    st.title("Article Generator")
    st.write("Enter a topic to generate an article using CrewAI.")
    
    topic = st.text_input("Article Topic", "")
    
    if st.button("Generate Article"):
        if not topic:
            st.error("Please provide a topic!")
        else:
            with st.spinner("Generating article..."):
                result = ArticleCrew().crew().kickoff(inputs={"topic": topic})
                article = result.raw
                st.session_state["article"] = article
            st.success("Article generated successfully!")
    
    if "article" in st.session_state:
        st.subheader("Generated Article")
        st.write(st.session_state["article"])
        
        st.download_button(
            label="Download Article",
            data=st.session_state["article"],
            file_name="article.md",
            mime="text/markdown"
        )


if __name__ == "__main__":
    app()