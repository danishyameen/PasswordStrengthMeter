# import streamlit as st
# import re
# import random
# import string
# from datetime import datetime

# # Set page configuration
# st.set_page_config(page_title='Giaic Password Guardian', page_icon='🔐', layout='centered')

# # Common password list
# COMMON_PASSWORDS = [
#     'password', '12345678', 'qwerty123', 'letmein', 'admin123',
#     'welcome1', 'monkey', 'sunshine', 'password1', '123456789'
# ]

# def check_password_strength(password: str) -> tuple:
#     score = 0
#     feedback = []

#     # Length Check
#     if len(password) >= 12:
#         score += 2
#         feedback.append("✅ Password length is excellent (12+ characters)")
#     elif len(password) >= 8:
#         score += 1
#         feedback.append("⚠️ Password length is good but could be longer (8+ recommended)")
#     else:
#         feedback.append("❌ Password should be at least 8 characters long")

#     # Character Diversity Check
#     checks = {
#         'uppercase': re.search(r"[A-Z]", password),
#         'lowercase': re.search(r"[a-z]", password),
#         'digit': re.search(r"\d", password),
#         'special': re.search(r"[!@#$%^&*]", password)
#     }
    
#     diversity_score = sum(1 for check in checks.values() if check)
#     score += diversity_score
#     if diversity_score == 4:
#         feedback.append("✅ Excellent character diversity (uppercase, lowercase, number, special)")
#     else:
#         missing = [k for k, v in checks.items() if not v]
#         feedback.append(f"❌ Missing character types: {', '.join(missing)}")

#     # Common Password Check
#     if password.lower() in COMMON_PASSWORDS:
#         score = max(0, score - 2)
#         feedback.append("❌ Password is in common passwords list - very insecure!")
#     else:
#         score += 1

#     # Final Evaluation
#     strength = "💪 Extremely Strong" if score >= 8 else \
#                "🔒 Strong" if score >= 6 else \
#                "🛡 Moderate" if score >= 4 else \
#                "⚠️ Weak"

#     return strength, score, feedback

# def generate_password(length=12):
#     """Generate a secure password with required character types"""
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     while True:
#         password = ''.join(random.choice(characters) for _ in range(length))
#         if (re.search(r"[A-Z]", password) and
#             re.search(r"[a-z]", password) and
#             re.search(r"\d", password) and
#             re.search(r"[!@#$%^&*]", password)):
#             return password

# # Custom CSS for animations and styling
# st.markdown("""
#     <style>
#     @keyframes gradient {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }
    
#     @keyframes bounce {
#         0%, 100% {transform: translateY(0);}
#         50% {transform: translateY(-10px);}
#     }
    
#     .sidebar .sidebar-content {
#         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#         color: white;
#     }
    
#     .metric-box {
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 10px;
#         padding: 20px;
#         margin: 10px 0;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         transition: transform 0.3s ease;
#     }
    
#     .metric-box:hover {
#         transform: translateY(-5px);
#     }
    
#     .stProgress > div > div > div {
#         background-image: linear-gradient(45deg, #00C853, #B2FF59);
#         border-radius: 4px;
#     }
    
#     .history-item {
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 8px;
#         padding: 15px;
#         margin: 10px 0;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
#         animation: slideIn 0.5s ease;
#     }
    
#     @keyframes slideIn {
#         from { transform: translateX(100px); opacity: 0; }
#         to { transform: translateX(0); opacity: 1; }
#     }
    
#     h1 {
#         text-align: center;
#         animation: bounce 2s infinite;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Initialize session state for history
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Animated sidebar
# with st.sidebar:
#     st.title("🔐 Giaic Security Password Guardian")

#     # Password Generator Section
#     st.markdown("---")
#     st.subheader("🔧 Password Generator")
#     pwd_length = st.number_input("Password Length", min_value=8, max_value=20, value=12, step=1)
    
#     if st.button("✨ Generate Secure Password", key="generate_btn"):
#         generated_pwd = generate_password(pwd_length)
#         st.session_state.pwd_input = generated_pwd  # Update main input field
#         st.session_state.generated_password = generated_pwd
    
#     if 'generated_password' in st.session_state:
#         st.markdown("### Generated Password")
#         st.code(st.session_state.generated_password, language="text")
        
#         # Copy button with feedback
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             if st.button("📋 Copy", key="copy_btn"):
#                 st.session_state.copied = True
#         if 'copied' in st.session_state:
#             st.success("Password copied to clipboard!")
#             del st.session_state.copied  # Clear the state after showing

#     st.markdown("---")
#     st.markdown("### Security Metrics")
#     st.markdown("""
#         <div class="metric-box">
#             <h3>🔑 Entropy Level</h3>
#             <p>Measures password complexity</p>
#         </div>
#         <div class="metric-box">
#             <h3>🛡 Threat Detection</h3>
#             <p>Checks against known breaches</p>
#         </div>
#         <div class="metric-box">
#             <h3>📈 Strength History</h3>
#             <p>Track your security progress</p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # # Password Generator Section
#     # st.markdown("---")
#     # st.subheader("🔧 Password Generator")
#     # pwd_length = st.number_input("Password Length", min_value=8, max_value=20, value=12, step=1)
    
#     # if st.button("✨ Generate Secure Password", key="generate_btn"):
#     #     generated_pwd = generate_password(pwd_length)
#     #     st.session_state.pwd_input = generated_pwd  # Update main input field
#     #     st.session_state.generated_password = generated_pwd
    
#     # if 'generated_password' in st.session_state:
#     #     st.markdown("### Generated Password")
#     #     st.code(st.session_state.generated_password, language="text")
        
#     #     # Copy button with feedback
#     #     col1, col2 = st.columns([1, 3])
#     #     with col1:
#     #         if st.button("📋 Copy", key="copy_btn"):
#     #             st.session_state.copied = True
#     #     if 'copied' in st.session_state:
#     #         st.success("Password copied to clipboard!")
#     #         del st.session_state.copied  # Clear the state after showing

# # Main content
# st.markdown("<h1>🔒 Giaic Password Strength Meter</h1>", unsafe_allow_html=True)
# password = st.text_input("Enter your password:", type="password", key="pwd_input")

# if st.button("🚀 Check Password Strength", use_container_width=True):
#     if password:
#         strength, score, feedback = check_password_strength(password)
        
#         # Update history
#         st.session_state.history.insert(0, {
#             'time': datetime.now().strftime("%Y-%m-%d %H:%M"),
#             'strength': strength,
#             'score': score,
#             'password': '*' * len(password)
#         })
        
#         # Keep only last 5 entries
#         if len(st.session_state.history) > 5:
#             st.session_state.history.pop()
        
#         # Display results
#         st.subheader(f"Security Assessment: {strength}")
#         st.progress(min(score/10, 1.0))
        
#         with st.expander("🔍 Detailed Security Analysis", expanded=True):
#             for item in feedback:
#                 st.markdown(f"- {item}")
        
#         # Security recommendations
#         if score < 6:
#             st.error("**Security Alert:** This password doesn't meet minimum security standards!")
#         else:
#             st.success("**Verified Secure:** This password meets recommended security standards!")
#     else:
#         st.warning("Please enter a password to analyze")

# # Display history
# if st.session_state.history:
#     st.subheader("📜 Security Check History")
#     for entry in st.session_state.history:
#         st.markdown(f"""
#         <div class="history-item">
#             <div style="display: flex; justify-content: space-between;">
#                 <div>{entry['time']}</div>
#                 <div>{entry['strength']}</div>
#             </div>
#             <div style="color: #666; margin-top: 5px;">
#                 {entry['password']} • Score: {entry['score']}/10
#             </div>
#         </div>
#         """, unsafe_allow_html=True)



# import streamlit as st
# import re
# import random
# import string
# from datetime import datetime

# # Set page configuration
# st.set_page_config(page_title='Giaic Password Guardian', page_icon='🔐', layout='centered')

# # Common password list
# COMMON_PASSWORDS = [
#     'password', '12345678', 'qwerty123', 'letmein', 'admin123',
#     'welcome1', 'monkey', 'sunshine', 'password1', '123456789'
# ]

# def check_password_strength(password: str) -> tuple:
#     score = 0
#     feedback = []

#     # Length Check
#     if len(password) >= 12:
#         score += 2
#         feedback.append("✅ Password length is excellent (12+ characters)")
#     elif len(password) >= 8:
#         score += 1
#         feedback.append("⚠️ Password length is good but could be longer (8+ recommended)")
#     else:
#         feedback.append("❌ Password should be at least 8 characters long")

#     # Character Diversity Check
#     checks = {
#         'uppercase': re.search(r"[A-Z]", password),
#         'lowercase': re.search(r"[a-z]", password),
#         'digit': re.search(r"\d", password),
#         'special': re.search(r"[!@#$%^&*]", password)
#     }
    
#     diversity_score = sum(1 for check in checks.values() if check)
#     score += diversity_score
#     if diversity_score == 4:
#         feedback.append("✅ Excellent character diversity (uppercase, lowercase, number, special)")
#     else:
#         missing = [k for k, v in checks.items() if not v]
#         feedback.append(f"❌ Missing character types: {', '.join(missing)}")

#     # Common Password Check
#     if password.lower() in COMMON_PASSWORDS:
#         score = max(0, score - 2)
#         feedback.append("❌ Password is in common passwords list - very insecure!")
#     else:
#         score += 1

#     # Final Evaluation
#     strength = "💪 Extremely Strong" if score >= 8 else \
#                "🔒 Strong" if score >= 6 else \
#                "🛡 Moderate" if score >= 4 else \
#                "⚠️ Weak"

#     return strength, score, feedback

# def generate_password(length=12):
#     """Generate a secure password with required character types"""
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     while True:
#         password = ''.join(random.choice(characters) for _ in range(length))
#         if (re.search(r"[A-Z]", password) and
#             re.search(r"[a-z]", password) and
#             re.search(r"\d", password) and
#             re.search(r"[!@#$%^&*]", password)):
#             return password

# # Custom CSS for animations and styling
# st.markdown("""
#     <style>
#     @keyframes gradient {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }
    
#     @keyframes bounce {
#         0%, 100% {transform: translateY(0);}
#         50% {transform: translateY(-10px);}
#     }
    
#     .sidebar .sidebar-content {
#         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#         color: white;
#     }
    
#     .metric-box {
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 10px;
#         padding: 20px;
#         margin: 10px 0;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         transition: transform 0.3s ease;
#     }
    
#     .metric-box:hover {
#         transform: translateY(-5px);
#     }
    
#     .stProgress > div > div > div {
#         background-image: linear-gradient(45deg, #00C853, #B2FF59);
#         border-radius: 4px;
#     }
    
#     .history-item {
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 8px;
#         padding: 15px;
#         margin: 10px 0;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
#         animation: slideIn 0.5s ease;
#     }
    
#     @keyframes slideIn {
#         from { transform: translateX(100px); opacity: 0; }
#         to { transform: translateX(0); opacity: 1; }
#     }
    
#     h1 {
#         text-align: center;
#         animation: bounce 2s infinite;
#     }
    
#     .requirements {
#         background: #f8f9fa;
#         border-left: 4px solid #2196F3;
#         padding: 15px;
#         margin: 15px 0;
#         border-radius: 4px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Initialize session state for history
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Animated sidebar
# with st.sidebar:
#     st.title("🔐 Giaic Security Password Guardian")
    
#     # Password Generator Section
#     st.markdown("---")
#     st.subheader("🔧 Password Generator")
#     pwd_length = st.number_input("Password Length", min_value=8, max_value=20, value=12, step=1)
    
#     if st.button("✨ Generate Secure Password", key="generate_btn"):
#         generated_pwd = generate_password(pwd_length)
#         st.session_state.pwd_input = generated_pwd  # Update main input field
#         st.session_state.generated_password = generated_pwd
    
#     if 'generated_password' in st.session_state:
#         st.markdown("### Generated Password")
#         st.code(st.session_state.generated_password, language="text")
        
#         # Copy button with feedback
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             if st.button("📋 Copy", key="copy_btn"):
#                 st.session_state.copied = True
#         if 'copied' in st.session_state:
#             st.success("Password copied to clipboard!")
#             del st.session_state.copied  # Clear the state after showing
    
#     st.markdown("---")
#     st.markdown("### Security Metrics")
#     st.markdown("""
#         <div class="metric-box">
#             <h3>🔑 Entropy Level</h3>
#             <p>Measures password complexity</p>
#         </div>
#         <div class="metric-box">
#             <h3>🛡 Threat Detection</h3>
#             <p>Checks against known breaches</p>
#         </div>
#         <div class="metric-box">
#             <h3>📈 Strength History</h3>
#             <p>Track your security progress</p>
#         </div>
#     """, unsafe_allow_html=True)
    
    

# # Main content
# st.markdown("<h1>🔒 Giaic Password Strength Meter</h1>", unsafe_allow_html=True)
# password = st.text_input("Enter your password:", type="password", key="pwd_input")

# # Add minimum security standards guidance
# st.markdown("""
# <div class="metric-box">
#     <h4>🔐 Minimum Security Requirements</h4>
#     <ul style="list-style-type: none; padding-left: 0;">
#         <li>✅ At least 8 characters (12+ recommended)</li>
#         <li>✅ Mix of uppercase & lowercase letters</li>
#         <li>✅ At least one number (0-9)</li>
#         <li>✅ At least one special character (!@#$%^&*)</li>
#         <li>✅ Not a common or dictionary word</li>
#     </ul>
#     <p style="color: #666; margin: 5px 0 0 0;">Meeting these requirements is essential for basic security</p>
# </div>
# """, unsafe_allow_html=True)

# if st.button("🚀 Check Password Strength", use_container_width=True):
#     if password:
#         strength, score, feedback = check_password_strength(password)
        
#         # Update history
#         st.session_state.history.insert(0, {
#             'time': datetime.now().strftime("%Y-%m-%d %H:%M"),
#             'strength': strength,
#             'score': score,
#             'password': '*' * len(password)
#         })
        
#         # Keep only last 5 entries
#         if len(st.session_state.history) > 5:
#             st.session_state.history.pop()
        
#         # Display results
#         st.subheader(f"Security Assessment: {strength}")
#         st.progress(min(score/10, 1.0))
        
#         with st.expander("🔍 Detailed Security Analysis", expanded=True):
#             for item in feedback:
#                 st.markdown(f"- {item}")
        
#         # Security recommendations
#         if score < 6:
#             st.error("**Security Alert:** This password doesn't meet minimum security standards!")
#         else:
#             st.success("**Verified Secure:** This password meets recommended security standards!")
#     else:
#         st.warning("Please enter a password to analyze")

# # Display history
# if st.session_state.history:
#     st.subheader("📜 Security Check History")
#     for entry in st.session_state.history:
#         st.markdown(f"""
#         <div class="history-item">
#             <div style="display: flex; justify-content: space-between;">
#                 <div>{entry['time']}</div>
#                 <div>{entry['strength']}</div>
#             </div>
#             <div style="color: #666; margin-top: 5px;">
#                 {entry['password']} • Score: {entry['score']}/10
#             </div>
#         </div>
#         """, unsafe_allow_html=True)


# import streamlit as st
# import re
# import random
# import string
# from datetime import datetime

# # Set page configuration
# st.set_page_config(page_title='Giaic Password Guardian', page_icon='🔐', layout='centered')

# # Common password list
# COMMON_PASSWORDS = [
#     'password', '12345678', 'qwerty123', 'letmein', 'admin123',
#     'welcome1', 'monkey', 'sunshine', 'password1', '123456789'
# ]

# def check_password_strength(password: str) -> tuple:
#     score = 0
#     feedback = []
#     criteria_met = {
#         'length': False,
#         'uppercase': False,
#         'lowercase': False,
#         'digit': False,
#         'special': False,
#         'not_common': False
#     }

#     # Length Check
#     length_ok = len(password) >= 8
#     criteria_met['length'] = length_ok
#     if len(password) >= 12:
#         score += 2
#         feedback.append("✅ Password length is excellent (12+ characters)")
#     elif length_ok:
#         score += 1
#         feedback.append("⚠️ Password length is good but could be longer (8+ recommended)")
#     else:
#         feedback.append("❌ Password should be at least 8 characters long")

#     # Character Diversity Check
#     checks = {
#         'uppercase': bool(re.search(r"[A-Z]", password)),
#         'lowercase': bool(re.search(r"[a-z]", password)),
#         'digit': bool(re.search(r"\d", password)),
#         'special': bool(re.search(r"[!@#$%^&*]", password))
#     }
    
#     criteria_met['uppercase'] = checks['uppercase']
#     criteria_met['lowercase'] = checks['lowercase']
#     criteria_met['digit'] = checks['digit']
#     criteria_met['special'] = checks['special']
    
#     diversity_score = sum(checks.values())
#     score += diversity_score
#     if diversity_score == 4:
#         feedback.append("✅ Excellent character diversity (uppercase, lowercase, number, special)")
#     else:
#         missing = [k for k, v in checks.items() if not v]
#         feedback.append(f"❌ Missing character types: {', '.join(missing)}")

#     # Common Password Check
#     not_common = password.lower() not in COMMON_PASSWORDS
#     criteria_met['not_common'] = not_common
#     if not not_common:
#         score = max(0, score - 2)
#         feedback.append("❌ Password is in common passwords list - very insecure!")
#     else:
#         score += 1

#     # Final Evaluation
#     strength = "💪 Extremely Strong" if score >= 8 else \
#                "🔒 Strong" if score >= 6 else \
#                "🛡 Moderate" if score >= 4 else \
#                "⚠️ Weak"

#     return strength, score, feedback, criteria_met

# def generate_password(length=12):
#     """Generate a secure password with required character types"""
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     while True:
#         password = ''.join(random.choice(characters) for _ in range(length))
#         if (re.search(r"[A-Z]", password) and
#             re.search(r"[a-z]", password) and
#             re.search(r"\d", password) and
#             re.search(r"[!@#$%^&*]", password)):
#             return password

# # Custom CSS for animations and styling
# st.markdown("""
#     <style>
#     @keyframes gradient {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }
    
#     @keyframes bounce {
#         0%, 100% {transform: translateY(0);}
#         50% {transform: translateY(-10px);}
#     }
    
#     .sidebar .sidebar-content {
#         background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#         color: white;
#     }
    
#     .metric-box {
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 10px;
#         padding: 20px;
#         margin: 10px 0;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         transition: transform 0.3s ease;
#     }
    
#     .metric-box:hover {
#         transform: translateY(-5px);
#     }
    
#     .stProgress > div > div > div {
#         background-image: linear-gradient(45deg, #00C853, #B2FF59);
#         border-radius: 4px;
#     }
    
#     .history-item {
#         background: rgba(255, 255, 255, 0.9);
#         border-radius: 8px;
#         padding: 15px;
#         margin: 10px 0;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
#         animation: slideIn 0.5s ease;
#     }
    
#     @keyframes slideIn {
#         from { transform: translateX(100px); opacity: 0; }
#         to { transform: translateX(0); opacity: 1; }
#     }
    
#     h1 {
#         text-align: center;
#         animation: bounce 2s infinite;
#     }
    
#     .criteria-item {
#         font-size: 16px;
#         margin: 8px 0;
#         transition: all 0.3s ease;
#     }
    
#     .criteria-met {
#         color: #4CAF50 !important;
#         font-weight: bold;
#     }
    
#     .criteria-unmet {
#         color: #FF0000 !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Initialize session state
# if 'history' not in st.session_state:
#     st.session_state.history = []
# if 'criteria_met' not in st.session_state:
#     st.session_state.criteria_met = {
#         'length': False,
#         'uppercase': False,
#         'lowercase': False,
#         'digit': False,
#         'special': False,
#         'not_common': False
#     }

# # Animated sidebar
# with st.sidebar:
#     st.title("🔐 Giaic Security Password Guardian")
    
#     # Password Generator Section
#     st.markdown("---")
#     st.subheader("🔧 Password Generator")
#     pwd_length = st.number_input("Password Length", min_value=8, max_value=20, value=12, step=1)
    
#     if st.button("✨ Generate Secure Password", key="generate_btn"):
#         generated_pwd = generate_password(pwd_length)
#         st.session_state.pwd_input = generated_pwd
#         st.session_state.generated_password = generated_pwd
    
#     if 'generated_password' in st.session_state:
#         st.markdown("### Generated Password")
#         st.code(st.session_state.generated_password, language="text")
        
#         # Copy button with feedback
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             if st.button("📋 Copy", key="copy_btn"):
#                 st.session_state.copied = True
#         if 'copied' in st.session_state:
#             st.success("Password copied to clipboard!")
#             del st.session_state.copied
    
#     st.markdown("---")
#     st.markdown("### Security Metrics")
#     st.markdown("""
#         <div class="metric-box">
#             <h3>🔑 Entropy Level</h3>
#             <p>Measures password complexity</p>
#         </div>
#         <div class="metric-box">
#             <h3>🛡 Threat Detection</h3>
#             <p>Checks against known breaches</p>
#         </div>
#         <div class="metric-box">
#             <h3>📈 Strength History</h3>
#             <p>Track your security progress</p>
#         </div>
#     """, unsafe_allow_html=True)
    
    

# # Main content
# st.markdown("<h1>🔒 Giaic Password Strength Meter</h1>", unsafe_allow_html=True)
# password = st.text_input("Enter your password:", type="password", key="pwd_input")

# # Minimum Security Standards Checklist
# st.subheader("🔐 Minimum Security Standards Guidance")
# criteria_list = [
#     ("At least 8 characters long", 'length'),
#     ("Contains uppercase letters (A-Z)", 'uppercase'),
#     ("Contains lowercase letters (a-z)", 'lowercase'),
#     ("Contains numbers (0-9)", 'digit'),
#     ("Contains special characters (!@#$%^&*)", 'special'),
#     ("Not a commonly used password", 'not_common')
# ]

# for desc, key in criteria_list:
#     met = st.session_state.criteria_met[key]
#     icon = "✅" if met else "❌"
#     css_class = "criteria-met" if met else "criteria-unmet"
#     st.markdown(f"""
#         <div class="criteria-item {css_class}">
#             {icon} {desc}
#         </div>
#     """, unsafe_allow_html=True)

# if st.button("🚀 Check Password Strength", use_container_width=True):
#     if password:
#         strength, score, feedback, criteria_met = check_password_strength(password)
#         st.session_state.criteria_met = criteria_met
        
#         # Update history
#         st.session_state.history.insert(0, {
#             'time': datetime.now().strftime("%Y-%m-%d %H:%M"),
#             'strength': strength,
#             'score': score,
#             'password': '*' * len(password)
#         })
        
#         # Keep only last 5 entries
#         if len(st.session_state.history) > 5:
#             st.session_state.history.pop()
        
#         # Display results
#         st.subheader(f"Security Assessment: {strength}")
#         st.progress(min(score/10, 1.0))
        
#         with st.expander("🔍 Detailed Security Analysis", expanded=True):
#             for item in feedback:
#                 st.markdown(f"- {item}")
        
#         # Security recommendations
#         if score < 6:
#             st.error("**Security Alert:** This password doesn't meet minimum security standards!")
#         else:
#             st.success("**Verified Secure:** This password meets recommended security standards!")
#     else:
#         st.warning("Please enter a password to analyze")

# # Display history
# if st.session_state.history:
#     st.subheader("📜 Security Check History")
#     for entry in st.session_state.history:
#         st.markdown(f"""
#         <div class="history-item">
#             <div style="display: flex; justify-content: space-between;">
#                 <div>{entry['time']}</div>
#                 <div>{entry['strength']}</div>
#             </div>
#             <div style="color: #666; margin-top: 5px;">
#                 {entry['password']} • Score: {entry['score']}/10
#             </div>
#         </div>
#         """, unsafe_allow_html=True)


import streamlit as st
import re
import random
import string
from datetime import datetime

# Set page configuration
st.set_page_config(page_title='Giaic Password Guardian', page_icon='🔐', layout='centered')

# Common password list
COMMON_PASSWORDS = [
    'password', '12345678', 'qwerty123', 'letmein', 'admin123',
    'welcome1', 'monkey', 'sunshine', 'password1', '123456789'
]

def check_password_strength(password: str) -> tuple:
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Password length is excellent (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️ Password length is good but could be longer (8+ recommended)")
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    # Character Diversity Check
    checks = {
        'uppercase': re.search(r"[A-Z]", password),
        'lowercase': re.search(r"[a-z]", password),
        'digit': re.search(r"\d", password),
        'special': re.search(r"[!@#$%^&*]", password)
    }
    
    diversity_score = sum(1 for check in checks.values() if check)
    score += diversity_score
    if diversity_score == 4:
        feedback.append("✅ Excellent character diversity (uppercase, lowercase, number, special)")
    else:
        missing = [k for k, v in checks.items() if not v]
        feedback.append(f"❌ Missing character types: {', '.join(missing)}")

    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        score = max(0, score - 2)
        feedback.append("❌ Password is in common passwords list - very insecure!")
    else:
        score += 1

    # Final Evaluation
    strength = "💪 Extremely Strong" if score >= 8 else \
               "🔒 Strong" if score >= 6 else \
               "🛡 Moderate" if score >= 4 else \
               "⚠️ Weak"

    return strength, score, feedback

def generate_password(length=12):
    """Generate a secure password with required character types"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"\d", password) and
            re.search(r"[!@#$%^&*]", password)):
            return password

# Custom CSS for animations and styling
st.markdown("""
    <style>
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    @keyframes bounce {
        0%, 100% {transform: translateY(0);}
        50% {transform: translateY(-10px);}
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }
    
    .metric-box {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-box:hover {
        transform: translateY(-5px);
    }
    
    .stProgress > div > div > div {
        background-image: linear-gradient(45deg, #00C853, #B2FF59);
        border-radius: 4px;
    }
    
    .history-item {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        animation: slideIn 0.5s ease;
    }
    
    .requirement-met {
        color: #00C853 !important;
        font-weight: bold !important;
    }
    
    .requirement-unmet {
        color: #ff0000 !important;
    }
    
    @keyframes slideIn {
        from { transform: translateX(100px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    h1 {
        text-align: center;
        animation: bounce 2s infinite;
    }
    
    .security-checklist {
        padding: 15px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

def check_minimum_standards(password):
    return {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*]', password))
    }

# Animated sidebar
with st.sidebar:
    st.title("🔐 Giaic Security Password Guardian")
    
    # Password Generator Section
    st.markdown("---")
    st.subheader("🔧 Password Generator")
    pwd_length = st.number_input("Password Length", min_value=8, max_value=20, value=12, step=1)
    
    if st.button("✨ Generate Secure Password", key="generate_btn"):
        generated_pwd = generate_password(pwd_length)
        st.session_state.pwd_input = generated_pwd
        st.session_state.generated_password = generated_pwd
    
    if 'generated_password' in st.session_state:
        st.markdown("### Generated Password")
        st.code(st.session_state.generated_password, language="text")
        
        # Copy button with feedback
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("📋 Copy", key="copy_btn"):
                st.session_state.copied = True
        if 'copied' in st.session_state:
            st.success("Password copied to clipboard!")
            del st.session_state.copied
    
    st.markdown("---")
    st.markdown("### Security Metrics")
    st.markdown("""
        <div class="metric-box">
            <h3>🔑 Entropy Level</h3>
            <p>Measures password complexity</p>
        </div>
        <div class="metric-box">
            <h3>🛡 Threat Detection</h3>
            <p>Checks against known breaches</p>
        </div>
        <div class="metric-box">
            <h3>📈 Strength History</h3>
            <p>Track your security progress</p>
        </div>
    """, unsafe_allow_html=True)
    
    

# Main content
st.markdown("<h1>🔒 Giaic Password Strength Meter</h1>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password", key="pwd_input")

# Real-time security standards checklist
if password:
    standards = check_minimum_standards(password)
    common_password = password.lower() in COMMON_PASSWORDS
else:
    standards = {key: False for key in ['length', 'uppercase', 'lowercase', 'digit', 'special']}
    common_password = False

with st.container():
    st.markdown("""
    <div class="security-checklist">
        <h4>🔍 Minimum Security Standards</h4>
    """, unsafe_allow_html=True)
    
    checklist_items = [
        ("At least 8 characters", 'length'),
        ("Contains uppercase letter (A-Z)", 'uppercase'),
        ("Contains lowercase letter (a-z)", 'lowercase'),
        ("Contains digit (0-9)", 'digit'),
        ("Contains special character (!@#$%^&*)", 'special'),
        ("Not a common password", 'common')
    ]
    
    for text, key in checklist_items:
        if key == 'common':
            met = not common_password
            icon = "✅" if met else "❌"
            color_class = "requirement-met" if met else "requirement-unmet"
            st.markdown(f"""
            <div style="margin: 8px 0; padding: 5px;">
                <span style="font-size: 1.2em;">{icon}</span>
                <span class="{color_class}">{text}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            met = standards.get(key, False)
            icon = "✅" if met else "❌"
            color_class = "requirement-met" if met else "requirement-unmet"
            st.markdown(f"""
            <div style="margin: 8px 0; padding: 5px;">
                <span style="font-size: 1.2em;">{icon}</span>
                <span class="{color_class}">{text}</span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if common_password:
    st.error("⚠️ Warning: This password is in a list of commonly used passwords!")

if st.button("🚀 Check Password Strength", use_container_width=True):
    if password:
        strength, score, feedback = check_password_strength(password)
        
        # Update history
        st.session_state.history.insert(0, {
            'time': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'strength': strength,
            'score': score,
            'password': '*' * len(password)
        })
        
        # Keep only last 5 entries
        if len(st.session_state.history) > 5:
            st.session_state.history.pop()
        
        # Display results
        st.subheader(f"Security Assessment: {strength}")
        st.progress(min(score/10, 1.0))
        
        with st.expander("🔍 Detailed Security Analysis", expanded=True):
            for item in feedback:
                st.markdown(f"- {item}")
        
        # Security recommendations
        if score < 6:
            st.error("**Security Alert:** This password doesn't meet minimum security standards!")
        else:
            st.success("**Verified Secure:** This password meets recommended security standards!")
    else:
        st.warning("Please enter a password to analyze")

# Display history
if st.session_state.history:
    st.subheader("📜 Security Check History")
    for entry in st.session_state.history:
        st.markdown(f"""
        <div class="history-item">
            <div style="display: flex; justify-content: space-between;">
                <div>{entry['time']}</div>
                <div>{entry['strength']}</div>
            </div>
            <div style="color: #666; margin-top: 5px;">
                {entry['password']} • Score: {entry['score']}/10
            </div>
        </div>
        """, unsafe_allow_html=True)