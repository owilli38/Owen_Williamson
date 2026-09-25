from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Owen Williamson",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --ink: #111111;
        --muted: #5a7164;
        --paper: #f7f5f0;
        --line: #d7ddd5;
        --accent: #1f5a43;
        --accent-soft: #e1ece5;
        --navy: #163d2e;
    }

    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }
    [data-testid='stHeader'] { background: transparent; }
    [data-testid='stSidebar'] {
        background: var(--navy);
        border-right: 0;
    }
    [data-testid='stSidebar'] * { color: #f7f5f0; }
    [data-testid='stSidebar'] .stButton button {
        background: transparent;
        border: 1px solid rgba(247, 245, 240, .35);
        color: #f7f5f0;
        border-radius: 3px;
    }
    [data-testid='stSidebar'] .stButton button:hover {
        border-color: #f7f5f0;
        color: #f7f5f0;
    }
    [data-testid='stSidebar'] .stDownloadButton button {
        background: transparent;
        border: 1px solid rgba(247, 245, 240, .35);
        color: #f7f5f0;
        border-radius: 3px;
        width: 100%;
    }
    [data-testid='stSidebar'] .stDownloadButton button:hover {
        border-color: #f7f5f0;
        color: #f7f5f0;
    }
    .block-container { max-width: 1160px; padding: 4rem 4rem 5rem; }
    h1, h2, h3, h4 { font-family: 'Space Grotesk', sans-serif; color: var(--ink); }
    h1 { font-size: clamp(3rem, 7vw, 6.6rem) !important; line-height: .92 !important; letter-spacing: -0.06em; margin-bottom: 1.2rem !important; }
    h2 { font-size: 1.45rem !important; letter-spacing: -.03em; margin-top: 3rem !important; }
    h3 { font-size: 1.12rem !important; margin-bottom: .2rem !important; }
    p { color: var(--muted); line-height: 1.65; }
    .eyebrow { color: var(--accent); font-size: .75rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-bottom: 1rem; }
    .hero-copy { font-size: 1.12rem; max-width: 640px; }
    .hero-rule { border-top: 1px solid var(--line); margin: 2.5rem 0 2rem; }
    .section-label { color: var(--accent); font-family: 'Space Grotesk', sans-serif; font-size: .8rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
    .role { color: var(--muted); font-size: .9rem; margin: 0; }
    .date { color: var(--accent); font-size: .8rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
    .resume-item { border-top: 1px solid var(--line); padding: 1.25rem 0 1.5rem; }
    .resume-item:first-child { margin-top: .75rem; }
    .skill { background: #fffdf8; border: 1px solid var(--line); display: inline-block; font-size: .85rem; margin: .25rem .35rem .25rem 0; padding: .5rem .7rem; }
    .project-card { background: #fffdf8; border-top: 3px solid var(--accent); min-height: 250px; padding: 1.25rem 1.2rem 1.4rem; }
    .project-card h3 { margin-top: .65rem !important; }
    .project-label, .project-tools { color: var(--accent); font-size: .72rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
    .project-tools { border-top: 1px solid var(--line); color: var(--muted); line-height: 1.5; margin-top: 1.2rem; padding-top: .85rem; }
    .project-links { display: flex; gap: 1rem; margin-top: 1rem; }
    .project-links a { color: var(--accent); font-size: .8rem; font-weight: 700; text-decoration: none; }
    .project-links a:hover { text-decoration: underline; }
    .note { background: var(--accent-soft); border-left: 3px solid var(--accent); padding: 1rem 1.2rem; }
    .note p { color: var(--ink); margin: 0; }
    .footer { border-top: 1px solid var(--line); color: var(--muted); font-size: .8rem; margin-top: 4rem; padding-top: 1rem; }
    @media (max-width: 700px) {
        .block-container { padding: 2.5rem 1.4rem 3rem; }
        h1 { font-size: 3.8rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.markdown("## Owen")
    st.markdown("**Owen Williamson**")
    st.caption("Resume")
    st.markdown("---")
    st.markdown("**Navigate**")
    st.markdown("[About](#about)  \n[Skills](#skills)  \n[Education](#education)  \n[Experience](#experience)  \n[Projects](#projects)  \n[Publications](#publications)")
    st.markdown("---")
    st.markdown("**Let's connect**")
    st.markdown("owenwilliamson997@gmail.com  \n[LinkedIn](https://www.linkedin.com/in/owen-k-williamson)  \n[GitHub](https://github.com/owilli38)", unsafe_allow_html=True)
    resume_path = Path(__file__).parent / "Williamson, Owen Resume.pdf"
    if resume_path.exists():
        st.download_button(
            "Download resume",
            data=resume_path.read_bytes(),
            file_name="Owen_Williamson_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.error("Resume PDF is unavailable.")


st.markdown('<div class="eyebrow">Resume</div>', unsafe_allow_html=True)
st.title("Owen Williamson")
st.markdown(
    """
    <p class="hero-copy">M.S. in Data Science & Business Analytics (GPA: 3.90) with experience building machine learning models,
    NLP pipelines, and analytics dashboards. Skilled in Python, R, SQL, and Power BI with experience applying statistical and ML methods
    to healthcare and business problems.</p>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="hero-rule"></div>', unsafe_allow_html=True)

about, focus = st.columns([1.6, 1], gap="large")
with about:
    st.markdown('<div id="about" class="section-label">About</div>', unsafe_allow_html=True)
    st.markdown(
        "I am a recent graduate from the University of North Carolina at Charlotte with a Master of Science in Data Science & Business Analytics. Before that, I graduated from Davidson College magna cum laude with a bachelor’s degree in political science. I have experience turning complex data into analysis-ready data and translating and communicating my findings to general audiences. I am passionate about public health and improving health outcomes. I have experience in both supervised and unsupervised machine learning, along with text mining and natural language processing. Beyond my professional experience, I love running and training for marathons. I have run 3 so far (Charlotte 2 times and Columbus, Ohio, once). My PB is 2:43:53."
    )
with focus:
    st.markdown('<div class="section-label">Focus areas</div>', unsafe_allow_html=True)
    st.markdown("**Data analysis**  \n**Statistics**  \n**Research & communication**")


st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("## Skills & interests")
skills = ["R", "Python", "SQL", "Power BI", "Excel", "Github", "Regression", "Classification Models", "XGBoost/Random Forest/Logistic Regression", "RAG", "AI Prompt Engineering", "Data storytelling", "Data analysis", "Research", "Machine Learning", "Text Analysis/NLP", "Communication","Statistics"]
st.markdown("".join(f'<span class="skill">{skill}</span>' for skill in skills), unsafe_allow_html=True)


st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown("## Education")
st.markdown(
    """
    <div class="resume-item">
        <div class="date">Graduate study</div>
        <h3>Master of Science in Data Science & Business Analytics</h3>
        <p class="role">GPA: 3.90 · University of North Carolina at Charlotte, May 2026</p>
    </div>
    <div class="resume-item">
        <div class="date">Undergraduate study</div>
        <h3>Bachelor of Arts in Political Science</h3>
        <p class="role">GPA: 3.84, Magna Cum Laude · Davidson College, January 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("## Experience")
st.markdown(
    """
        <div class="resume-item">
            <div class="date">Wake Forest University School of Medicine</div>
            <h3>Biostatistics Intern</h3>
            <p class="role">Winston-Salem, NC · June 2026 - Present</p>
            <p class="description">Automated matching pipeline in R using the rentrez package to programmatically query PubMed for downstream publications 
for 1,650 institutional service forms.</p>
            <p class="description">Applied text analysis and natural language processing techniques to extract insights from unstructured data.</p>
            <p class="description">Predicted publication success using a penalized logistic regression model with cross-validation.</p>
            <p class="description">Analyzed the causal effect of institutional support on bibliometric measures using mixed-effect and general linear mixed models 
with fixed and random effect variables.</p>
            <p class="description">Conducted systematic clinical chart reviews of Electronic Health Record (EHR) data to obtain high-fidelity ground truth variables 
and identify data quality gaps within structured clinical fields</p>
        </div>
        <div class="resume-item">
            <div class="date">Fleet Feet</div>
            <h3>Marketing Coordinator</h3>
            <p class="role">Huntersville, NC · March 2024 - May 2026</p>
            <p class="description">Coordinated marketing campaigns and events to drive brand awareness and customer engagement.</p>
            <p class="description">Segmented a CRM database of 30,000+ contacts for targeted campaigns, increasing participation by 50%+.</p>  
            <p class="description">Streamlined operations by building an automated Excel KPI dashboard, reducing manual reporting constraints by 2 hours/week.</p>
            <p class="description">Conducted SEO analysis to optimize web presence, successfully driving measurable increases in digital and foot traffic.</p>
            <p class="description">Monitored social media engagement metrics through iterative testing, refining content strategy to boost engagement by 75%</p>
            <h3>Outfitter</h3>
            <p class="role">Huntersville, NC · August 2023 - May 2026</p>
            <p class="description">Provided excellent customer service by actively educating customers about specialized products in a one-on-one fitting experience.</p>
            <p class="description">Served as team lead, managing a team of outfitters, greeting customers, and fulfilling leadership roles in fast-paced store environments.</p>
        <div class="resume-item">
            <div class="date">Center for Civic Engagement</div>
            <h3>Community Research Fellow</h3>
            <p class="role">Davidson, NC · March 2024 - May 2026</p>
            <p class="description">Created a dashboard using RShiny for partner organization, CREED, displaying representation for students of color compared to school board members across North Carolina’s 115 school districts and designed case studies to highlight exemplary stories</p>
            <p class="description">Compiled and cleaned data using R and wrote code to automate the matching process for school board members to their voter registration from the state-wide file, successfully matching 90% of school board members.</p>
            <p class="description">Utilized an API to streamline data collection and publicly available data on district- and school-level achievement.</p>
            <p class="description">Collaborated with CREED and stakeholders, presenting weekly updates and effectively communicated to meet deliverables.</p>
        </div>
        <div class="resume-item">
             <div class="date">Ron Osborne for NC House</div>
            <h3>Assistant Treasurer</h3>
            <p class="role">Graham, NC · March 2022 - July 2023</p>
           <p class="description">Maintained detailed spreadsheets, confirming balance to bank statements to ensure accuracy and communicating effectively with others to capture financial data.</p>
           <p class="description">Managed and accounted over $35,000 in both contributions and expenditures.</p>
        """,
        unsafe_allow_html=True,
    )


st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("## Projects")
projects = [
    (
        "01 / Publication matching",
        "PubMed Matching Pipeline",
        "Built an automated R pipeline with rentrez to query PubMed and match publications to 1,650 institutional service forms.",
        "R · rentrez · TF-IDF · Logistic regression",
        None,
        None,
        None,
    ),
    (
        "02 / Masters Capstone Project",
        "Emerging Fraud Trends Dashboard",
        "Developed an automated pipeline to ingest news articles and other relevant text data daily and analyze fraud trends using clustering, text embeddings, and fraud risk scores.",
        "Python · Topic modeling · RAG (Retrieval-Augmented Generation) · Fraud analysis",
        "https://github.com/owilli38/DSBA6390-Fraud-Detection-Emerging-Fraud-Signals-Dashbaord-",
        None,
        None,
    ),
    (
        "03 / Measles Outbreak Prediction",
        "Measles Outbreak Prediction",
        "Developed a predictive model to forecast measles outbreaks using historical epidemiological data and machine learning techniques.",
        "Python · scikit-learn · Data analysis · Epidemiology",
        "https://github.com/owilli38/6156-Final-Project-Measles-Detection-Model",
        None,
        None,
    ),
    (
        "04 / Public data",
        "School Board Representation Dashboard",
        "Created an RShiny dashboard comparing representation for students of color and school board members across North Carolina's 115 school districts.",
        "R · RShiny · API · Data cleaning",
        None,
        "https://ncpublicschoolrepresentation.shinyapps.io/NC-Public-School-Representation/",
        None,
    ),
    (
        "05 / AirBNB Analysis",
        "Sicily Investment Strategy",
        "Used linear regression, text mining (sentiment analysis), support vector machines (SVM), heat maps, and time series analysis to make recommendations and strategies.",
        "Python · Data visualization · Analysis",
        "https://github.com/owilli38/DSBA-6211/blob/main/FinalProject6211_for_EDA_Maps_Price.ipynb",
        None,
        None
    ),
    (
        "06 / Undergrad Capstone",
        "What Explains Ranked Choice Voting Adoption?",
        "Used Most Similar Systems and Most Different Systems analysis to examine why Maine and Alaska adopted ranked-choice voting through ballot referendums.",
        "Qualitative & Quantitative analysis · Comparative politics",
        None,
        None,
        "https://www.linkedin.com/in/owen-k-williamson/details/projects/",
    ),
]
for row_start in range(0, len(projects), 3):
    project_columns = st.columns(3, gap="medium")
    for column, (label, title, description, tools, github_url, shiny_url, pdf_url) in zip(project_columns, projects[row_start:row_start + 3]):
        with column:
            project_links = []
            if github_url:
                project_links.append(f'<a href="{github_url}" target="_blank">GitHub Repo ↗</a>')
            if shiny_url:
                project_links.append(f'<a href="{shiny_url}" target="_blank">RShiny App ↗</a>')
            if pdf_url:
                project_links.append(f'<a href="{pdf_url}" target="_blank">Open PDF ↗</a>')
            links_markup = f'<div class="project-links">{"".join(project_links)}</div>' if project_links else ""
            st.markdown(
                f"""
                <div class="project-card">
                    <div class="project-label">{label}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                    <div class="project-tools">{tools}</div>
                    {links_markup}
                </div>
                """,
                unsafe_allow_html=True,
            )


st.markdown('<div id="publications"></div>', unsafe_allow_html=True)
st.markdown("## Publications")
publication_url = "https://www.dhj.davidsonlocal.org/volume-xi/"
st.markdown(
    f"""
        <div class="resume-item">
            <div class="date">Research in progress</div>
            <h3>Publication Matching and Predicting Research Success</h3>
            <p class="role">Wake Forest University School of Medicine · 2026</p>
            <p class="description">Developing an automated workflow to match institutional service forms with downstream PubMed publications, extract high-value keywords from unstructured text, and predict publication success (1 = services requests with one or more publications, 0 otherwise) from service request data.</p>
            <p class="description">Methods include the rentrez package, TF-IDF text mining, LDA topic modeling, cross-validated logistic regression & random forest, and conditional inference trees.</p>
        </div>

        <div class="resume-item">
                    <div class="date">Davidson History Journal</div>
                    <h3>"The Shanghai Polytechnic Institute: How Did the Chinese Respond to Western Learning?"</h3>
                    <p class="role">Davidson College · Fall 2023</p>
                    <p class="description">Explores how the Chinese responded to Western learning through the case study of the Shanghai Polytechnic Institute.</p>
                    <p class="description">Methods include historical document analysis, archival research, and contextual interpretation.</p>
                    <p class="description">Written by Owen Williamson, Edited by Mary Herdelin</p>
                    {f'<p class="project-links"><a href="{publication_url}" target="_blank">View publication ↗</a></p>' if publication_url else ''}
                </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    '<div class="footer">Owen Williamson · Resume </div>',
    unsafe_allow_html=True,
)
