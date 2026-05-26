from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import KeepTogether

# Colors
C_BLUE_DARK   = colors.HexColor('#0C447C')
C_BLUE_MID    = colors.HexColor('#185FA5')
C_BLUE_LIGHT  = colors.HexColor('#B5D4F4')
C_BLUE_BG     = colors.HexColor('#E6F1FB')

C_GREEN_DARK  = colors.HexColor('#27500A')
C_GREEN_MID   = colors.HexColor('#3B6D11')
C_GREEN_LIGHT = colors.HexColor('#C0DD97')
C_GREEN_BG    = colors.HexColor('#EAF3DE')

C_TEAL_DARK   = colors.HexColor('#085041')
C_TEAL_MID    = colors.HexColor('#0F6E56')
C_TEAL_LIGHT  = colors.HexColor('#9FE1CB')
C_TEAL_BG     = colors.HexColor('#E1F5EE')

C_PURPLE_DARK = colors.HexColor('#3C3489')
C_PURPLE_MID  = colors.HexColor('#534AB7')
C_PURPLE_LIGHT= colors.HexColor('#CECBF6')
C_PURPLE_BG   = colors.HexColor('#EEEDFE')

C_AMBER_DARK  = colors.HexColor('#633806')
C_AMBER_MID   = colors.HexColor('#854F0B')
C_AMBER_LIGHT = colors.HexColor('#FAC775')
C_AMBER_BG    = colors.HexColor('#FAEEDA')

C_GRAY_DARK   = colors.HexColor('#444441')
C_GRAY_MID    = colors.HexColor('#5F5E5A')
C_GRAY_LIGHT  = colors.HexColor('#D3D1C7')
C_GRAY_BG     = colors.HexColor('#F1EFE8')

C_CORAL_LIGHT = colors.HexColor('#F5C4B3')
C_CORAL_DARK  = colors.HexColor('#712B13')

WHITE = colors.white
BLACK = colors.HexColor('#1a1a18')

PAGE_W, PAGE_H = landscape(A4)
MARGIN = 14*mm
CONTENT_W = PAGE_W - 2*MARGIN

output_dir = r"C:\black_paper\Python_practice\outputs"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "MedMind_System_Architecture.pdf")

doc = SimpleDocTemplate(
    output_path,
    pagesize=landscape(A4),
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=12*mm,
    bottomMargin=12*mm
)

styles = getSampleStyleSheet()

def style(name, parent='Normal', fontSize=8, textColor=BLACK, alignment=TA_LEFT,
          spaceAfter=0, spaceBefore=0, leading=10, fontName='Helvetica', bold=False):
    return ParagraphStyle(
        name, parent=styles[parent],
        fontSize=fontSize,
        textColor=textColor,
        alignment=alignment,
        spaceAfter=spaceAfter,
        spaceBefore=spaceBefore,
        leading=leading,
        fontName='Helvetica-Bold' if bold else fontName,
    )

TITLE_S   = style('TITLE_S',  fontSize=13, textColor=C_BLUE_DARK, alignment=TA_CENTER, bold=True, leading=16)
SUBTITLE_S= style('SUBTITLE_S',fontSize=7.5, textColor=C_GRAY_MID, alignment=TA_CENTER, leading=10)
SEC_S     = style('SEC_S',    fontSize=8,  textColor=C_BLUE_DARK, bold=True, leading=10, spaceAfter=2)
CARD_H    = style('CARD_H',   fontSize=7.5, textColor=BLACK, bold=True, leading=9, spaceAfter=1)
CARD_B    = style('CARD_B',   fontSize=6.5, textColor=colors.HexColor('#3d3d3a'), leading=9)
CARD_R    = style('CARD_R',   fontSize=6,  textColor=C_GRAY_MID, leading=8, fontName='Courier')
PIPE_S    = style('PIPE_S',   fontSize=6.5, textColor=BLACK, alignment=TA_CENTER, leading=8)
FEAT_S    = style('FEAT_S',   fontSize=6.5, textColor=C_GREEN_DARK, leading=9)
USER_H    = style('USER_H',   fontSize=7.5, textColor=BLACK, bold=True, alignment=TA_CENTER, leading=9)
USER_B    = style('USER_B',   fontSize=6,  textColor=C_GRAY_MID, alignment=TA_CENTER, leading=8)
NOTE_S    = style('NOTE_S',   fontSize=6,  textColor=C_CORAL_DARK, leading=8)

def section_header(text, bg_color, text_color=WHITE):
    return Table(
        [[Paragraph(text, style('sh', fontSize=8, textColor=text_color, bold=True, alignment=TA_CENTER, leading=10))]],
        colWidths=[CONTENT_W],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_color),
            ('ROUNDEDCORNERS', [4]),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
        ])
    )

def card(title, body, route=None, bg=C_BLUE_LIGHT, border=C_BLUE_MID, title_color=C_BLUE_DARK):
    content = [Paragraph(title, style('ch', fontSize=7.5, textColor=title_color, bold=True, leading=9))]
    if body:
        content.append(Paragraph(body, CARD_B))
    if route:
        content.append(Paragraph(route, CARD_R))
    return Table(
        [[content]],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg),
            ('BOX', (0,0), (-1,-1), 0.5, border),
            ('ROUNDEDCORNERS', [4]),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ])
    )

def row_table(cells, col_weights=None, spacing=3):
    n = len(cells)
    if col_weights:
        total = sum(col_weights)
        widths = [(w/total)*(CONTENT_W - spacing*(n-1)) for w in col_weights]
    else:
        w = (CONTENT_W - spacing*(n-1)) / n
        widths = [w]*n
    return Table(
        [cells],
        colWidths=widths,
        style=TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('INNERGRID', (0,0), (-1,-1), 0, colors.transparent),
        ]),
        spaceBefore=0, spaceAfter=spacing
    )

def pipeline_table(steps, colors_list):
    cells = []
    for i, (step, c) in enumerate(zip(steps, colors_list)):
        cells.append(Table(
            [[Paragraph(step, PIPE_S)]],
            style=TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), c),
                ('BOX', (0,0), (-1,-1), 0.5, C_GRAY_MID),
                ('ROUNDEDCORNERS', [3]),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('LEFTPADDING', (0,0), (-1,-1), 4),
                ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ])
        ))
        if i < len(steps)-1:
            cells.append(Paragraph('  →  ', style('arr', fontSize=8, textColor=C_GRAY_MID, alignment=TA_CENTER)))

    n = len(cells)
    step_count = len(steps)
    arrow_count = step_count - 1
    arrow_w = 14
    step_w = (CONTENT_W - arrow_count*arrow_w - 6) / step_count
    widths = []
    for i in range(n):
        widths.append(arrow_w if i % 2 == 1 else step_w)

    return Table(
        [cells],
        colWidths=widths,
        style=TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ])
    )

def user_card(title, body, bg, border):
    return Table(
        [[Paragraph(title, USER_H), Paragraph(body, USER_B)]],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg),
            ('BOX', (0,0), (-1,-1), 0.5, border),
            ('ROUNDEDCORNERS', [5]),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ])
    )

def arrow_row(label=''):
    t = '▼  ' + label if label else '▼'
    return Paragraph(t, style('arr', fontSize=8, textColor=C_GRAY_MID, alignment=TA_CENTER, leading=10, spaceAfter=2, spaceBefore=2))

def section_box(content_rows, bg, border, label=None):
    inner = []
    if label:
        inner.append(Paragraph(label, style('lb', fontSize=7, textColor=C_GRAY_MID, bold=True, leading=9, spaceAfter=3)))
    inner.extend(content_rows)
    return Table(
        [[inner]],
        colWidths=[CONTENT_W],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg),
            ('BOX', (0,0), (-1,-1), 1, border),
            ('ROUNDEDCORNERS', [6]),
            ('TOPPADDING', (0,0), (-1,-1), 7),
            ('BOTTOMPADDING', (0,0), (-1,-1), 7),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]),
        spaceAfter=5
    )

story = []

# ── TITLE ──────────────────────────────────────────────────────────────────
story.append(Paragraph('MEDMIND — AI HEALTH INTELLIGENCE PLATFORM', TITLE_S))
story.append(Paragraph('System Design Architecture · Final Year Project · AI-powered locally-deployable health intelligence web platform · Zero paid cloud cost', SUBTITLE_S))
story.append(Spacer(1, 4))
story.append(HRFlowable(width=CONTENT_W, thickness=1, color=C_BLUE_MID, spaceAfter=5))

# ── USERS LAYER ─────────────────────────────────────────────────────────────
story.append(section_box([
    row_table([
        user_card('General user / patient',
                  'Sign up · upload lab reports · view explanations\nDiet & lifestyle recs · AI health chat · blog · profile',
                  C_BLUE_LIGHT, C_BLUE_MID),
        user_card('Caregiver / health-conscious',
                  'Upload reports · track health trends\nAI Q&A · read educational content',
                  C_TEAL_LIGHT, C_TEAL_MID),
        user_card('Admin / content manager',
                  'Manage users · blog CRUD · knowledge base\nAudit logs · health categories',
                  C_AMBER_LIGHT, C_AMBER_MID),
        user_card('AI health assistant',
                  'Explains lab reports · RAG Q&A\nGenerates recs · simplifies medical terms',
                  C_PURPLE_LIGHT, C_PURPLE_MID),
    ])
], C_BLUE_BG, C_BLUE_MID, label='USERS / ACTORS'))

story.append(arrow_row('Interactions'))

# ── CLIENT LAYER ─────────────────────────────────────────────────────────────
story.append(section_box([
    row_table([
        card('Web application',
             'React + Vite  ·  TailwindCSS  ·  REST API communication  ·  WebSocket chat streaming\nSidebar dashboard UI  ·  Responsive layout',
             bg=C_BLUE_LIGHT, border=C_BLUE_MID, title_color=C_BLUE_DARK),
        card('Frontend screens (20 views)',
             'Landing · Sign up / Login · Dashboard · Upload report · Report processing · Analysis overview · Test explanation · Report history · Health profile · Lifestyle dashboard · Diet plan · Exercise plan · AI health chat · Report-aware chat · Blog listing · Blog reading · Blog search · User profile · Settings · Admin blog management',
             bg=C_BLUE_BG, border=C_BLUE_MID, title_color=C_BLUE_DARK),
        card('Optional mobile / PWA',
             'React Native or responsive PWA\nSame backend APIs · Future extension',
             bg=C_GRAY_BG, border=C_GRAY_MID, title_color=C_GRAY_DARK),
    ], col_weights=[1.2, 2.2, 1])
], C_BLUE_BG, C_BLUE_MID, label='CLIENT LAYER'))

story.append(arrow_row('REST API + WebSocket'))

# ── APPLICATION LAYER ─────────────────────────────────────────────────────
gw = card('API gateway',
          'REST API  ·  WebSocket API  ·  JWT Authentication  ·  Request validation  ·  Role-based access control',
          bg=C_GREEN_LIGHT, border=C_GREEN_MID, title_color=C_GREEN_DARK)

svc_row1 = row_table([
    card('Auth service',
         'Register/login · JWT tokens · bcrypt · role-based access · sessions',
         route='POST /api/auth/register  |  POST /api/auth/login  |  POST /api/auth/refresh',
         bg=C_GREEN_LIGHT, border=C_GREEN_MID, title_color=C_GREEN_DARK),
    card('User profile service',
         'Health profile · age/sex/weight/BMI · activity level · conditions · dietary restrictions · health goals',
         route='GET /api/users/me  |  PUT /api/users/profile  |  DELETE /api/users',
         bg=C_GREEN_LIGHT, border=C_GREEN_MID, title_color=C_GREEN_DARK),
    card('Lab report analysis service',
         'Upload PDF/DOCX/TXT · parse & extract tests · compare normal ranges · classify Normal/Low/High/Critical · plain-English explanations · store results',
         route='POST /api/lab/upload  |  POST /api/lab/analyze/{doc_id}  |  GET /api/lab/history',
         bg=C_TEAL_LIGHT, border=C_TEAL_MID, title_color=C_TEAL_DARK),
    card('Lifestyle & diet service',
         '7-day diet plan · exercise plan · lifestyle tips · WHO/AHA/ADA guidelines · structured JSON output',
         route='POST /api/lifestyle/recommend  |  GET /api/lifestyle/{user_id}/latest',
         bg=C_TEAL_LIGHT, border=C_TEAL_MID, title_color=C_TEAL_DARK),
])
svc_row2 = row_table([
    card('Blog service',
         'Health article CRUD · categories: Nutrition, Diseases, Lifestyle, Mental Health, Lab Insights · Markdown rendering · blog search · admin management',
         route='GET /api/blogs  |  POST /api/blogs  |  GET /api/blogs/search?q=',
         bg=C_GREEN_LIGHT, border=C_GREEN_MID, title_color=C_GREEN_DARK),
    card('RAG health Q&A service',
         'Conversational AI · retrieves medical knowledge chunks · optional report-aware mode · WebSocket streaming · source citations · grounded answers',
         route='WS /ws/qa  |  POST /api/qa  |  GET /api/qa/history',
         bg=C_PURPLE_LIGHT, border=C_PURPLE_MID, title_color=C_PURPLE_DARK),
    card('Report history & trend service',
         'Store reports · view past analyses · compare old & new results · track HbA1c, cholesterol, creatinine trends · generate trend charts',
         bg=C_GREEN_LIGHT, border=C_GREEN_MID, title_color=C_GREEN_DARK),
    card('Admin service',
         'Manage users · blog content · medical knowledge base · view analytics · audit logs',
         bg=C_AMBER_LIGHT, border=C_AMBER_MID, title_color=C_AMBER_DARK),
])

story.append(section_box([gw, Spacer(1, 4), svc_row1, Spacer(1, 3), svc_row2],
    C_GREEN_BG, C_GREEN_MID, label='APPLICATION LAYER / BACKEND — FastAPI + Python'))

story.append(arrow_row('AI calls'))

# ── AI PROCESSING LAYER ──────────────────────────────────────────────────────
ai_row = row_table([
    card('Document parser',
         'Extract text & tables from PDF, DOCX, TXT\nPyMuPDF · pdfplumber · python-docx · Regex',
         bg=C_TEAL_LIGHT, border=C_TEAL_MID, title_color=C_TEAL_DARK),
    card('Medical NER & extraction',
         'Extract test names, values, units, entities\nscispaCy · Regex · Biomedical NLP',
         bg=C_TEAL_LIGHT, border=C_TEAL_MID, title_color=C_TEAL_DARK),
    card('Lab analyzer',
         'Compare values vs normal ranges · classify results\nLOINC CSV · SQLite · pandas',
         bg=C_TEAL_LIGHT, border=C_TEAL_MID, title_color=C_TEAL_DARK),
    card('Explanation generator',
         'Plain-English lab result explanations\nBioGPT · Mistral 7B · Ollama',
         bg=C_TEAL_LIGHT, border=C_TEAL_MID, title_color=C_TEAL_DARK),
    card('Lifestyle recommender',
         'Diet, exercise & lifestyle plans from profile + lab results\nMistral 7B · LangChain · Pydantic',
         bg=C_GREEN_LIGHT, border=C_GREEN_MID, title_color=C_GREEN_DARK),
    card('RAG pipeline',
         'Embed → retrieve → inject → generate → stream\nLangChain · ChromaDB · all-MiniLM-L6-v2 · Mistral 7B',
         bg=C_PURPLE_LIGHT, border=C_PURPLE_MID, title_color=C_PURPLE_DARK),
    card('Medical term simplifier',
         'Complex terms → plain English · React tooltip\nscispaCy · Mistral 7B',
         bg=C_TEAL_LIGHT, border=C_TEAL_MID, title_color=C_TEAL_DARK),
])

rag_pipe = pipeline_table(
    ['User question', 'Embed query\n(all-MiniLM-L6-v2)', 'Retrieve top-5 chunks\n(ChromaDB)', 'Inject lab context', 'Build prompt\n(system+context+history)', 'Mistral 7B\n(Ollama)', 'Stream + cite\n(WebSocket)'],
    [C_BLUE_LIGHT, C_TEAL_LIGHT, C_PURPLE_LIGHT, C_TEAL_LIGHT, C_GREEN_LIGHT, C_AMBER_LIGHT, C_PURPLE_LIGHT]
)
lab_pipe = pipeline_table(
    ['File upload', 'Text extraction', 'Section detection', 'Medical NER', 'Range comparison', 'Explanation LLM', 'Store & display'],
    [C_BLUE_LIGHT, C_TEAL_LIGHT, C_TEAL_LIGHT, C_TEAL_LIGHT, C_GREEN_LIGHT, C_AMBER_LIGHT, C_PURPLE_LIGHT]
)
life_pipe = pipeline_table(
    ['Fetch lab results', 'Fetch health profile', 'Rule lookup', 'Guideline retrieval\n(ChromaDB)', 'LLM generation\n(Mistral 7B)', 'Output parsing\n(Pydantic)', 'Store & display'],
    [C_BLUE_LIGHT, C_BLUE_LIGHT, C_TEAL_LIGHT, C_GREEN_LIGHT, C_AMBER_LIGHT, C_PURPLE_LIGHT, C_GREEN_LIGHT]
)

note = Paragraph('Answer only from retrieved context  ·  Never diagnose  ·  Always recommend consulting a doctor for personal medical decisions', NOTE_S)

story.append(section_box([
    ai_row,
    Spacer(1, 5),
    Paragraph('RAG-based health Q&A pipeline', style('ph', fontSize=7, textColor=C_PURPLE_DARK, bold=True, spaceAfter=3)),
    rag_pipe,
    note,
    Spacer(1, 4),
    Paragraph('Lab report analysis pipeline', style('ph2', fontSize=7, textColor=C_TEAL_DARK, bold=True, spaceAfter=3)),
    lab_pipe,
    Spacer(1, 4),
    Paragraph('Lifestyle recommendation pipeline', style('ph3', fontSize=7, textColor=C_GREEN_DARK, bold=True, spaceAfter=3)),
    life_pipe,
], C_TEAL_BG, C_TEAL_MID, label='AI PROCESSING LAYER'))

story.append(arrow_row())

# ── BOTTOM ROW: DATA + KNOWLEDGE + EXTERNAL + DEPLOYMENT ─────────────────
col_w = (CONTENT_W - 9) / 4

def mini_card(title, body, bg, border, tc):
    return Table([[Paragraph(title, style('mc', fontSize=7, textColor=tc, bold=True, leading=8)),
                   Paragraph(body, style('mb', fontSize=6, textColor=colors.HexColor('#3d3d3a'), leading=8))]],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg),
            ('BOX', (0,0), (-1,-1), 0.5, border),
            ('ROUNDEDCORNERS', [3]),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]), spaceAfter=3)

def col_section(title, items, bg, border, tc):
    content = [Paragraph(title, style('cst', fontSize=7.5, textColor=tc, bold=True, leading=10, spaceAfter=4))]
    for t, b, cbg, cbord in items:
        content.append(mini_card(t, b, cbg, cbord, tc))
    return Table([[content]], colWidths=[col_w],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg),
            ('BOX', (0,0), (-1,-1), 1, border),
            ('ROUNDEDCORNERS', [5]),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))

data_col = col_section('DATA LAYER', [
    ('PostgreSQL', 'users · health_profiles · lab_reports · lab_test_results · recommendations · blogs · blog_categories · qa_sessions · qa_messages · audit_log', C_BLUE_LIGHT, C_BLUE_MID),
    ('ChromaDB vector DB', 'medical_kb · guidelines · user_reports · blog_embeddings (optional)\nsentence-transformers · local persisted storage', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('SQLite local cache', 'loinc_ranges · drug_interactions_cache · static_medical_terms · condition_recommendations', C_GRAY_LIGHT, C_GRAY_MID),
    ('File storage', 'Uploaded lab reports · generated PDFs · blog images · exported health summaries', C_AMBER_LIGHT, C_AMBER_MID),
], C_BLUE_BG, C_BLUE_MID, C_BLUE_DARK)

kb_col = col_section('MEDICAL KNOWLEDGE BASE', [
    ('Guidelines & standards', 'LOINC lab ranges · WHO health guidelines · AHA cardiovascular guidelines · ADA diabetes guidelines', C_TEAL_LIGHT, C_TEAL_MID),
    ('Medical content', 'MedlinePlus articles · PubMed abstracts · condition recommendation JSON · symptom-condition knowledge base · drug interaction cache / RxNorm (optional)', C_TEAL_LIGHT, C_TEAL_MID),
    ('Feeds into:', 'Lab Analyzer · Lifestyle Recommender · RAG Q&A · Medical Term Simplifier · Symptom Checker (optional)', C_GREEN_LIGHT, C_GREEN_MID),
], C_TEAL_BG, C_TEAL_MID, C_TEAL_DARK)

ext_col = col_section('EXTERNAL / LOCAL AI SERVICES', [
    ('Ollama local LLM runtime', 'Mistral 7B · local inference · no paid API required · CPU-friendly', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('Optional cloud LLM', 'OpenAI API or Azure OpenAI · fallback only', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('Email service', 'SMTP / SendGrid (optional) · email verification · password reset · health reminders', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('Medical data sources', 'LOINC · MedlinePlus · WHO · AHA · ADA · PubMed · RxNorm (optional)', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('PDF export service', 'ReportLab · health summaries · diet plans · doctor-shareable reports', C_PURPLE_LIGHT, C_PURPLE_MID),
], C_PURPLE_BG, C_PURPLE_MID, C_PURPLE_DARK)

deploy_steps = pipeline_table(
    ['GitHub', 'GitHub\nActions', 'Deploy\nfrontend', 'Deploy\nbackend', 'DB backup', 'Monitoring'],
    [C_GRAY_LIGHT, C_PURPLE_LIGHT, C_BLUE_LIGHT, C_GREEN_LIGHT, C_TEAL_LIGHT, C_AMBER_LIGHT]
)
deploy_items = [
    ('Local development', 'Laptop-runnable · zero cloud cost · CPU-friendly AI · optional GPU', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('Frontend hosting', 'Vercel · Netlify · local React dev server', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('Backend hosting', 'FastAPI · Uvicorn · Docker (optional) · Railway / Render (optional)', C_PURPLE_LIGHT, C_PURPLE_MID),
    ('DB hosting', 'Local PostgreSQL · Docker PostgreSQL · Supabase (optional)', C_PURPLE_LIGHT, C_PURPLE_MID),
]
deploy_content = [Paragraph('DEPLOYMENT & INFRASTRUCTURE', style('dh', fontSize=7.5, textColor=C_PURPLE_DARK, bold=True, leading=10, spaceAfter=4))]
for t, b, cbg, cbord in deploy_items:
    deploy_content.append(mini_card(t, b, cbg, cbord, C_PURPLE_DARK))
deploy_content.append(Spacer(1,3))
deploy_content.append(Paragraph('CI/CD pipeline:', style('cip', fontSize=6.5, textColor=C_PURPLE_DARK, bold=True, spaceAfter=2)))
deploy_content.append(deploy_steps)
deploy_col = Table([[deploy_content]], colWidths=[col_w],
    style=TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_PURPLE_BG),
        ('BOX', (0,0), (-1,-1), 1, C_PURPLE_MID),
        ('ROUNDEDCORNERS', [5]),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))

story.append(row_table([data_col, kb_col, ext_col, deploy_col]))

story.append(Spacer(1, 4))

# ── KEY FEATURES + OPTIONAL MODULES ──────────────────────────────────────────
features = [
    'AI lab report explanation', 'Plain-English medical interpretation',
    'Normal / Low / High / Critical classification', 'Personalized diet plan',
    'Exercise & lifestyle recommendations', 'RAG-based health Q&A',
    'Report-aware AI chat', 'Source-cited AI answers',
    'Health blog platform', 'Blog search & categories',
    'Health profile management', 'Report history & trends',
    'Admin content management', 'JWT authentication',
    'Role-based access control', 'Local LLM support (Ollama)',
    'ChromaDB vector search', 'PostgreSQL data storage',
    'Zero paid cloud cost', 'Responsible AI medical disclaimer',
]
feat_cells = [[Paragraph('✓  ' + f, FEAT_S) for f in features[i:i+4]] for i in range(0, len(features), 4)]
feat_table = Table(feat_cells, colWidths=[(CONTENT_W*0.65/4)]*4,
    style=TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
    ]))

future_mods = ['Medical term simplifier', 'Report history manager', 'Report comparison tool',
               'Health trend tracker', 'Medication interaction checker',
               'AI health summary generator', 'Symptom checker', 'Health reminders']
fut_content = [Paragraph('OPTIONAL / FUTURE MODULES', style('fh', fontSize=7.5, textColor=C_GRAY_DARK, bold=True, leading=10, spaceAfter=4))]
for m in future_mods:
    fut_content.append(Paragraph('○  ' + m, style('fm', fontSize=6.5, textColor=C_GRAY_DARK, leading=9)))
fut_content.append(Spacer(1,3))
fut_content.append(Paragraph('Future enhancements after core modules are complete.', style('fn', fontSize=6, textColor=C_GRAY_MID, leading=8, fontName='Helvetica-Oblique')))

fut_w = CONTENT_W * 0.32
feat_w = CONTENT_W - fut_w - 4

feat_box = Table([[Paragraph('KEY FEATURES', style('kfh', fontSize=7.5, textColor=C_GREEN_DARK, bold=True, leading=10, spaceAfter=4)), feat_table]],
    colWidths=[feat_w],
    style=TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_GREEN_BG),
        ('BOX', (0,0), (-1,-1), 1, C_GREEN_MID),
        ('ROUNDEDCORNERS', [5]),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))

fut_box = Table([[fut_content]], colWidths=[fut_w],
    style=TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_GRAY_BG),
        ('BOX', (0,0), (-1,-1), 1, C_GRAY_MID),
        ('ROUNDEDCORNERS', [5]),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))

story.append(row_table([feat_box, fut_box], col_weights=[feat_w, fut_w]))

doc.build(story)
print(f"PDF generated successfully: {output_path}")