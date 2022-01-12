mkdir -p ~/.streamlit/
echo "[theme]
backgroundColor="#06060a"
secondaryBackgroundColor="#292b35"
textColor="#fdfbfb"
font="serif"
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml