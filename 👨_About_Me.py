import streamlit as st

st.set_page_config(page_title="👨 About Me", page_icon=":man:", layout="wide")

st.title("Alexander Radchenko")
st.markdown("### First Year Robotics Masters Student at the GRASP Lab, University of Pennsylvania")

description = """
## Welcome to my personal website!

Welcome to my personal website! I’m Alexander Radchenko, a passionate advocate for automation and efficiency. 
I believe in the power of disassembling complex systems to uncover their core functionalities and reassembling them in a way that enhances performance and productivity. 
My journey in robotics and machine learning is driven by this philosophy, as I strive to create intelligent solutions that simplify life and work.

As a current Masters student in Robotics at the University of Pennsylvania, 
I specialize in Computer Vision and Reinforcement Learning, applying these cutting-edge technologies to the field of robotics. 
My academic excellence is reflected in my 3.9 GPA, and my hands-on experience includes a dissertation that achieved state-of-the-art results in language reasoning with visual cues.

My technical skills are diverse, encompassing programming languages like Python, Java, C, and C++, 
as well as expertise in data science and machine learning tools such as PyTorch, Pandas, and HuggingFace. 
I’ve also demonstrated my abilities in game and web development, with projects like the Graviton Android game and Unreal Engine plugins that have garnered significant attention.

I invite you to explore my site, learn more about my projects, and see how my skills and experiences can contribute to innovative and efficient technological advancements.

### Contact me!
- +1 (929) 641 3080
- [alex.and.radchenko@gmail.com](mailto:alex.and.radchenko@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/xaler/)
"""

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(description)

with col2:
    st.image("./profile_pic.jpg", caption="Alexander Radchenko", use_column_width=True)


