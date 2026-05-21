import streamlit as st


def apply_css():
    st.markdown(
        """
        <style>
        @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap");

        :root {
            /* Deep navy — clinical authority */
            --navy-950: #080f20;
            --navy-900: #0c1f3f;
            --navy-800: #112d52;
            --navy-700: #183d6b;
            --navy-600: #1f5080;
            /* Medical blue — primary action / accent */
            --blue-600: #1a6eb5;
            --blue-500: #2480cc;
            --blue-400: #56a0dc;
            --blue-100: #dbeafe;
            /* Sky accent — section bars, highlights */
            --sky-500: #0ea5e9;
            --sky-300: #7dd3fc;
            --bg-main: #eef2f7;
            --bg-card: #ffffff;
            --border: #dde3ec;
            --border-strong: #c8d2e0;
            --text-900: #0d1b2a;
            --text-700: #2d3f52;
            --text-500: #5a6e82;
            --text-400: #8fa0b0;
            --red-600: #dc2626;
            --amber-600: #d97706;
            --green-600: #059669;
            --shadow-sm: 0 1px 3px rgba(8,20,48,0.08), 0 1px 2px rgba(8,20,48,0.05);
            --shadow-md: 0 4px 16px rgba(8,20,48,0.10);
            --radius: 10px;
            --radius-sm: 6px;
        }

        html, body, [class*="css"] {
            font-family: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif !important;
        }

        /* Clean light-gray main background */
        .stApp,
        [data-testid="stAppViewContainer"] {
            background-color: var(--bg-main) !important;
            background-image: none !important;
        }

        html, body {
            background: var(--bg-main) !important;
        }

        [data-testid="stMain"] {
            background: transparent !important;
            max-width: 1380px !important;
            margin: 0 auto !important;
            padding: 4.5rem 2rem 3rem !important;
            box-sizing: border-box;
        }

        [data-testid="stMain"] .block-container {
            background: transparent !important;
            padding: 0 !important;
            max-width: none !important;
        }

        [data-testid="stHeader"] {
            background: rgba(243, 244, 248, 0.92) !important;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border-bottom: 1px solid var(--border);
        }

        /* ── SIDEBAR ─────────────────────────────────────── */
        section[data-testid="stSidebar"] {
            background: linear-gradient(175deg, var(--navy-950) 0%, var(--navy-900) 45%, var(--navy-800) 100%) !important;
            min-width: 230px !important;
            max-width: 230px !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
            box-shadow: 4px 0 24px rgba(0, 0, 0, 0.3);
        }

        section[data-testid="stSidebar"] .block-container {
            padding: 1.35rem 1rem 2rem !important;
        }

        section[data-testid="stSidebar"] {
            color: rgba(255, 255, 255, 0.85) !important;
        }

        /* Brand */
        .sidebar-brand {
            padding-bottom: 1.1rem;
            margin-bottom: 0.35rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .sidebar-brand__mark {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 36px;
            height: 36px;
            border-radius: 8px;
            background: var(--blue-500);
            color: #ffffff;
            font-size: 1.1rem;
            font-weight: 900;
            margin-bottom: 0.6rem;
            box-shadow: 0 4px 12px rgba(36, 128, 204, 0.4);
        }

        .sidebar-brand__title {
            font-size: 0.88rem;
            font-weight: 700;
            color: #ffffff !important;
            line-height: 1.2;
            margin: 0 0 0.2rem 0;
            letter-spacing: -0.01em;
        }

        .sidebar-brand__tag {
            font-size: 0.67rem;
            color: rgba(255, 255, 255, 0.45) !important;
            letter-spacing: 0.015em;
            line-height: 1.4;
        }

        /* Section labels */
        .sidebar-nav-label,
        .sidebar-filters-label {
            font-size: 0.62rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.36) !important;
            margin: 1rem 0 0.4rem 0;
        }

        .sidebar-filters-label {
            margin-top: 1.4rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }

        /* Radio nav items */
        section[data-testid="stSidebar"] [data-testid="stRadio"] label {
            padding: 0.38rem 0.65rem !important;
            margin: 0.1rem 0 !important;
            border-radius: var(--radius-sm) !important;
            border: 1px solid transparent !important;
            color: rgba(255, 255, 255, 0.65) !important;
            -webkit-text-fill-color: rgba(255, 255, 255, 0.65) !important;
            font-size: 0.84rem !important;
            font-weight: 500 !important;
            transition: background 0.14s ease, color 0.14s ease;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label p,
        section[data-testid="stSidebar"] [data-testid="stRadio"] label span,
        section[data-testid="stSidebar"] [data-testid="stRadio"] label div {
            color: rgba(255, 255, 255, 0.65) !important;
            -webkit-text-fill-color: rgba(255, 255, 255, 0.65) !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
            background: rgba(255, 255, 255, 0.08) !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover p,
        section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover span {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
            background: var(--blue-600) !important;
            border-color: rgba(26, 110, 181, 0.5) !important;
            font-weight: 600 !important;
            box-shadow: 0 2px 8px rgba(26, 110, 181, 0.35) !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) p,
        section[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) span,
        section[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) div {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] input[type="radio"] {
            accent-color: var(--blue-400);
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] span {
            color: rgba(255, 255, 255, 0.7) !important;
            font-size: 0.74rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.08em !important;
        }

        /* Sidebar controls */
        section[data-testid="stSidebar"] [data-baseweb="select"] > div {
            background: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: var(--radius-sm) !important;
            color: rgba(255, 255, 255, 0.88) !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="select"] input,
        section[data-testid="stSidebar"] [data-baseweb="select"] [data-testid="stMarkdownContainer"] p {
            color: rgba(255, 255, 255, 0.88) !important;
            -webkit-text-fill-color: rgba(255, 255, 255, 0.88) !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="select"] svg {
            fill: rgba(255, 255, 255, 0.55) !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="tag"] {
            background: rgba(36, 128, 204, 0.25) !important;
            color: #bae6fd !important;
            border: 1px solid rgba(36, 128, 204, 0.5) !important;
        }

        section[data-testid="stSidebar"] .stTextInput > div > div {
            background: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: var(--radius-sm) !important;
        }

        section[data-testid="stSidebar"] .stTextInput input {
            background: transparent !important;
            color: rgba(255, 255, 255, 0.88) !important;
            -webkit-text-fill-color: rgba(255, 255, 255, 0.88) !important;
            border: none !important;
        }

        section[data-testid="stSidebar"] .stTextInput input::placeholder {
            color: rgba(255, 255, 255, 0.32) !important;
            -webkit-text-fill-color: rgba(255, 255, 255, 0.32) !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="slider"] {
            background: rgba(255, 255, 255, 0.06) !important;
            border-radius: var(--radius-sm) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            padding: 0.5rem 0.75rem 0.6rem !important;
        }

        section[data-testid="stSidebar"] [data-testid="stTickBarMin"],
        section[data-testid="stSidebar"] [data-testid="stTickBarMax"] {
            color: rgba(255, 255, 255, 0.38) !important;
        }

        /* ── PAGE HERO ──────────────────────────────────── */
        .page-hero {
            margin-bottom: 1.25rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border);
        }

        .page-title {
            font-size: clamp(1.5rem, 2.5vw, 1.9rem);
            font-weight: 800;
            color: var(--text-900);
            letter-spacing: -0.035em;
            line-height: 1.15;
            margin: 0 0 0.3rem 0;
        }

        .page-subtitle {
            color: var(--text-500);
            font-size: 0.875rem;
            font-weight: 400;
            line-height: 1.55;
            margin: 0;
            max-width: 52rem;
        }

        /* ── ALERT BANNER ───────────────────────────────── */
        .alert-banner {
            background: linear-gradient(135deg, var(--navy-900) 0%, var(--navy-700) 100%);
            border-radius: var(--radius);
            padding: 0.8rem 1.1rem;
            margin-bottom: 1.2rem;
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            border: 1px solid rgba(26, 110, 181, 0.25);
            box-shadow: 0 2px 10px rgba(8, 20, 48, 0.2);
        }

        .alert-banner__icon {
            font-size: 1rem;
            flex-shrink: 0;
            margin-top: 0.1rem;
        }

        .alert-banner__title {
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--sky-300);
            margin-bottom: 0.15rem;
            letter-spacing: -0.01em;
        }

        .alert-banner__body {
            font-size: 0.78rem;
            color: rgba(255, 255, 255, 0.68);
            line-height: 1.45;
        }

        /* ── SPACERS ────────────────────────────────────── */
        .section-spacer--sm { height: 0.5rem; }
        .section-spacer--md { height: 0.9rem; }
        .section-spacer--lg { height: 1.4rem; }
        .section-spacer--xl { height: 2rem; }

        /* ── KPI CARDS ──────────────────────────────────── */
        .kpi-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 0.95rem 1.1rem 0.9rem;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.18s ease, transform 0.18s ease;
        }

        .kpi-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        .kpi-label {
            font-size: 0.615rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--text-400);
            margin-bottom: 0.38rem;
        }

        .kpi-value {
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--text-900);
            line-height: 1.1;
            letter-spacing: -0.03em;
            font-variant-numeric: tabular-nums;
        }

        .kpi-card--emphasis .kpi-value {
            color: var(--navy-800);
            font-size: 1.8rem;
        }

        .kpi-sublabel {
            font-size: 0.7rem;
            color: var(--text-400);
            margin-top: 0.18rem;
        }

        /* ── PANELS ─────────────────────────────────────── */
        [data-testid="stMain"] div[data-testid="stVerticalBlockBorderWrapper"] {
            margin-bottom: 1rem !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--bg-card) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius) !important;
            box-shadow: var(--shadow-sm) !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            padding: 1rem 1.1rem 1.1rem !important;
        }

        /* Section headings — medical blue left-bar accent */
        .section-heading {
            font-size: 0.875rem;
            font-weight: 700;
            color: var(--text-900);
            letter-spacing: -0.02em;
            margin: 0 0 0.7rem 0;
            padding: 0 0 0.6rem 0.8rem;
            border-bottom: 1px solid var(--border);
            border-left: 3px solid var(--sky-500);
            line-height: 1.3;
        }

        /* Plotly mat */
        [data-testid="stMain"] [data-testid="stPlotlyChart"] {
            border-radius: var(--radius-sm);
            border: 1px solid var(--border);
            background: #fafafa;
            padding: 0.2rem 0.3rem 0.1rem;
            margin-top: 0.1rem;
        }

        /* Data grid */
        div[data-testid="stDataFrame"] {
            border-radius: var(--radius-sm);
            overflow: hidden;
            border: 1px solid var(--border);
            box-shadow: var(--shadow-sm);
            background: #ffffff !important;
            margin-top: 0.1rem;
            --gdg-bg-cell: #ffffff !important;
            --gdg-bg-bubble: #f9fafb !important;
            --gdg-bg-header: #f9fafb !important;
            --gdg-bg-header-has-focus: #f3f4f6 !important;
            --gdg-border-color: #e5e7eb !important;
            --gdg-text-dark: #111827 !important;
            --gdg-text-medium: #374151 !important;
            --gdg-text-light: #6b7280 !important;
            --gdg-text-group-header: #111827 !important;
            --gdg-accent-color: #1a6eb5 !important;
            --gdg-accent-light: rgba(26, 110, 181, 0.12) !important;
            --gdg-accent-fg: #ffffff !important;
            --gdg-link-color: #1a6eb5 !important;
            --gdg-font-family: "Inter", system-ui, sans-serif !important;
            --gdg-header-font-style: 600 12px !important;
            --gdg-editor-font-size: 13px !important;
        }

        div[data-testid="stDataFrame"] > div {
            --gdg-bg-cell: #ffffff !important;
            --gdg-bg-header: #f0f5fb !important;
            --gdg-border-color: #dde3ec !important;
            --gdg-text-dark: #0d1b2a !important;
            --gdg-accent-color: #1a6eb5 !important;
            --gdg-accent-light: rgba(26, 110, 181, 0.12) !important;
            --gdg-font-family: "Inter", system-ui, sans-serif !important;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.2rem;
            background: #f3f4f6;
            padding: 0.28rem;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 5px !important;
            font-weight: 600 !important;
            font-size: 0.83rem !important;
            color: var(--text-500) !important;
            padding: 0.32rem 0.85rem !important;
        }

        .stTabs [aria-selected="true"] {
            background: #ffffff !important;
            color: var(--blue-600) !important;
            box-shadow: var(--shadow-sm) !important;
        }

        /* Buttons */
        .stButton > button {
            border-radius: var(--radius-sm) !important;
            font-weight: 600 !important;
            border: none !important;
            background: var(--blue-600) !important;
            color: #ffffff !important;
            padding: 0.38rem 1rem !important;
            font-size: 0.84rem !important;
            box-shadow: 0 2px 8px rgba(26, 110, 181, 0.28) !important;
            transition: background 0.15s ease, box-shadow 0.15s ease !important;
        }

        .stButton > button:hover {
            background: var(--blue-500) !important;
            box-shadow: 0 4px 14px rgba(26, 110, 181, 0.38) !important;
        }

        div[data-testid="stAlert"] {
            border-radius: var(--radius-sm) !important;
        }

        /* Priority badges */
        .badge-high {
            display: inline-flex;
            align-items: center;
            padding: 3px 10px;
            border-radius: 999px;
            background: #fef2f2;
            color: #b91c1c;
            font-weight: 700;
            font-size: 0.78rem;
            border: 1px solid #fecaca;
        }

        .badge-medium {
            display: inline-flex;
            align-items: center;
            padding: 3px 10px;
            border-radius: 999px;
            background: #fffbeb;
            color: #b45309;
            font-weight: 700;
            font-size: 0.78rem;
            border: 1px solid #fde68a;
        }

        .badge-low {
            display: inline-flex;
            align-items: center;
            padding: 3px 10px;
            border-radius: 999px;
            background: #ecfdf5;
            color: #047857;
            font-weight: 700;
            font-size: 0.78rem;
            border: 1px solid #a7f3d0;
        }

        /* Insight block — "Why Flagged" navy gradient card */
        .insight-block {
            background: linear-gradient(135deg, var(--navy-950) 0%, var(--navy-800) 55%, var(--blue-600) 100%);
            border-radius: var(--radius);
            padding: 1.4rem 1.5rem;
            color: #ffffff;
            position: relative;
            overflow: hidden;
        }

        .insight-block::before {
            content: "";
            position: absolute;
            top: -40px;
            right: -40px;
            width: 140px;
            height: 140px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.04);
        }

        .insight-block h3 {
            font-size: 0.65rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: rgba(255, 255, 255, 0.55) !important;
            margin: 0 0 0.55rem 0;
        }

        .insight-list {
            margin: 0;
            padding-left: 1rem;
            color: rgba(255, 255, 255, 0.88);
            font-size: 0.9rem;
            line-height: 1.65;
        }

        .insight-list li {
            margin-bottom: 0.3rem;
        }

        .hint-text {
            font-size: 0.8rem;
            color: var(--text-500);
            margin-top: 0.3rem;
        }

        /* Main selectbox / inputs */
        [data-testid="stMain"] [data-baseweb="select"] > div {
            border-radius: var(--radius-sm) !important;
            border-color: var(--border-strong) !important;
            font-size: 0.875rem !important;
        }

        [data-testid="stMain"] .stTextInput input {
            border-radius: var(--radius-sm) !important;
            border-color: var(--border-strong) !important;
        }

        [data-testid="stMain"] [data-testid="stWidgetLabel"] p {
            font-weight: 600 !important;
            font-size: 0.84rem !important;
            color: var(--text-700) !important;
            letter-spacing: -0.01em !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def format_currency(x):
    return f"${x:,.0f}"


def render_kpi(col, label, value, *, emphasis: bool = False, sublabel: str = ""):
    mod = " kpi-card--emphasis" if emphasis else ""
    sub_html = f'<div class="kpi-sublabel">{sublabel}</div>' if sublabel else ""
    with col:
        st.markdown(
            f"""
            <div class="kpi-card{mod}">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                {sub_html}
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_alert_banner(title: str, body: str, icon: str = "⚡") -> None:
    st.markdown(
        f"""
        <div class="alert-banner">
            <div class="alert-banner__icon">{icon}</div>
            <div>
                <div class="alert-banner__title">{title}</div>
                <div class="alert-banner__body">{body}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_spacer(size: str = "md") -> None:
    cls = {
        "sm": "section-spacer--sm",
        "md": "section-spacer--md",
        "lg": "section-spacer--lg",
        "xl": "section-spacer--xl",
    }.get(size, "section-spacer--md")
    st.markdown(
        f'<div class="section-spacer {cls}" aria-hidden="true"></div>',
        unsafe_allow_html=True,
    )


def priority_badge(value):
    if str(value).lower() == "high":
        return '<span class="badge-high">High</span>'
    if str(value).lower() == "medium":
        return '<span class="badge-medium">Medium</span>'
    return '<span class="badge-low">Low</span>'


def apply_sidebar_filters(df):
    st.sidebar.markdown('<p class="sidebar-filters-label">Data Filters</p>', unsafe_allow_html=True)

    orgs = sorted(df["organization_name"].dropna().astype(str).unique().tolist())
    providers = sorted(df["provider_name"].dropna().astype(str).unique().tolist())
    priorities = sorted(df["financial_priority_bucket"].dropna().astype(str).unique().tolist())
    ages = sorted(df["claim_age_bucket"].dropna().astype(str).unique().tolist())
    statuses = sorted(df["status_primary"].dropna().astype(str).unique().tolist())

    selected_orgs = st.sidebar.multiselect("Organization", orgs)
    selected_providers = st.sidebar.multiselect("Provider", providers)
    selected_priorities = st.sidebar.multiselect("Priority bucket", priorities)
    selected_ages = st.sidebar.multiselect("Age bucket", ages)
    selected_statuses = st.sidebar.multiselect("Primary status", statuses)

    min_out = float(df["latest_outstanding"].min()) if len(df) else 0.0
    max_out = float(df["latest_outstanding"].max()) if len(df) else 1.0
    if min_out == max_out:
        max_out = min_out + 1.0

    out_range = st.sidebar.slider(
        "Latest outstanding range",
        min_value=float(min_out),
        max_value=float(max_out),
        value=(float(min_out), float(max_out)),
    )

    claim_search = st.sidebar.text_input("Search claim ID", placeholder="Type to filter…")

    filtered = df.copy()

    if selected_orgs:
        filtered = filtered[filtered["organization_name"].isin(selected_orgs)]
    if selected_providers:
        filtered = filtered[filtered["provider_name"].isin(selected_providers)]
    if selected_priorities:
        filtered = filtered[filtered["financial_priority_bucket"].isin(selected_priorities)]
    if selected_ages:
        filtered = filtered[filtered["claim_age_bucket"].isin(selected_ages)]
    if selected_statuses:
        filtered = filtered[filtered["status_primary"].isin(selected_statuses)]

    filtered = filtered[
        (filtered["latest_outstanding"] >= out_range[0])
        & (filtered["latest_outstanding"] <= out_range[1])
    ]

    if claim_search:
        filtered = filtered[
            filtered["claim_id"].astype(str).str.contains(claim_search, case=False, na=False)
        ]

    return filtered
