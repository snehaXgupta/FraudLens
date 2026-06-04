import os
import sys
import subprocess

# Ensure python-pptx is installed
try:
    import pptx
except ImportError:
    print("python-pptx not found. Attempting to install it...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-pptx"])
        import pptx
        print("python-pptx successfully installed!")
    except Exception as e:
        print(f"Error installing python-pptx: {e}")
        print("Please run 'pip install python-pptx' manually.")
        sys.exit(1)

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    
    # Set to widescreen (16:9)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Colors
    NAVY = RGBColor(15, 23, 42)       # #0F172A (Primary Background)
    TEAL = RGBColor(13, 148, 136)     # #0D9488 (Primary Accent)
    WHITE = RGBColor(248, 250, 252)   # #F8FAFC (Primary Text)
    GRAY = RGBColor(148, 163, 184)    # #94A3B8 (Secondary Text / Body)
    CARD_BG = RGBColor(30, 41, 59)    # #1E293B (Card/Box Background)
    
    # ----------------------------------------------------
    # Helper: Set slide background color
    # ----------------------------------------------------
    def set_slide_background(slide, color):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    # ----------------------------------------------------
    # Helper: Add header block (Title, subtitle, and thin accent line)
    # ----------------------------------------------------
    def add_slide_header(slide, title_text, category_text="AUTHENTIX PROJECT DECK"):
        # Add a top accent line
        accent_line = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.75), Inches(0.4), Inches(11.833), Inches(0.06)
        )
        accent_line.fill.solid()
        accent_line.fill.fore_color.rgb = TEAL
        accent_line.line.fill.background()
        
        # Add category text (tracker)
        cat_box = slide.shapes.add_textbox(Inches(0.75), Inches(0.5), Inches(8.0), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = TEAL
        
        # Add Title text
        title_box = slide.shapes.add_textbox(Inches(0.75), Inches(0.8), Inches(11.0), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(28)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE

    # ----------------------------------------------------
    # Helper: Add footer / branding
    # ----------------------------------------------------
    def add_slide_footer(slide, current_slide, total_slides=12):
        footer_box = slide.shapes.add_textbox(Inches(0.75), Inches(7.0), Inches(11.833), Inches(0.3))
        tf = footer_box.text_frame
        p = tf.paragraphs[0]
        p.text = f"AuthentiX | Fake Review Detection System"
        p.font.name = "Arial"
        p.font.size = Pt(9)
        p.font.color.rgb = GRAY
        
        # Slide number aligned to right
        p2 = tf.add_paragraph()
        p2.text = f"Slide {current_slide} of {total_slides}"
        p2.font.name = "Arial"
        p2.font.size = Pt(9)
        p2.font.color.rgb = TEAL
        p2.alignment = PP_ALIGN.RIGHT

    # ----------------------------------------------------
    # SLIDE 1: First Empty Page (Minimalist & Aesthetic Cover)
    # ----------------------------------------------------
    slide_layout = prs.slide_layouts[6] # Blank layout
    slide1 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide1, NAVY)
    
    # Add a beautiful modern design element (two overlapping rectangles)
    rect1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), Inches(2.5), Inches(0.15), Inches(2.5))
    rect1.fill.solid()
    rect1.fill.fore_color.rgb = TEAL
    rect1.line.fill.background()
    
    # Simple empty page placeholder text box (to help the user edit or keep empty)
    text_box = slide1.shapes.add_textbox(Inches(1.1), Inches(2.5), Inches(11.0), Inches(2.5))
    tf1 = text_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "[ PRESENTATION COVER ]"
    p1.font.name = "Arial"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    
    p1_sub = tf1.add_paragraph()
    p1_sub.text = "(This slide was requested to be empty. Double-click here to insert your Title, or delete this placeholder text)"
    p1_sub.font.name = "Arial"
    p1_sub.font.size = Pt(14)
    p1_sub.font.color.rgb = GRAY
    
    add_slide_footer(slide1, 1)

    # ----------------------------------------------------
    # SLIDE 2: Second - Intro (Part 1)
    # ----------------------------------------------------
    slide2 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide2, NAVY)
    add_slide_header(slide2, "Introduction: AuthentiX & FraudLens")
    
    # Description box left
    desc_box = slide2.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(6.5), Inches(4.5))
    tf2 = desc_box.text_frame
    tf2.word_wrap = True
    
    bullets2 = [
        "AuthentiX is an advanced web-based intelligence platform built to detect fraudulent, computer-generated, and biased product reviews on major e-commerce platforms.",
        "Combines Natural Language Processing (NLP) with Machine Learning classifiers to inspect review structures, grammar patterns, and user metrics.",
        "Provides multi-modal processing including direct review text validation, speech analysis (voice reviews), and automated web scraping inputs.",
        "Calculates authenticity ratings and sentiment correlation in real-time, helping users make secure and informed purchase decisions."
    ]
    
    for i, b in enumerate(bullets2):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = b
        p.font.name = "Arial"
        p.font.size = Pt(16)
        p.font.color.rgb = WHITE
        p.space_after = Pt(20)
        p.level = 0
        
    # Feature blocks on the right
    block1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.8), Inches(4.8), Inches(2.2))
    block1.fill.solid()
    block1.fill.fore_color.rgb = CARD_BG
    block1.line.color.rgb = TEAL
    block1.line.width = Pt(1.5)
    
    tb_b1 = slide2.shapes.add_textbox(Inches(8.0), Inches(2.0), Inches(4.4), Inches(1.8))
    tf_b1 = tb_b1.text_frame
    tf_b1.word_wrap = True
    p_b1_title = tf_b1.paragraphs[0]
    p_b1_title.text = "INTELLIGENT PREDICTION"
    p_b1_title.font.name = "Arial"
    p_b1_title.font.size = Pt(14)
    p_b1_title.font.bold = True
    p_b1_title.font.color.rgb = TEAL
    
    p_b1_desc = tf_b1.add_paragraph()
    p_b1_desc.text = "Leverages TF-IDF representation paired with optimized ML classifiers to screen out synthetically generated reviews."
    p_b1_desc.font.name = "Arial"
    p_b1_desc.font.size = Pt(12)
    p_b1_desc.font.color.rgb = GRAY
    p_b1_desc.space_before = Pt(8)

    block2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(4.3), Inches(4.8), Inches(2.2))
    block2.fill.solid()
    block2.fill.fore_color.rgb = CARD_BG
    block2.line.color.rgb = TEAL
    block2.line.width = Pt(1.5)
    
    tb_b2 = slide2.shapes.add_textbox(Inches(8.0), Inches(4.5), Inches(4.4), Inches(1.8))
    tf_b2 = tb_b2.text_frame
    tf_b2.word_wrap = True
    p_b2_title = tf_b2.paragraphs[0]
    p_b2_title.text = "SENTIMENT MAPPING"
    p_b2_title.font.name = "Arial"
    p_b2_title.font.size = Pt(14)
    p_b2_title.font.bold = True
    p_b2_title.font.color.rgb = TEAL
    
    p_b2_desc = tf_b2.add_paragraph()
    p_b2_desc.text = "Correlates positive and negative sentiment distribution with fraud probabilities to isolate highly opinionated fake profiles."
    p_b2_desc.font.name = "Arial"
    p_b2_desc.font.size = Pt(12)
    p_b2_desc.font.color.rgb = GRAY
    p_b2_desc.space_before = Pt(8)
    
    add_slide_footer(slide2, 2)

    # ----------------------------------------------------
    # SLIDE 3: Third - Intro (Part 2)
    # ----------------------------------------------------
    slide3 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide3, NAVY)
    add_slide_header(slide3, "Introduction: E-Commerce Review Crisis")
    
    # Left Box - Text details
    left_box = slide3.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(6.5), Inches(4.5))
    tf3 = left_box.text_frame
    tf3.word_wrap = True
    
    bullets3 = [
        "Modern consumer decision making is heavily influenced by social proof, with over 70% of shoppers checking online reviews before purchasing.",
        "This critical reliance has birthed a massive underground industry of fake review farms, selling artificial positive scores and coordinated negative attacks.",
        "The emergence of Generative AI has further allowed bad actors to generate highly authentic, natural-sounding product reviews at scale, leaving traditional heuristic filters obsolete.",
        "AuthentiX steps in as an independent, algorithmically driven verification layer that restores honesty and transparency to online marketplaces."
    ]
    
    for i, b in enumerate(bullets3):
        p = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
        p.text = b
        p.font.name = "Arial"
        p.font.size = Pt(16)
        p.font.color.rgb = WHITE
        p.space_after = Pt(20)
        p.level = 0

    # Right Box - Highlight/Stats Card
    stat_block = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.8), Inches(4.8), Inches(4.7))
    stat_block.fill.solid()
    stat_block.fill.fore_color.rgb = CARD_BG
    stat_block.line.color.rgb = TEAL
    stat_block.line.width = Pt(1.5)
    
    tb_stat = slide3.shapes.add_textbox(Inches(8.0), Inches(2.2), Inches(4.4), Inches(4.0))
    tf_stat = tb_stat.text_frame
    tf_stat.word_wrap = True
    
    p_num = tf_stat.paragraphs[0]
    p_num.text = "70%+"
    p_num.font.name = "Arial"
    p_num.font.size = Pt(72)
    p_num.font.bold = True
    p_num.font.color.rgb = TEAL
    p_num.alignment = PP_ALIGN.CENTER
    
    p_stat_lbl = tf_stat.add_paragraph()
    p_stat_lbl.text = "OF BUYERS RELY ON REVIEWS"
    p_stat_lbl.font.name = "Arial"
    p_stat_lbl.font.size = Pt(14)
    p_stat_lbl.font.bold = True
    p_stat_lbl.font.color.rgb = WHITE
    p_stat_lbl.alignment = PP_ALIGN.CENTER
    p_stat_lbl.space_after = Pt(24)
    
    p_stat_text = tf_stat.add_paragraph()
    p_stat_text.text = "Because e-commerce reviews directly translate to revenue, bad actors actively manipulate ratings. AuthentiX bypasses star-ratings to inspect linguistic signals."
    p_stat_text.font.name = "Arial"
    p_stat_text.font.size = Pt(14)
    p_stat_text.font.color.rgb = GRAY
    p_stat_text.alignment = PP_ALIGN.CENTER
    
    add_slide_footer(slide3, 3)

    # ----------------------------------------------------
    # SLIDE 4: Fourth - Problem Statement
    # ----------------------------------------------------
    slide4 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide4, NAVY)
    add_slide_header(slide4, "Problem Statement")
    
    # 3-column Layout for the Problem Areas
    col_width = Inches(3.6)
    gap = Inches(0.4)
    y_pos = Inches(1.8)
    h_pos = Inches(4.7)
    
    problems = [
        {
            "num": "01",
            "title": "THE TRUST DEFICIT",
            "desc": "Consumers face constant deception from astroturfing campaigns. Authentic sellers are pushed down by competitors buying bulk five-star reviews, creating market imbalance."
        },
        {
            "num": "02",
            "title": "AI-DRIVEN DECEPTION",
            "desc": "Traditional review systems flag simple copy-pasted comments. Modern LLMs write highly specific, context-aware reviews that bypass basic filters, mimicking real buyer speech."
        },
        {
            "num": "03",
            "title": "MANUAL AUDITING FAIL",
            "desc": "It is physically and economically impossible for marketplace operators or customers to manually verify thousands of daily reviews for structured patterns, creating a detection gap."
        }
    ]
    
    for idx, prob in enumerate(problems):
        x_pos = Inches(0.75) + idx * (col_width + gap)
        
        # Background card
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_pos, y_pos, col_width, h_pos)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = TEAL
        card.line.width = Pt(1.5)
        
        tb = slide4.shapes.add_textbox(x_pos + Inches(0.2), y_pos + Inches(0.2), col_width - Inches(0.4), h_pos - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p_num = tf.paragraphs[0]
        p_num.text = prob["num"]
        p_num.font.name = "Arial"
        p_num.font.size = Pt(36)
        p_num.font.bold = True
        p_num.font.color.rgb = TEAL
        
        p_title = tf.add_paragraph()
        p_title.text = prob["title"]
        p_title.font.name = "Arial"
        p_title.font.size = Pt(16)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE
        p_title.space_before = Pt(10)
        p_title.space_after = Pt(15)
        
        p_desc = tf.add_paragraph()
        p_desc.text = prob["desc"]
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(13)
        p_desc.font.color.rgb = GRAY
        
    add_slide_footer(slide4, 4)

    # ----------------------------------------------------
    # SLIDE 5: Fifth - Objectives
    # ----------------------------------------------------
    slide5 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide5, NAVY)
    add_slide_header(slide5, "Project Objectives")
    
    # 4 objective boxes
    obj_w = Inches(5.6)
    obj_h = Inches(2.2)
    
    objs = [
        ("AUTOMATE REVIEW CLASSIFICATION", "Construct a robust classifier that instantly categories dynamic reviews into 'Genuine' or 'Fake' without relying on manual rating analysis."),
        ("REAL-TIME WEB CRAWLING", "Integrate BeautifulSoup and Selenium web crawlers to grab and evaluate reviews directly from active Amazon and Flipkart product links on-demand."),
        ("SENTIMENT & FRAUD MAPPING", "Examine review text sentiments to evaluate if highly emotional patterns (extreme positivity or negativity) correlate to fraudulent accounts."),
        ("INTUITIVE VISUAL INSIGHTS", "Deliver a consumer-facing dashboard showing predictive probabilities, cleaned token metrics, and a searchable history for auditing reviews.")
    ]
    
    positions = [
        (Inches(0.75), Inches(1.8)),
        (Inches(6.983), Inches(1.8)),
        (Inches(0.75), Inches(4.3)),
        (Inches(6.983), Inches(4.3))
    ]
    
    for idx, (title, desc) in enumerate(objs):
        x, y = positions[idx]
        
        # Border box
        box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, obj_w, obj_h)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = TEAL
        box.line.width = Pt(1.5)
        
        # Text
        tb = slide5.shapes.add_textbox(x + Inches(0.2), y + Inches(0.2), obj_w - Inches(0.4), obj_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.name = "Arial"
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = TEAL
        
        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.name = "Arial"
        pd.font.size = Pt(12)
        pd.font.color.rgb = WHITE
        pd.space_before = Pt(8)
        
    add_slide_footer(slide5, 5)

    # ----------------------------------------------------
    # SLIDE 6: Sixth - System Workflow
    # ----------------------------------------------------
    slide6 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide6, NAVY)
    add_slide_header(slide6, "System Workflow & Architecture")
    
    # Draw simple horizontal flow chart
    steps = ["1. Input", "2. Crawl", "3. Process", "4. Vectorize", "5. Classify", "6. Present"]
    details = [
        "Raw review text,\nvoice audio, or\ne-commerce URL.",
        "BeautifulSoup or\nSelenium fetches\nactive website HTML.",
        "Lowercasing,\nspecial character\nstripping, NLTK.",
        "TF-IDF converts\ntext into numerical\nsparse matrices.",
        "Logistic Regression\nscores authenticity\n& lexicon sentiment.",
        "Visual cards show\nverdict, score,\nand review logs."
    ]
    
    card_w = Inches(1.7)
    card_h = Inches(4.5)
    gap_w = Inches(0.3)
    
    for idx, (title, desc) in enumerate(zip(steps, details)):
        x = Inches(0.75) + idx * (card_w + gap_w)
        y = Inches(1.8)
        
        # Shape
        card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = TEAL
        card.line.width = Pt(1.5)
        
        # Text Box
        tb = slide6.shapes.add_textbox(x, y + Inches(0.15), card_w, card_h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = TEAL
        p_t.alignment = PP_ALIGN.CENTER
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = WHITE
        p_d.space_before = Pt(20)
        p_d.alignment = PP_ALIGN.CENTER
        
        # Draw small arrow between cards except last
        if idx < 5:
            arr = slide6.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x + card_w, y + Inches(2.0), Inches(0.3), Inches(0.3))
            arr.fill.solid()
            arr.fill.fore_color.rgb = TEAL
            arr.line.fill.background()
            
    add_slide_footer(slide6, 6)

    # ----------------------------------------------------
    # SLIDE 7: Seventh - Blank Page (Transition / Intermission)
    # ----------------------------------------------------
    slide7 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide7, NAVY)
    
    # Just vertical stripes/lines to look premium and empty
    line1 = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), Inches(0.0), Inches(0.2), Inches(7.5))
    line1.fill.solid()
    line1.fill.fore_color.rgb = TEAL
    line1.line.fill.background()
    
    text_box_s7 = slide7.shapes.add_textbox(Inches(1.5), Inches(3.0), Inches(10.0), Inches(1.5))
    tf7 = text_box_s7.text_frame
    tf7.word_wrap = True
    p7 = tf7.paragraphs[0]
    p7.text = "[ INTERACTIVE DEMO / TRANSITION ]"
    p7.font.name = "Arial"
    p7.font.size = Pt(32)
    p7.font.bold = True
    p7.font.color.rgb = WHITE
    
    p7_sub = tf7.add_paragraph()
    p7_sub.text = "(This slide was requested to be blank. Perfect for a project demo video, a screenshot placeholder, or Q&A segment transition)"
    p7_sub.font.name = "Arial"
    p7_sub.font.size = Pt(14)
    p7_sub.font.color.rgb = GRAY
    
    add_slide_footer(slide7, 7)

    # ----------------------------------------------------
    # SLIDE 8: Eighth - Implementation Details
    # ----------------------------------------------------
    slide8 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide8, NAVY)
    add_slide_header(slide8, "Technical Implementation Details")
    
    # Two main blocks: Pipeline details and Model comparison
    left_card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(1.8), Inches(5.6), Inches(4.7))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = CARD_BG
    left_card.line.color.rgb = TEAL
    left_card.line.width = Pt(1.5)
    
    tb_l = slide8.shapes.add_textbox(Inches(0.95), Inches(2.0), Inches(5.2), Inches(4.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    
    p_lt = tf_l.paragraphs[0]
    p_lt.text = "DATA PROCESSING & NLP"
    p_lt.font.name = "Arial"
    p_lt.font.size = Pt(16)
    p_lt.font.bold = True
    p_lt.font.color.rgb = TEAL
    p_lt.space_after = Pt(12)
    
    l_bullets = [
        "Dataset Merge: Combines computer-generated fake review corpus (CG/OR tags) with parsed Amazon products.",
        "Text Cleaning: Lowercasing, punctuation regex removal, NLTK stopword exclusions (fallback list implemented).",
        "Vectorization: TF-IDF vectorizer converts text corpus into 5000 analytical numerical features.",
        "Scraper System: BeautifulSoup for static selectors + Selenium web driver scripts to load dynamic SPA pages."
    ]
    for b in l_bullets:
        p = tf_l.add_paragraph()
        p.text = b
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.color.rgb = WHITE
        p.space_after = Pt(10)
        p.level = 0
        
    right_card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.983), Inches(1.8), Inches(5.6), Inches(4.7))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = CARD_BG
    right_card.line.color.rgb = TEAL
    right_card.line.width = Pt(1.5)
    
    tb_r = slide8.shapes.add_textbox(Inches(7.183), Inches(2.0), Inches(5.2), Inches(4.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    
    p_rt = tf_r.paragraphs[0]
    p_rt.text = "CLASSIFICATION PIPELINE"
    p_rt.font.name = "Arial"
    p_rt.font.size = Pt(16)
    p_rt.font.bold = True
    p_rt.font.color.rgb = TEAL
    p_rt.space_after = Pt(12)
    
    r_bullets = [
        "Logistic Regression (Best Model): Selected for final deployment due to rapid classification and high accuracy.",
        "Random Forest Classifier: Tested with 100 estimators; provides deep decision-tree boundary evaluation.",
        "Multinomial Naive Bayes: Evaluated as a baseline classifier optimized for text frequency structures.",
        "Production API: Model weights pickled and served dynamically via Flask REST endpoints."
    ]
    for b in r_bullets:
        p = tf_r.add_paragraph()
        p.text = b
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.color.rgb = WHITE
        p.space_after = Pt(10)
        p.level = 0
        
    add_slide_footer(slide8, 8)

    # ----------------------------------------------------
    # SLIDE 9: Ninth - Application
    # ----------------------------------------------------
    slide9 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide9, NAVY)
    add_slide_header(slide9, "Practical Applications & Use Cases")
    
    # 3 boxes for applications
    col_w = Inches(3.6)
    col_gap = Inches(0.4)
    y_pos = Inches(1.8)
    h_pos = Inches(4.7)
    
    apps = [
        {
            "title": "SHOPPING ASSISTANT",
            "desc": "Can be distributed as a browser extension that reads customer reviews on the fly and overlays an authenticity rating directly on Amazon or Flipkart product pages.",
            "color": TEAL
        },
        {
            "title": "BRAND REPUTATION",
            "desc": "Enables corporate brands to audit product listings, trace coordinated negative feedback attacks launched by competitors, and verify authentic consumer feedback.",
            "color": WHITE
        },
        {
            "title": "PLATFORM INTEGRATION",
            "desc": "Provides e-commerce platforms with a scalable plug-and-play API to filter synthetic feedback at submission time, flag reviews for moderation, and keep databases clean.",
            "color": TEAL
        }
    ]
    
    for idx, item in enumerate(apps):
        x = Inches(0.75) + idx * (col_w + col_gap)
        
        card = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y_pos, col_w, h_pos)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = TEAL
        card.line.width = Pt(1.5)
        
        tb = slide9.shapes.add_textbox(x + Inches(0.2), y_pos + Inches(0.2), col_w - Inches(0.4), h_pos - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = item["title"]
        p_t.font.name = "Arial"
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = item["color"]
        p_t.space_after = Pt(20)
        
        p_d = tf.add_paragraph()
        p_d.text = item["desc"]
        p_d.font.name = "Arial"
        p_d.font.size = Pt(14)
        p_d.font.color.rgb = WHITE
        
    add_slide_footer(slide9, 9)

    # ----------------------------------------------------
    # SLIDE 10: Tenth - Limitations
    # ----------------------------------------------------
    slide10 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide10, NAVY)
    add_slide_header(slide10, "System Limitations")
    
    # Left Box: Structural and crawl limits. Right Box: Algorithmic limits
    left_card = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(1.8), Inches(5.6), Inches(4.7))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = CARD_BG
    left_card.line.color.rgb = TEAL
    left_card.line.width = Pt(1.5)
    
    tb_l10 = slide10.shapes.add_textbox(Inches(0.95), Inches(2.0), Inches(5.2), Inches(4.3))
    tf_l10 = tb_l10.text_frame
    tf_l10.word_wrap = True
    
    p_lt10 = tf_l10.paragraphs[0]
    p_lt10.text = "CRAWLER & WEB DEPENDENCIES"
    p_lt10.font.name = "Arial"
    p_lt10.font.size = Pt(16)
    p_lt10.font.bold = True
    p_lt10.font.color.rgb = TEAL
    p_lt10.space_after = Pt(15)
    
    l_bullets10 = [
        "E-commerce websites update their HTML class names and layout structures frequently, breaking hardcoded CSS scraper selectors.",
        "Strict anti-scraping mechanisms (like CAPTCHA walls, Cloudflare challenge pages, and rate limits) block automated request scripts.",
        "Scraping dynamic, single-page applications requires selenium engines which consumes heavy RAM/CPU overhead on deployment servers."
    ]
    for b in l_bullets10:
        p = tf_l10.add_paragraph()
        p.text = b
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.color.rgb = WHITE
        p.space_after = Pt(12)
        
    right_card = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.983), Inches(1.8), Inches(5.6), Inches(4.7))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = CARD_BG
    right_card.line.color.rgb = TEAL
    right_card.line.width = Pt(1.5)
    
    tb_r10 = slide10.shapes.add_textbox(Inches(7.183), Inches(2.0), Inches(5.2), Inches(4.3))
    tf_r10 = tb_r10.text_frame
    tf_r10.word_wrap = True
    
    p_rt10 = tf_r10.paragraphs[0]
    p_rt10.text = "ALGORITHMIC LIMITS"
    p_rt10.font.name = "Arial"
    p_rt10.font.size = Pt(16)
    p_rt10.font.bold = True
    p_rt10.font.color.rgb = TEAL
    p_rt10.space_after = Pt(15)
    
    r_bullets10 = [
        "Text features are based on NLTK English structures; the system is currently blind to local or regional multilingual review manipulation.",
        "TF-IDF vectorizer only analyses token frequencies and fails to capture deep contextual semantic relationships or advanced syntax sarcasm.",
        "Requires active server models. If server resources are restricted and pickle files fail to load, model degrades to a rule-based mock engine."
    ]
    for b in r_bullets10:
        p = tf_r10.add_paragraph()
        p.text = b
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.color.rgb = WHITE
        p.space_after = Pt(12)
        
    add_slide_footer(slide10, 10)

    # ----------------------------------------------------
    # SLIDE 11: Eleventh - Future Enhancement
    # ----------------------------------------------------
    slide11 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide11, NAVY)
    add_slide_header(slide11, "Future Enhancements")
    
    # 4 grid blocks
    positions_s11 = [
        (Inches(0.75), Inches(1.8)),
        (Inches(6.983), Inches(1.8)),
        (Inches(0.75), Inches(4.3)),
        (Inches(6.983), Inches(4.3))
    ]
    
    enhancements = [
        ("ADVANCED DEEP LEARNING", "Replace traditional Logistic Regression with Transformer architectures like BERT or RoBERTa to capture semantic context and AI review patterns."),
        ("ROBUST CRAWLER ROTATION", "Implement residential proxy servers, rotate user agents, and coordinate cloud scraping workers to bypass marketplace CAPTCHAs reliably."),
        ("REAL BROWSER EXTENSION", "Develop a lightweight Chrome/Firefox add-on that extracts review content from product details in real-time, displaying grades as you browse."),
        ("MULTILINGUAL ANALYSIS", "Expand the preprocessing dictionaries and vector model datasets to recognize review syntax in Spanish, Hindi, German, and Mandarin.")
    ]
    
    for idx, (title, desc) in enumerate(enhancements):
        x, y = positions_s11[idx]
        
        card = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = TEAL
        card.line.width = Pt(1.5)
        
        tb = slide11.shapes.add_textbox(x + Inches(0.2), y + Inches(0.2), Inches(5.2), Inches(1.8))
        tf = tb.text_frame
        tf.word_wrap = True
        
        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.name = "Arial"
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = TEAL
        
        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.name = "Arial"
        pd.font.size = Pt(12)
        pd.font.color.rgb = WHITE
        pd.space_before = Pt(8)
        
    add_slide_footer(slide11, 11)

    # ----------------------------------------------------
    # SLIDE 12: Twelfth - Thank You
    # ----------------------------------------------------
    slide12 = prs.slides.add_slide(slide_layout)
    set_slide_background(slide12, NAVY)
    
    # Large center text with card layout
    center_card = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.0), Inches(1.5), Inches(9.333), Inches(4.5))
    center_card.fill.solid()
    center_card.fill.fore_color.rgb = CARD_BG
    center_card.line.color.rgb = TEAL
    center_card.line.width = Pt(2.0)
    
    tb12 = slide12.shapes.add_textbox(Inches(2.5), Inches(2.2), Inches(8.333), Inches(3.0))
    tf12 = tb12.text_frame
    tf12.word_wrap = True
    
    p12 = tf12.paragraphs[0]
    p12.text = "Thank You!"
    p12.font.name = "Arial"
    p12.font.size = Pt(54)
    p12.font.bold = True
    p12.font.color.rgb = TEAL
    p12.alignment = PP_ALIGN.CENTER
    
    p12_sub = tf12.add_paragraph()
    p12_sub.text = "AuthentiX — Restoring Integrity to Digital Reviews"
    p12_sub.font.name = "Arial"
    p12_sub.font.size = Pt(20)
    p12_sub.font.color.rgb = WHITE
    p12_sub.alignment = PP_ALIGN.CENTER
    p12_sub.space_before = Pt(15)
    
    p12_foot = tf12.add_paragraph()
    p12_foot.text = "Questions & Answers Session"
    p12_foot.font.name = "Arial"
    p12_foot.font.size = Pt(14)
    p12_foot.font.color.rgb = GRAY
    p12_foot.alignment = PP_ALIGN.CENTER
    p12_foot.space_before = Pt(30)
    
    add_slide_footer(slide12, 12)

    # Save presentation
    output_path = "AuthentiX_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation successfully created and saved to: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    create_presentation()
